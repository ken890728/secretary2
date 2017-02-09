from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Message(models.Model):
  user = models.CharField(max_length=50)
  subject = models.CharField(max_length=200)
  publication_date = models.DateTimeField()
  def __unicode__(self):
     return self.subject
  
class Month(models.Model):
  date = models.IntegerField(default=0)
  def __unicode__(self):
    return str(self.date)

class Menu(models.Model):
  food = models.CharField(max_length=20)
  price = models.IntegerField(default=0)
  def __unicode__(self):
    return self.food