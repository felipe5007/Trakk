from django.shortcuts import render
from django.template import Template, Context

# Create your views here.
def home(request):
    return render(request, "appTrakk/home.html")

def usuarios(request):
    return render(request, "appTrakk/usuarios.html")


def hallazgo(request):
    return render(request, "appTrakk/hallazgo.html")


def feedback(request):
    return render(request, "appTrakk/feedback.html")

def usuariosform(request):
    return render(request, "appTrakk/usuariosform")

def aghallazgo(request):
    return render(request, "appTrakk/aghallazgo")

def bhallazgo(request):
    return render(request, "appTrakk/bhallazgo")