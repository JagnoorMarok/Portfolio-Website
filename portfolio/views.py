from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from django.http import JsonResponse
from .models import Image, Skill, Experience, Responsibility, Education
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .forms import ContactForm

# Create your views here.

def home(request):
    return render(request, 'portfolio/home.html')

def resume(request):
    categories = Skill.CATEGORY_CHOICES
    skills = Skill.objects.all()
    skills_by_category = {category[0]: [] for category in categories}
    experiences = Experience.objects.all()
    responsibilities = Responsibility.objects.all()
    education = Education.objects.all()
    
    for skill in skills:
        skills_by_category[skill.category].append(skill.name)
    
    return render(request, 'portfolio/resume.html', {'education': education,'experiences': experiences,
        'responsibilities': responsibilities,'skills_by_category': skills_by_category})

def portfolio(request):
    images = Image.objects.order_by('-uploaded_at')[:10]  # Load initial 10 images
    return render(request, 'portfolio/portfolio.html', {'images': images})

def contact(request):
    message = ''
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message_text = form.cleaned_data['message']

            subject = 'Contact Form Submission'
            body = f"Name: {name}\nEmail: {email}\nMessage: {message_text}"

            try:
                send_mail(subject, body, settings.EMAIL_HOST_USER, [settings.EMAIL_RECIEVER])
                message = 'Email sent successfully'
            except Exception as e:
                message = f'Error: {str(e)}'
    else:
        form = ContactForm()

    return render(request, 'portfolio/contact.html', {'form': form, 'message': message})


def load_more_images(request):
    if request.is_ajax():
        page = request.GET.get('page', None)
        images_list = Image.objects.order_by('-uploaded_at')
        paginator = Paginator(images_list, 10)  # Show 10 images per page

        try:
            images = paginator.page(page)
        except PageNotAnInteger:
            images = paginator.page(1)
        except EmptyPage:
            images = []

        images_data = []
        for image in images:
            images_data.append({
                'title': image.title,
                'image_url': image.image_url,
            })

        return JsonResponse({'images': images_data})
    