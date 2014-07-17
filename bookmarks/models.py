from django.db import models

# Create your models here.

class Tags(models.Model):
  name = models.CharField(max_length=20)
   
  def __unicode__(self):
    return self.name

class Link(models.Model):
  url = models.URLField()
  tags = models.ManyToManyField(Tags)
  
  def __unicode__(self):
    return self.url
    

