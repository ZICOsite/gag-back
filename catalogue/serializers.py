from catalogue.models import Main_Directions, Category, Product_card, Product_detailpage, Characteristics, Product_images, Comp_logo
from rest_framework import serializers


class Category_Serializer(serializers.ModelSerializer):
    child_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'title_en', 'child_count']

    def get_child_count(self, obj):
        return obj.product_card.count()


class Category_Serializer_ru(serializers.ModelSerializer):
    child_count = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'title_ru', 'child_count']

    def get_child_count(self, obj):
        return obj.product_card.count()


class Main_Directions_Serializer(serializers.ModelSerializer):
    category = Category_Serializer(many=True)

    class Meta:
        model = Main_Directions
        fields = [
            'id',
            'title_en',
            'image',
            'category',
            # 'child_count',
        ]


class Main_Directions_Serializer_ru(serializers.ModelSerializer):
    category = Category_Serializer_ru(many=True)

    class Meta:
        model = Main_Directions
        fields = ['id', 'title_ru', 'image', 'category']


class Main_Directions_Serializer_logo(serializers.ModelSerializer):
    carousel_images = serializers.SlugRelatedField(many=True,
                                                   read_only=True,
                                                   slug_field='image_url',
                                                   source='company_logo')

    class Meta:
        model = Main_Directions
        fields = [
            'id',
            'title_en',
            'carousel_images'
        ]


class Main_Directions_Serializer_ru_logo(serializers.ModelSerializer):
    carousel_images = serializers.SlugRelatedField(many=True,
                                                   read_only=True,
                                                   slug_field='image_url',
                                                   source='company_logo')

    class Meta:
        model = Main_Directions
        fields = [
            'id',
            'title_ru',
            'carousel_images'
        ]


class Company_logo_Serializer(serializers.ModelSerializer):
    company_logo = Main_Directions_Serializer_logo()

    class Meta:
        model = Comp_logo
        fields = ['image', 'company_logo']


class Company_logo_Serializer_ru(serializers.ModelSerializer):
    company_logo = Main_Directions_Serializer_ru_logo()

    class Meta:
        model = Comp_logo
        fields = ['image', 'company_logo']


class Product_images_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product_images
        fields = [
            'image',
        ]


class Product_card_Serializer_ru(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    product_detailpage = serializers.PrimaryKeyRelatedField(many=True,
                                                            read_only=True)

    class Meta:
        model = Product_card
        fields = [
            'id', 'title_ru', 'producer_ru', 'model_ru', 'diameter_ru',
            'pressure_ru', 'image', 'product_detailpage'
        ]

    def get_image(self, obj):
        image = Product_images.objects.first()
        return Product_images_Serializer(image).data.get('image')


class Product_card_Serializer(serializers.ModelSerializer):
    product_detailpage = serializers.PrimaryKeyRelatedField(many=True,
                                                            read_only=True)
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product_card
        fields = [
            'id', 'title_en', 'producer_en', 'model_en', 'diameter_en',
            'pressure_en', 'image', 'product_detailpage'
        ]

    def get_image(self, obj):
        image = Product_images.objects.first()
        return Product_images_Serializer(image).data.get('image')


class Characteristics_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristics
        fields = ['title_en', 'value_en']


class Characteristics_ru_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Characteristics
        fields = ['title_ru', 'value_ru']


class Product_detailpage_Serializer(serializers.ModelSerializer):
    desc = Characteristics_Serializer(source='characteristics', many=True)
    # value_en= serializers.SlugRelatedField(many=True,read_only=True,slug_field='value_en', allow_null=True,                                       source='characteristics')
    title_en = serializers.SlugRelatedField(read_only=True,
                                            slug_field='title_en',
                                            source='product_detailpage')
    carousel_images = serializers.SlugRelatedField(many=True,
                                                   read_only=True,
                                                   slug_field='image_url',
                                                   source='product_images')

    class Meta:
        model = Product_detailpage
        fields = [
            'id', 'image', 'title_en', 'text_en', 'desc', 'carousel_images'
        ]


class Product_detailpage_ru_Serializer(serializers.ModelSerializer):
    # value_ru = serializers.SlugRelatedField(many=True,read_only=True,slug_field='value_ru', allow_null=True,                                       source='characteristics')
    title_ru = serializers.SlugRelatedField(read_only=True,
                                            slug_field='title_ru',
                                            source='product_detailpage',
                                            allow_null=True)
    desc = Characteristics_ru_Serializer(source='characteristics', many=True)
    carousel_images = serializers.SlugRelatedField(many=True,
                                                   read_only=True,
                                                   slug_field='image_url',
                                                   source='product_images')

    class Meta:
        model = Product_detailpage
        fields = [
            'id', 'title_ru', 'image', 'text_ru', 'desc', 'carousel_images'
        ]
