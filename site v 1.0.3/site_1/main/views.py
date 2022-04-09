from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request,'main/contact.html')
