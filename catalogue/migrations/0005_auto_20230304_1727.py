# Generated by Django 3.2.13 on 2023-03-04 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_alter_product_images_product_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='characteristics',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='product_images',
            options={'ordering': ['id']},
        ),
    ]
