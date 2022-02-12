from django.shortcuts import render
from django.http import HttpResponse
from website.models import Contact
from website.forms import NameForm,Contact_form
def index_view(request):
    return render(request , 'website/index.html')

def about_view(request):
    return render(request , "website/about.html")

def contact_view(request):
    return render(request , "website/contact.html")

def test_view(request):
    if request.method == 'POST':
        form = Contact_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')
    form = Contact_form()
    return render(request ,'test.html' , {'form':form})
