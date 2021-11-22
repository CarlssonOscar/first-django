from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# A view-function takes a request and returns a respons
# Request handler

def say_hello(request):
    # pull data from db
    # Transform data
    # send email
    return HttpResponse('Hello World!')