from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def january(request):
    return HttpResponse("Go to university very early ")

def february(request):
    return HttpResponse("Playing video game every day")