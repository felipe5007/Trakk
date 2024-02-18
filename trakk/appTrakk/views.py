from django.shortcuts import render
from django.template import Template, Context

# Create your views here.
def home(request):
    return render(request, "appTrakk/home.html")

# Usuarios
def usuarios(request):
    return render(request, "appTrakk/usuarios.html")
def agregar_usuario(request):
    return render(request, "appTrakk/agregar_usuario.html")

def buscar_usuario(request):
    return render(request, "appTrakk/buscar_usuario.html")

#Hallazgos
def hallazgo(request):
    return render(request, "appTrakk/hallazgo.html")
def agregar_hallazgo(request):
    return render(request, "appTrakk/agregar_hallazgo.html")

def buscar_hallazgo(request):
    return render(request, "appTrakk/buscar_hallazgo.html")

#Feedbacks
def feedback(request):
    return render(request, "appTrakk/feedback.html")

def agregar_feedback(request):
    return render(request, "appTrakk/agregar_feedback.html")

def buscar_feedback(request):
    return render(request, "appTrakk/buscar_feedback.html")