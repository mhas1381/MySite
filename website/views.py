from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return HttpResponse("Home page")

def about_view(request):
    return HttpResponse("About")

def contact_view(request):
    return HttpResponse("Contact")
