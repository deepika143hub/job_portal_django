from django.contrib import admin
from .models import Job, Application

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'job_type', 'created_at', 'posted_by')
    search_fields = ('title', 'company', 'location')
    list_filter = ('job_type', 'created_at')


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'job', 'status', 'applied_at', 'user')
    list_filter = ('status', 'applied_at')
    search_fields = ('name', 'email', 'job__title')
