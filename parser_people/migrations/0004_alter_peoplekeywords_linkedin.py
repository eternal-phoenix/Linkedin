# Generated by Django 4.2.1 on 2023-06-14 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_people', '0003_remove_peoplekeywords_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peoplekeywords',
            name='linkedin',
            field=models.CharField(max_length=250, unique=True),
        ),
    ]