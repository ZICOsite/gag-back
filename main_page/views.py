from django.shortcuts import render
from rest_framework.response import Response
from main_page.models import Main_page
from rest_framework import viewsets, status
from main_page.serializers import Main_Page_Serializer_ru,Main_Page_Serializer
from main_page.pagination import Main_page_pagination

class Main_page_ViewSet(viewsets.ModelViewSet):
    queryset = Main_page.objects.all()
    serializer_class = Main_Page_Serializer
    pagination_class=Main_page_pagination
    def get_serializer(self, *args, **kwargs):
      if self.request.query_params.get('lang') == 'en':
          return Main_Page_Serializer(*args, **kwargs)
      elif self.request.query_params.get('lang') == 'ru':
          return Main_Page_Serializer_ru(*args, **kwargs)
      else:
          return super().get_serializer(*args, **kwargs)

# Create your views here.
