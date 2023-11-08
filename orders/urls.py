from django.urls import path
from .views import add_to_cart, OrderList,chackout_page
from .models import Order,OrderDetail,Cart,CartDetail,Coupon


app_name = "orders"

urlpatterns = [
    path('' , OrderList.as_view()),
    path('add-to-cart' , add_to_cart ,name='add_to_cart'),
    path('checkout' , chackout_page),
    
]