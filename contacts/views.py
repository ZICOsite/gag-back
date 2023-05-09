from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from contacts.models import Contacts
from contacts.serializers import Contacts_Serializer,Contacts_ru_Serializer


class Contacts_ViewSet(viewsets.ModelViewSet):
    queryset = Contacts.objects.all()
    serializer_class = Contacts_Serializer

    
    def get_serializer(self, *args, **kwargs):
      if self.request.query_params.get('lang') == 'en':
          return Contacts_Serializer(*args, **kwargs)
      elif self.request.query_params.get('lang') == 'ru':
          return Contacts_ru_Serializer(*args, **kwargs)
      else:
          return super().get_serializer(*args, **kwargs)

