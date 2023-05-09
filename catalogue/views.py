from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from catalogue.models import *
from catalogue.serializers import Main_Directions_Serializer_ru,Main_Directions_Serializer,Category_Serializer,Category_Serializer_ru,Product_card_Serializer_ru,Product_card_Serializer,Product_detailpage_Serializer,Product_detailpage_ru_Serializer,Characteristics_ru_Serializer,Characteristics_Serializer,Main_Directions_Serializer_logo,Main_Directions_Serializer_ru_logo,Company_logo_Serializer_ru,Company_logo_Serializer_ru
from rest_framework import filters
from rest_framework_word_filter import FullWordSearchFilter

class Main_Directions_ViewSet(viewsets.ModelViewSet):
    queryset = Main_Directions.objects.all()
    serializer_class = Main_Directions_Serializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['username', 'email']
    
    def get_serializer(self, *args, **kwargs):
      if self.request.query_params.get('lang') == 'en':
          return Main_Directions_Serializer(*args, **kwargs)
      elif self.request.query_params.get('lang') == 'ru':
          return Main_Directions_Serializer_ru(*args, **kwargs)
      else:
          return super().get_serializer(*args, **kwargs)

    
class Category_ViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Category_Serializer
    def get_serializer(self, *args, **kwargs):
      if self.request.query_params.get('lang') == 'en':
          return Category_Serializer(*args, **kwargs)
      elif self.request.query_params.get('lang') == 'ru':
          return Category_Serializer_ru(*args, **kwargs)
      else:
          return super().get_serializer(*args, **kwargs)



class Product_card_ViewSet(viewsets.ModelViewSet):
    queryset = Product_card.objects.all()
    serializer_class = Product_card_Serializer
    # filter_backends = (FullWordSearchFilter, )
    # word_fields = ('title_ru', 'title_en')
    filter_backends = [filters.SearchFilter]
    search_fields = ['title_ru','title_en']
    def list(self, request,*args, **kwargs):
      queryset = self.filter_queryset(self.get_queryset())
      
      if self.request.query_params.get('par_id'):
        x=self.request.query_params.get('par_id')
        queryset = queryset.filter(product_card__category__id=x)
      if self.request.query_params.get('cat_id'):
        y=self.request.query_params.get('cat_id')
        queryset = queryset.filter(product_card_id=y)
      serializer = self.get_serializer(queryset, many=True)
      paginated_queryset = self.paginate_queryset(serializer.data)
      
      return self.get_paginated_response(paginated_queryset)

    
    def get_serializer(self, *args, **kwargs):
      if self.request.query_params.get('lang') == 'en':
          return Product_card_Serializer(*args, **kwargs)
      elif self.request.query_params.get('lang') == 'ru':
          return Product_card_Serializer_ru(*args, **kwargs)
      else:
          return super().get_serializer(*args, **kwargs)

class Product_detailpage_ViewSet(viewsets.ModelViewSet):
    queryset = Product_detailpage.objects.all()
    serializer_class = Product_detailpage_Serializer
    
    def get_serializer(self, *args, **kwargs):
      if self.request.query_params.get('lang') == 'en':
          return Product_detailpage_Serializer(*args, **kwargs)
      elif self.request.query_params.get('lang') == 'ru':
          return Product_detailpage_ru_Serializer(*args, **kwargs)
      else:
          return super().get_serializer(*args, **kwargs)

class Company_logo_ViewSet(viewsets.ModelViewSet):
    queryset = Main_Directions.objects.all()
    serializer_class = Main_Directions_Serializer_logo
    # def list(self, request,*args, **kwargs):
    #   queryset = self.filter_queryset(self.get_queryset())
      
    #   if self.request.query_params.get('par_id'):
    #     x=self.request.query_params.get('par_id')
    #     queryset = queryset.filter(company_logo=x)
    #   serializer = self.get_serializer(queryset, many=True)
    #   paginated_queryset = self.paginate_queryset(serializer.data)
      
    #   return self.get_paginated_response(paginated_queryset)

  
    def get_serializer(self, *args, **kwargs):
      if self.request.query_params.get('lang') == 'en':
          return Main_Directions_Serializer_logo(*args, **kwargs)
      elif self.request.query_params.get('lang') == 'ru':
          return Main_Directions_Serializer_ru_logo(*args, **kwargs)
      else:
          return super().get_serializer(*args, **kwargs)

class Characteristics_ViewSet(viewsets.ModelViewSet):
    queryset = Characteristics.objects.all()
    serializer_class = Characteristics_Serializer
    def get_serializer(self, *args, **kwargs):
      if self.request.query_params.get('lang') == 'en':
          return Characteristics_Serializer(*args, **kwargs)
      elif self.request.query_params.get('lang') == 'ru':
          return Characteristics_ru_Serializer(*args, **kwargs)
      else:
          return super().get_serializer(*args, **kwargs)
