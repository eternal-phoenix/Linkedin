from django.contrib import admin

from .models import JobKeywords, JobInfo

class JobKeywordsAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'status')

# class JobInfoAdmin(admin.ModelAdmin):
#     list_display = ('vacancy', 'name_company', 'geo', 'workplacetype', 'schedule', 'status')

class JobInfoAdmin(admin.ModelAdmin):
    list_display =  ('vacancy', 'name_company', 'geo', 'seniority_level', 'employment_type', 'job_functions', 'industries', 'status', )

admin.site.register(JobKeywords, JobKeywordsAdmin)
admin.site.register(JobInfo, JobInfoAdmin)