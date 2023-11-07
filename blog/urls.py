from django.urls import path
from .views import BlogList,BlogDetail

app_name = 'blog'

urlpatterns = [
    path('',BlogList.as_view(),name='blog_list'),
    path('<slug:slug>',BlogDetail.as_view(),name='blog_detail'),
]
