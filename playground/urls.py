from django.urls import path
from . import views 
# . = current folder

# URLconf, kopplas till projektnamn (fristdjango)/urls.py
urlpatterns = [
    path('playground/hello', views.say_hello)
]