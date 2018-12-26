#this is a view creation
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world this is my first app which is cool ")


# Create your views here.
