from django.urls import path
from .views import NikeList, NikeDetail

app_name = 'nike'

urlpatterns = [
    path('',NikeList.as_view(),name='nike_list'),
    path('<int:pk>',NikeDetail.as_view(),name='nike_detail'),
]