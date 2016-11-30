from __future__ import unicode_literals
from django.utils.translation import gettext as _
from django.db import models
from django import forms



class Mosques(models.Model):
    gmap_id = models.CharField(max_length= 50 )
    mosque_name  = models.CharField(max_length = 100)
    long_location  = models.FloatField()
    lat_location   = models.FloatField() 
    def __unicode__(self):
       return  self.mosque_name
class User(models.Model):
    user_name = models.CharField(max_length=45)
    password =  models.CharField(max_length=100)
    def __unicode__(self):
       return  self.user_name


class Timing(models.Model):
	#PRAYERS = (	('Fajar', 'Fajar'),('Dhuhur', 'Dhuhur'), ('Asr', 'Asr'),('Maghrib' , 'Maghrib'),('Isha' , 'Isha'),('Friday' , 'Friday'))
    mosque = models.ForeignKey(Mosques)
    prayer = models.CharField(max_length=10 )
    time = models.TimeField(_(u"Conversation Time"))
    city = models.CharField(max_length=45)
    time_stamp  = models.DateTimeField(auto_now_add=True)
    user    =  models.ForeignKey(User)
    def __unicode__(self):
       return self.prayer +' ' + self.mosque