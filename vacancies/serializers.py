from vacancies.models import Jobs, Jobs_title
from rest_framework import serializers




class Jobs_title_Serializer_ru(serializers.ModelSerializer):
    list=serializers.SlugRelatedField(many=True,read_only=True,slug_field='text_ru', allow_null=True,                                       source='jobs_title_des')
    class Meta:
        model = Jobs_title
        fields = [
          'title_ru',
          'list',
        ]


class Jobs_Serializer_ru(serializers.ModelSerializer):
    desc = Jobs_title_Serializer_ru(source='jobs_title', many=True)
  
    class Meta:
        model = Jobs
        fields = [
            'id',
            'icon',
            'occupation_name_ru',
            'desc',
        ]

class Jobs_title_Serializer_en(serializers.ModelSerializer):
    list=serializers.SlugRelatedField(many=True,read_only=True,slug_field='text_en', allow_null=True,                                       source='jobs_title_des')
    class Meta:
        model = Jobs_title
        fields = [
          'title_en',
          'list',
        ]


class Jobs_Serializer_en(serializers.ModelSerializer):
    desc = Jobs_title_Serializer_en(source='jobs_title', many=True)
  
    class Meta:
        model = Jobs
        fields = [
            'id',
            'icon',
            'occupation_name_en',
            'desc',
        ]