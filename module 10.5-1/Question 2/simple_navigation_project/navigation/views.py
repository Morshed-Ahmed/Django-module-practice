from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def About(response):
    return render(response,'navigation/About.html')

def Contact(response):
    return render(response,'navigation/Contact.html')