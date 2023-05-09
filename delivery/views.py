from django.shortcuts import render
from rest_framework.response import Response
from delivery.models import Delivery
from rest_framework import viewsets, status
from delivery.serializers import Delivery_Serializer_ru,Delivery_Serializer

class Delivery_ViewSet(viewsets.ModelViewSet):
    queryset = Delivery.objects.all()
    serializer_class = Delivery_Serializer
    def get_serializer(self, *args, **kwargs):
      if self.request.query_params.get('lang') == 'en':
          return Delivery_Serializer(*args, **kwargs)
      elif self.request.query_params.get('lang') == 'ru':
          return Delivery_Serializer_ru(*args, **kwargs)
      else:
          return super().get_serializer(*args, **kwargs)