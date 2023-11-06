from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=15)
    logo = models.ImageField(upload_to='company')
    subtitle = models.TextField(max_length=30,null=True,blank=True)
    email = models.CharField(max_length=15,null=True,blank=True)
    phones = models.CharField(max_length=15,null=True,blank=True)
    address = models.TextField(max_length=15,null=True,blank=True)
    fb_link = models.URLField(null=True,blank=True)
    android_link = models.URLField(null=True,blank=True)
    appstore_link = models.URLField(null=True,blank=True)
    about_us = models.TextField(max_length=500)


    def __str__(self):
        return self.name