from contacts.models import Contacts
from rest_framework import serializers

class Contacts_Serializer(serializers.ModelSerializer):

  class Meta:
    model=Contacts
    fields=[
    'text_loc_en',
    'text_loc2_en',
    'tel1',
    'tel2',
    'tel3',
    'email',
  
      
    ]
class Contacts_ru_Serializer(serializers.ModelSerializer):

  class Meta:
    model=Contacts
    fields=[
    'text_loc_ru', 
    'text_loc2_ru',
    'tel1',
    'tel2',
    'tel3',
    'email',
    ]