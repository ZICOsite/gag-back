from django.db import models


class Main_page(models.Model):
  title_ru = models.CharField(max_length=255)
  title_en = models.CharField(max_length=255)
  image = models.ImageField(upload_to='main_page/banner_image/')
  text_en=models.TextField()
  text_ru=models.TextField()
  def __str__(self):
    return f'{self.title_en}'
  class Meta:
    ordering = ['id']

class Document(models.Model):
  file=models.FileField(upload_to='main_page/catalogue_doc/')
  document=models.ForeignKey(Main_page, on_delete=models.PROTECT ,related_name='document')
  @property
  def document_url(self):
      return "{0}".format(self.file.url)
  class Meta:
    ordering = ['id']    