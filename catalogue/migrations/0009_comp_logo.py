# Generated by Django 3.2.13 on 2023-05-05 06:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0008_auto_20230325_0617'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comp_logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='catalogue/company_logo/')),
                ('company_logo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='company_logo', to='catalogue.main_directions')),
            ],
        ),
    ]
