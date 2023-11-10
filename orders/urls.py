from django.urls import path
from .views import add_to_cart, OrderList,chackout_page,OrderDetail,confirmation
from .models import Order,OrderDetail,CartDetail,Cart,Coupon


app_name = "orders"

urlpatterns = [
    path('' , OrderList.as_view()),
    path('confirmation' , confirmation),
    path('add-to-cart' , add_to_cart ,name='add_to_cart'),
    path('checkout' , chackout_page),
    
]