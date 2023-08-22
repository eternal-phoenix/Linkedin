from django.db import models

class CompaniesKeywords(models.Model):
    company_name = models.CharField(max_length=250, null=True, blank=True) 
    link = models.URLField(max_length=250, unique=True)
    status = models.CharField(max_length=25, default='New')

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links' 


class CompanyInfo(models.Model):
    link = models.URLField(max_length=250, unique=True)
    company_website = models.CharField(max_length=250, null=True, blank=True)
    company_name = models.CharField(max_length=250, null=True, blank=True)
    company_size = models.CharField(max_length=250, null=True)
    company_founded = models.CharField(max_length=250, null=True, blank=True)
    company_specialties = models.CharField(max_length=250, null=True, blank=True)
    industry = models.CharField(max_length=250, null=True, blank=True)
    company_headquarters = models.CharField(max_length=250, null=True)
    nasdaq = models.CharField(max_length=250, null=True, blank=True)
    ipo = models.CharField(max_length=250, null=True)
    programs = models.CharField(max_length=250, null=True, blank=True)
    learning = models.CharField(max_length=250, null=True, blank=True)
    job_actual = models.CharField(max_length=250, null=True, blank=True)
    location = models.CharField(max_length=250, null=True)
    phone = models.CharField(max_length=250, null=True)
    overview = models.TextField(null=True)


    status = models.CharField(max_length=25, default='New')

    def __str__(self):
        return self.company_name

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies' 
