from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import ListView
from .models import Order, Cart , CartDetail, Coupon
from nike.models import Nike
from django.contrib.auth.mixins import LoginRequiredMixin
import datetime
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views import generic



class OrderList(LoginRequiredMixin,ListView):
    model = Order

    def get_queryset(self):
        order_detail =  order_detail.objects.all()
        queryset = OrderDetail.objects.all()
        return queryset
    

    def get_queryset(self):
        queryset = super().get_queryset()   # all orders 
        queryset = queryset.filter(user=self.request.user)
        return queryset

class OrderDetail(generic.DetailView):
    model = Order

def chackout_page(request):
    cart = Cart.objects.get(user=request.user , completed=False)
    cart_detail = CartDetail.objects.filter(cart=cart)
    
    if request.method == 'POST':
        code = request.POST['coupon']
        coupon = Coupon.objects.get(code=code)
        if coupon and coupon.quantity > 0:
            today_date = datetime.datetime.today().date()
            if today_date >= coupon.start_date and today_date <= coupon.end_date:
                code_value = cart.cart_total() / 100*coupon.percentage
                sub_total = cart.cart_total() -  code_value
                total = sub_total 
                cart.coupon = coupon 
                cart.total_with_coupon = sub_total
                cart.save()
                html = render_to_string('include/checkout_table.html',{
                'cart_detail':cart_detail , 
                 
                'sub_total': round(sub_total,2) , 
                'total': round(total,2) , 
                'discount': round(code_value,2) , 
                request:request
                })
                return JsonResponse({'result':html})

    sub_total = cart.cart_total()
    
    discount = 0
    total = sub_total 

    return render(request,'orders/checkout.html',{
        'cart_detail':cart_detail , 
     
        'sub_total': sub_total , 
        'total': total , 
        'discount': discount
        })



def add_to_cart(request):

    # get data frontend 
    nike = Nike.objects.get(id=request.POST['nike_id'])
    qauntity = request.POST['quantity']

    # get cart
    cart = Cart.objects.get(user=request.user,completed=False)

    # cart detail 
    cart_detail  , created = CartDetail.objects.get_or_create(cart=cart , nike=nike)
    cart_detail.quantity = qauntity
    cart_detail.price = nike.price
    cart_detail.total = round(int(qauntity) * nike.price,2)
    cart_detail.save()

    return redirect(f'/nike/{nike.slug}')

    #cart = Cart.objects.get(user=request.user,completed=False)
    #detail = CartDetail.objects.filter(cart=cart)

    #total = f"{cart.cart_total()}$"

    #html = render_to_string('include/base_sidebar.html',{'cart_data':cart, 'cart_detail_data':detail, request:request})
    #return JsonResponse({'result':html ,'total':total})
    # # cart detail 
    # cart_detail  , created = CartDetail.objects.get_or_create(cart=cart , product=product)
    # if created : 
    #     cart_detail.quantity = qauntity
    # else:
    #     cart_detail.quantity += qauntity

    # cart_detail.price = product.price
    # cart_detail.total = int(qauntity) * product.price
    # cart_detail.save()



def confirmation(request):
    cart = Cart.objects.all()
    cart_detail = CartDetail.objects.all()
    

    return render(request, 'orders/order-detail.html',{
        'cart':Cart,
        'cart_detail':CartDetail

    })