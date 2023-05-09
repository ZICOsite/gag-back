from django.shortcuts import render
from rest_framework.response import Response
from vacancies.models import Jobs
from rest_framework import viewsets, status
from vacancies.serializers import Jobs_Serializer_ru,Jobs_Serializer_en

class Jobs_ViewSet(viewsets.ModelViewSet):
    queryset = Jobs.objects.all()
    serializer_class = Jobs_Serializer_en
    def get_serializer(self, *args, **kwargs):
      if self.request.query_params.get('lang') == 'en':
          return Jobs_Serializer_en(*args, **kwargs)
      elif self.request.query_params.get('lang') == 'ru':
          return Jobs_Serializer_ru(*args, **kwargs)
      else:
          return super().get_serializer(*args, **kwargs)
         
          

