from django.contrib import admin
from .models import CompaniesKeywords, CompanyInfo


class CompaniesKeywordsAdmin(admin.ModelAdmin):
    list_display = ('link', 'company_name', 'status')

class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ('link', 'company_website', 'company_name', 'company_size', 'company_founded', 'company_specialties', 'industry', 'company_headquarters', 'ipo', 'programs', 'learning', 'job_actual', 'location', 'phone')

admin.site.register(CompaniesKeywords, CompaniesKeywordsAdmin)
admin.site.register(CompanyInfo, CompanyInfoAdmin)
