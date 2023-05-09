from delivery.models import Delivery
from rest_framework import serializers

class Delivery_Serializer(serializers.ModelSerializer):
  product_name = serializers.DateField(source='product_name.title_en')
  directions = serializers.DateField(source='directions.title_en')
  class Meta:
    model=Delivery
    fields=[  
      
      'delivery_time',
      'directions',
      'product_name',
      'quantity',
      'customer',
  
      
      
    ]

class Delivery_Serializer_ru(serializers.ModelSerializer):
  product_name = serializers.DateField(source='product_name.title_ru')
  directions = serializers.DateField(source='directions.title_ru')
  class Meta:
    model=Delivery
    fields=[  
      'delivery_time',
      'directions',
      'product_name',
      'quantity_ru',
      'customer_ru',
      
  
    ]