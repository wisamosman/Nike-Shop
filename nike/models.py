from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.


class Nike(models.Model):
    name = models.CharField(max_length=10)
    subtitle = models.TextField(max_length=30)
    price = models.FloatField()
    image = models.ImageField(upload_to='nike')
    tags = TaggableManager()

    def __str__(self):
        return self.name


class Review(models.Model):
    user = models.ForeignKey(User,related_name='user_review',on_delete=models.SET_NULL,null=True,blank=True)
    nike = models.ForeignKey(Nike,related_name='nike_review',on_delete=models.SET_NULL,null=True,blank=True)
    review = models.TextField(max_length=30)
    rate = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)])
    create_data = models.DateTimeField(default=timezone.now)
    comment = models.TextField(max_length=50)

    def __str__(self):
        return f"{self.user}"

