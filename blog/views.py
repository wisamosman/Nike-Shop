from django.shortcuts import render
from django.views import generic
from .models import Blog
# Create your views here.


class BlogList(generic.ListView):
    model = Blog
    



class BlogDetail(generic.DeleteView):
    model = Blog  