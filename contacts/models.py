from django.db import models


class Contacts(models.Model):
  text_loc_ru = models.CharField(max_length=255)
  text_loc_en = models.CharField(max_length=255)
  text_loc2_en =models.CharField(max_length=255)
  text_loc2_ru=models.CharField(max_length=255)
  tel1=models.CharField(max_length=255)
  tel2=models.CharField(max_length=255)
  tel3=models.CharField(max_length=255)
  email=models.EmailField(max_length=254)
  class Meta:
    ordering = ['id']

