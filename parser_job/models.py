from django.db import models

class JobKeywords(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=250, unique=True)
    status = models.CharField(max_length=50, default='New') 

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'

# class JobInfo(models.Model):
#     vacancy = models.CharField(max_length=250)
#     name_company = models.CharField(max_length=250)
#     link = models.CharField(max_length=250, unique=True)
#     geo = models.CharField(max_length=250, null=True, blank=True)
#     workplacetype = models.CharField(max_length=250, null=True, blank=True)
#     schedule = models.CharField(max_length=250, null=True, blank=True)
#     about_vacancy = models.CharField(max_length=5000, default="")
#     about_company = models.CharField(max_length=5000, default="")
#     status = models.CharField(max_length=25, default='New')


class JobInfo(models.Model):
    link = models.CharField(max_length=510, unique=True)
    vacancy = models.CharField(max_length=255, null=True, blank=True)
    name_company = models.CharField(max_length=255, null=True, blank=True)
    geo = models.CharField(max_length=255, null=True, blank=True)
    about_vacancy = models.TextField(null=True, blank=True)
    seniority_level = models.CharField(max_length=255, null=True, blank=True)
    employment_type = models.CharField(max_length=255, null=True, blank=True)
    job_functions = models.CharField(max_length=255, null=True, blank=True)
    industries = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=25, default='New')

    def __str__(self):
        return self.vacancy

    class Meta:
        verbose_name = 'Vacancy'
        verbose_name_plural = 'Job' 
