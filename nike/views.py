from django.shortcuts import render
from django.views import generic
from .models import Nike , Review




# Create your views here.

class NikeList(generic.ListView):
    model = Nike