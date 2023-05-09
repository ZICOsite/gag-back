from news.models import News, Detail_page
from rest_framework import serializers

class News_Serializer(serializers.ModelSerializer):
  detailpage = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  class Meta:
    model=News
    fields=[
      'id',
      'title_en',
      'post_time',
      'image',
      'detailpage'
      
    ]
class News_Serializer_ru(serializers.ModelSerializer):
  detailpage=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  class Meta:
    model=News
    fields=[
      'id',
      'title_ru',
      'post_time',
      'image',
      'detailpage'
    ]
      
    
class Detail_page_Serializer(serializers.ModelSerializer):
  post_time = serializers.DateField(source='detailpage.post_time')
  class Meta:
    model=Detail_page
    fields=[
      'id',
      'title_en',
      'post_time',
      'image',
      'reading_time_en',
      'text_en',
      'publication_author_en',
      
  ]
    
class Detail_page_Serializer_ru(serializers.ModelSerializer):
  post_time = serializers.DateField(source='detailpage.post_time')
  class Meta:
    model=Detail_page
    fields=[
      'id',
      'title_ru',
      'post_time',
      'image',
      'reading_time_ru', 
      'text_ru',
      'publication_author_ru',
  ]
  