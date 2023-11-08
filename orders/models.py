from django.db import models
from django.utils import timezone
from accounts.models import Address , Profile , Phones
from nike.models import Nike
from django.contrib.auth.models import User
from utils.generate_code import generate_code

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User,related_name='order_user',on_delete=models.SET_NULL,blank=True,null=True)
    profile = models.ForeignKey(Profile,related_name='delivery_profile',on_delete=models.SET_NULL,null=True,blank=True)
    phones = models.ForeignKey(Phones,related_name='delivery_phones',on_delete=models.SET_NULL,null=True,blank=True)
    delivery_location = models.ForeignKey(Address,related_name='delivery_address',on_delete=models.SET_NULL,null=True,blank=True)
    code = models.CharField(max_length=30,default=generate_code)
    order_time = models.DateTimeField(default=timezone.now)
    coupon = models.ForeignKey('Coupon',related_name='order_coupon',on_delete=models.SET_NULL , null=True,blank=True)
    total_with_coupon = models.FloatField(null=True,blank=True)

    def __str__(self):
        return self.code




class OrderDetail(models.Model):
    order = models.ForeignKey(Order,related_name='order_detail',on_delete=models.CASCADE)
    nike = models.ForeignKey(Nike , related_name='order_nike',on_delete=models.SET_NULL,null=True)
    price = models.FloatField
    quantity = models.IntegerField()
    total = models.FloatField()

    def __str__(self):
        return str(self.order)


class Cart(models.Model):
    user = models.ForeignKey(User,related_name='cart_user',on_delete=models.SET_NULL,blank=True,null=True)
    completed = models.BooleanField(default=False)
    coupon = models.ForeignKey('Coupon',related_name='cart_coupon',on_delete=models.SET_NULL , null=True,blank=True)
    total_with_coupon = models.FloatField(null=True,blank=True)

     # instance method
    def cart_total(self):
        total = 0
        for nike in self.cart_detail.all():
            total += nike.total
        return round(total,2)



class CartDetail(models.Model):
    cart = models.ForeignKey(Cart , related_name='cart_detail',on_delete=models.CASCADE)
    nike = models.ForeignKey(Nike , related_name='cart_nike',on_delete=models.SET_NULL,null=True)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)
    total = models.FloatField(default=0)



class Coupon(models.Model):
    code = models.CharField(max_length=25)
    percentage = models.FloatField()
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now)
    quantity = models.IntegerField()

    def __str__(self):
        return self.code