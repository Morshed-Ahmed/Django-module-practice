from django.shortcuts import render
from . forms import Register,Contact

# Create your views here.
def home(request):
    registerField = Register()
    return render(request,'register.html',{'form':registerField})


def contact(request):
    registerField = Contact()
    return render(request,'contact.html',{'form':registerField})