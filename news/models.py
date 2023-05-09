from django.db import models

class News(models.Model):
  title_ru = models.CharField(max_length=255)
  title_en = models.CharField(max_length=255)
  post_time=models.DateField()
  image = models.ImageField(upload_to='news_images/main_images/')
  def __str__(self):
    return f'{self.title_en}'
  class Meta:
    ordering = ['id']
    
class Detail_page(models.Model):
  title_ru = models.CharField(max_length=255)
  title_en = models.CharField(max_length=255)
  reading_time_ru=models.CharField(max_length=255)
  reading_time_en=models.CharField(max_length=255)
  image = models.ImageField(upload_to='news_images/background_images/')
  text_en=models.TextField()
  text_ru=models.TextField()
  publication_author_en=models.CharField(max_length=50)
  publication_author_ru=models.CharField(max_length=50)
  detailpage = models.ForeignKey(News, on_delete=models.PROTECT ,related_name='detailpage')
  def __str__(self):
    return f'{self.title_en}'
  class Meta:
    ordering = ['id']