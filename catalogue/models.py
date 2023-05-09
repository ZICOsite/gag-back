from django.db import models


class Main_Directions(models.Model):
  title_ru = models.CharField(max_length=255)
  title_en = models.CharField(max_length=255)
  image = models.ImageField(upload_to='catalogue/direction_images/')
  def __str__(self):
    return f'{self.title_en}'
  class Meta:
    ordering = ['id']
class Comp_logo(models.Model):
  image = models.ImageField(upload_to='catalogue/company_logo/')
  company_logo=models.ForeignKey(Main_Directions, on_delete=models.PROTECT ,related_name='company_logo')
  @property
  def image_url(self):
      return "{0}".format(self.image.url)
  class Meta:
    ordering = ['id']   
  
  
class Category(models.Model):
  title_ru = models.CharField(max_length=255)
  title_en = models.CharField(max_length=255)  
  category=models.ForeignKey(Main_Directions, on_delete=models.PROTECT ,related_name='category')
  def __str__(self):
    return f'{self.title_en}'
  class Meta:
    ordering = ['id']

class Product_card(models.Model):  
  title_ru = models.CharField(max_length=255)
  title_en = models.CharField(max_length=255)
  producer_ru=models.CharField(max_length=255)
  producer_en=models.CharField(max_length=255)
  model_en=models.CharField(max_length=255)
  model_ru=models.CharField(max_length=255)
  diameter_en=models.CharField(max_length=255)
  diameter_ru=models.CharField(max_length=255)
  pressure_ru=models.CharField(max_length=255)
  pressure_en=models.CharField(max_length=255)
  product_card=models.ForeignKey(Category, on_delete=models.PROTECT ,related_name='product_card')
  def __str__(self):
    return f'{self.title_en}'
  @property
  def first_url(self):
      return self.product_detailpage.product_images.first()
  class Meta:
    ordering = ['id']

class Product_detailpage(models.Model):  
  image = models.ImageField(upload_to='catalogue/product_logo/')

  text_en=models.TextField()
  text_ru=models.TextField()
  product_detailpage=models.ForeignKey(Product_card, on_delete=models.PROTECT ,related_name='product_detailpage')
  def __str__(self):
    return f'{self.product_detailpage}'
  class Meta:
    ordering = ['id']
class Characteristics(models.Model):
    title_ru = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    value_ru = models.CharField(max_length=255)
    value_en = models.CharField(max_length=255)
    characteristics=models.ForeignKey(Product_detailpage, on_delete=models.PROTECT ,related_name='characteristics')
    def __str__(self):
      return f'{self.title_en}'
    class Meta:
      ordering = ['id']
class Product_images(models.Model):
  image = models.ImageField(upload_to='catalogue/product_images/')
  product_images=models.ForeignKey(Product_detailpage, on_delete=models.PROTECT ,related_name='product_images')
  @property
  def image_url(self):
      return "{0}".format(self.image.url)
  class Meta:
    ordering = ['id']    

