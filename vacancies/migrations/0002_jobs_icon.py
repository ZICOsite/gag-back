# Generated by Django 3.2.13 on 2023-02-28 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacancies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='jobs/icon/'),
        ),
    ]
