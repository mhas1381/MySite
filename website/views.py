import re
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from website.models import Contact
from website.forms import NameForm
def index_view(request):
    return render(request , 'website/index.html')

def about_view(request):
    return render(request , "website/about.html")

def contact_view(request):
    return render(request , "website/contact.html")

def test_view(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')
    form = NameForm()
    return render(request ,'test.html' , {'form':form})
