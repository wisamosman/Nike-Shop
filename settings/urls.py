from django.urls import path
from .views import CompanyList

app_name = 'settings'

urlpatterns = [
    path('',CompanyList.as_view(),name='settings_list'),
    
]