from django.contrib import admin
from .models import PeopleLinks, PeopleInfo
# Register your models here.


@admin.register(PeopleLinks)
class PeopleLinks(admin.ModelAdmin):
    list_display = ('link', 'status')

@admin.register(PeopleInfo)
class PeopleInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'job', 'geo', 'connections', 'education', 'contact_info')
