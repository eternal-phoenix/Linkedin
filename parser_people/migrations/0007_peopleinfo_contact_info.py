# Generated by Django 4.2.2 on 2023-07-07 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_people', '0006_rename_peoplekeywords_peoplelinks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='peopleinfo',
            name='contact_info',
            field=models.CharField(blank=True, max_length=510, null=True),
        ),
    ]
