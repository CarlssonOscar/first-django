from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# A view-function takes a request and returns a respons
# Request handler

def sayhello(request):
    return render(request, 'hello.html', {'name': 'Oscar'})

# pull data from db
# Transform data
# send email