from django.shortcuts import render
from django.views import generic
from .models import Company




# Create your views here.

class CompanyList(generic.ListView):
    model = Company
# Create your views here.
