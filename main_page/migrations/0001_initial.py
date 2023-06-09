# Generated by Django 3.2.13 on 2023-02-27 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Main_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(max_length=255)),
                ('title_en', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='main_page/banner_image/')),
                ('file', models.FileField(upload_to='main_page/catalogue_doc/')),
                ('text_en', models.TextField()),
                ('text_ru', models.TextField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
