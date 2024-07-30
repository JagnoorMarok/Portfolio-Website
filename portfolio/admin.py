from django.contrib import admin
from .models import Image, Experience, Responsibility, Skill, Education

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_url', 'uploaded_at')
    search_fields = ('title',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'start_date', 'end_date')
    search_fields = ('title', 'organization')

@admin.register(Responsibility)
class ResponsibilityAdmin(admin.ModelAdmin):
    list_display = ('title', 'organization', 'start_date', 'end_date')
    search_fields = ('title', 'organization')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('institution', 'start_year', 'end_year')
    search_fields = ('institution',)