# Generated by Django 3.2.13 on 2023-03-25 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0007_auto_20230325_0540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_detailpage',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='product_detailpage',
            name='title_ru',
        ),
    ]
