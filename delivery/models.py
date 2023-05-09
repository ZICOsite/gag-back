from django.db import models
from catalogue.models import Main_Directions,Product_card


class Delivery(models.Model):
  delivery_time=models.DateField()
  directions=models.ForeignKey(Main_Directions, on_delete=models.PROTECT ,related_name='directions')
  product_name=models.ForeignKey(Product_card, on_delete=models.PROTECT ,related_name='product_name')
  quantity = models.CharField(max_length=255)
  quantity_ru = models.CharField(max_length=255)
  customer=models.CharField(max_length=255)
  customer_ru=models.CharField(max_length=255)
  
 
  class Meta:
    ordering = ['id']