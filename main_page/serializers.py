from main_page.models import Main_page
from rest_framework import serializers
from collections import OrderedDict


class Main_Page_Serializer(serializers.ModelSerializer):

  
  class Meta:
    model=Main_page
    fields=[  
      'id',
      'title_en',
      'image',
 
      
      'text_en',
      
      
    ]
  def to_representation(self, instance):
      result = super(Main_Page_Serializer, self).to_representation(instance)
      return OrderedDict([(key, result[key]) for key in result if result[key] is not None])
    

class Main_Page_Serializer_ru(serializers.ModelSerializer):

  class Meta:
    model=Main_page
    fields=[
      'id',
      'title_ru',
      
      'image',

      
      'text_ru',
      
    ]
  def to_representation(self, instance):
      result = super(Main_Page_Serializer_ru, self).to_representation(instance)
      return OrderedDict([(key, result[key]) for key in result if result[key] is not None])

