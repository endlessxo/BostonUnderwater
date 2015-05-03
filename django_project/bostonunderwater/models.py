from django.db import models
from django.utils.encoding import smart_unicode
#import datetime
from datetime import datetime

class Totem(models.Model):
    place = models.CharField(max_length=120, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    tier = models.IntegerField(max_length=1, null=True, blank=True)
    def __unicode__(self):
            return smart_unicode(self.place)

class Node(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    #http://david.feinzeig.com/blog/2011/12/06/how-to-properly-set-a-default-value-for-a-datetimefield-in-django/
    time = models.DateTimeField('date created', default=datetime.now)
    water_level = models.IntegerField(max_length=1, null=True, blank=True)
    node_number = models.IntegerField(max_length=40, null=True, blank=True)
    def __unicode__(self):
        return smart_unicode(self.node_number)

class Contact(models.Model):
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField()
    message = models.CharField(max_length=1000, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __unicode__(self):
        return smart_unicode(self.email)

class Beacon(models.Model):
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    time = models.DateTimeField('date created', default=datetime.now)
    water_level = models.IntegerField(max_length=1, null=True, blank=True)
    node_number = models.CharField(max_length=40, null=True, blank=True)
    def __unicode__(self):
        return smart_unicode(self.node_number)


