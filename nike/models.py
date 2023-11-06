from collections.abc import Iterable
from django.db import models
from taggit.managers import TaggableManager
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator,MinValueValidator
from django.utils.text import slugify
from django.db.models.aggregates import Avg , Sum,Count
# Create your models here.


class Nike(models.Model):
    name = models.CharField(max_length=10)
    subtitle = models.TextField(max_length=30)
    price = models.FloatField()
    image = models.ImageField(upload_to='nike')
    slug = models.SlugField(null=True,blank=True)
    tags = TaggableManager()

    def __str__(self):
        return self.name
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)    
        super(Nike, self).save(*args, **kwargs) 

   
    def get_avg_rate(self):
        avg = self.nike_review.aggregate(avg=Avg('rate'))
        return avg
    
class Review(models.Model):
    user = models.ForeignKey(User,related_name='user_review',on_delete=models.SET_NULL,null=True,blank=True)
    nike = models.ForeignKey(Nike,related_name='nike_review',on_delete=models.SET_NULL,null=True,blank=True)
    review = models.TextField(max_length=30)
    rate = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)])
    create_data = models.DateTimeField(default=timezone.now)
    comment = models.TextField(max_length=50)

    def __str__(self):
        return f"{self.user}"

