# Generated by Django 3.2.13 on 2023-02-27 09:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='detail_page',
            options={'ordering': ['-id']},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-id']},
        ),
    ]
