# portfolio/urls.py

from django.urls import path
from . import views
from .views import  load_more_images

urlpatterns = [
    path('', views.home, name='home'),
    path('resume/', views.resume, name='resume'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('portfolio/load-more/', load_more_images, name='load_more_images'),

]
