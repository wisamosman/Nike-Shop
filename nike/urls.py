from django.urls import path
from .views import NikeList

app_name = 'nike'

urlpatterns = [
    path('',NikeList.as_view(),name='nike_list'),
]