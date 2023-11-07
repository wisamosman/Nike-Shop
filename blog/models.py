from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=10)
    subtitle = models.TextField(max_length=30)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='blog')
    user = models.ForeignKey(User,related_name='user_blog',on_delete=models.SET_NULL,null=True,blank=True)
    tags = TaggableManager()
    create_data = models.DateTimeField(default=timezone.now)
    comment = models.TextField(max_length=50)
    
    def __str__(self):
        return self.name
    