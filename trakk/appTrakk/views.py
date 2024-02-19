from django.shortcuts import render
from django.template import Template, Context
from .forms import *

# Create your views here.
def home(request):
    return render(request, "appTrakk/home.html")

# Usuarios
def usuarios(request):
    UsuarioForm = UsuarioForm()
    return render(request, "appTrakk/usuarios.html", {"form": UsuarioForm})
def agregar_usuario(request):
    return render(request, "appTrakk/agregar_usuario.html")

def buscar_usuario(request):
    return render(request, "appTrakk/buscar_usuario.html")

#Hallazgos
def hallazgo(request):
    return render(request, "appTrakk/hallazgo.html")
def agregar_hallazgo(request):
    HallazgoForm = HallazgoForm()
    return render(request, "appTrakk/agregar_hallazgo.html", {"form": HallazgoForm})

def buscar_hallazgo(request):
    return render(request, "appTrakk/buscar_hallazgo.html")

#Feedbacks
def feedback(request):
    return render(request, "appTrakk/feedback.html")

def agregar_feedback(request):
    FeedbackForm = FeedbackForm()
    return render(request, "appTrakk/agregar_feedback.html",{"form": FeedbackForm})

def buscar_feedback(request):
    return render(request, "appTrakk/buscar_feedback.html")