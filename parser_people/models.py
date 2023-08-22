from django.db import models


class PeopleLinks(models.Model):
    link = models.CharField(max_length=250, unique=True)
    status = models.CharField(max_length=25, default='New')

    def __str__(self):
        return self.link

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links' 


class PeopleInfo(models.Model):
    link = models.CharField(max_length=250, unique=True)
    name = models.CharField(max_length=250)
    job = models.CharField(max_length=250, null=True, blank=True)
    geo = models.CharField(max_length=250, null=True, blank=True)
    connections = models.CharField(max_length=250, null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    skils = models.TextField(null=True, blank=True)
    education = models.TextField(null=True, blank=True)
    experience = models.TextField(null=True, blank=True)
    contact_info = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Person'
        verbose_name_plural = 'People'