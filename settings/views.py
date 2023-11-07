from django.shortcuts import render
from django.views import generic
from .models import Company
from nike.models import Nike, Review




def home(request):
    nikes = Nike.objects.all()[:8]
    reviews = Review.objects.all()
    return render(request,'settings/home.html',{
        'nikes':nikes,
        'reviews':reviews,
    })

# Create your views here.

class CompanyList(generic.ListView):
    model = Company
# Create your views here.
