# Generated by Django 4.2.1 on 2023-06-13 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parser_job', '0009_delete_companieskeywords_delete_companyinfo_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='jobkeywords',
            options={'verbose_name': 'Link', 'verbose_name_plural': 'Links'},
        ),
    ]