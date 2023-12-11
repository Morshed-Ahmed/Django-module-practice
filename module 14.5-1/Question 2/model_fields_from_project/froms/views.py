from django.shortcuts import render
from froms.forms import JobPostForm

def home(request):
    postForm = JobPostForm()
    return render(request,'home.html',{'form': postForm})
