#coding:utf-8 

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User 



class Subscription(models.Model):
   name = models.CharField(_('nome'),max_length=100)
   username = models.CharField(_('login'),max_length=100)
   password = models.CharField(_('senha'), max_length=20)

   
   
   

   def __unicode__(self):
        return (self.name) 

   