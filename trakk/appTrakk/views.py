from django.shortcuts import render
from django.template import Template, Context

# Create your views here.
def home(request):
    return render(request, "appTrakk/home.html")