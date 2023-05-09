from django.db import models

class Jobs(models.Model):
  icon = models.FileField(upload_to='jobs/icon/')
  occupation_name_ru=models.CharField(max_length=255)
  occupation_name_en=models.CharField(max_length=255)
  def __str__(self):
    return f'{self.occupation_name_en}'
  class Meta:
    ordering = ['id']
class Jobs_title(models.Model):
  title_en=models.CharField(max_length=255)
  title_ru=models.CharField(max_length=255)
  jobs_title = models.ForeignKey(Jobs, on_delete=models.PROTECT ,related_name='jobs_title')
class Jobs_title_des(models.Model):
  text_en=models.CharField(max_length=255)
  text_ru=models.CharField(max_length=255)
  jobs_title_des = models.ForeignKey(Jobs_title, on_delete=models.PROTECT ,related_name='jobs_title_des')
  