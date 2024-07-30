from django.db import models

class Image(models.Model):
    title = models.CharField(max_length=255)
    image_url = models.URLField(max_length=2000)  # Store Google Drive image URLs
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('Programming Languages', 'Programming Languages'),
        ('Web Development', 'Web Development'),
        ('Frameworks/Libraries', 'Frameworks/Libraries'),
        ('Technologies', 'Technologies'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.name
    


class Experience(models.Model):
    title = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.organization}"

class Responsibility(models.Model):
    title = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    start_date = models.CharField(max_length=100)
    end_date = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.organization}"

class Education(models.Model):
    institution = models.CharField(max_length=255)
    start_year = models.CharField(max_length=100)
    end_year = models.CharField(max_length=100, blank=True, null=True)
    details = models.TextField()

    def __str__(self):
        return f"{self.institution} ({self.start_year}-{self.end_year or 'Present'})"