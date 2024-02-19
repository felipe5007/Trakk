from django.shortcuts import render
from django.template import Template, Context
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, "appTrakk/home.html")

# Usuarios
def usuarios(request):
    if request.method == "POST":
        UForm = UsuarioForm(request.post)
        if UForm.is_valid():
            user_name = UForm.cleaned_data.get("name")
            user_email = UForm.cleaned_data.get("email")
            usuario = Usuario(name=user_name, email=user_email)
            usuario.save()
            return render(request, "appTrakk/home.html")
    else:
        UForm = UsuarioForm()
        return render(request, "appTrakk/usuarios.html", {"form": UForm})


#Hallazgos
def hallazgo(request):
    if request.method == "POST":
        HForm = HallazgoForm(request.post)
        if HForm.is_valid():
            hallazgo_name = HForm.cleaned_data.get("name")
            hallazgo_descripcion = HForm.cleaned_data.get("descripcion")
            hallazgo = Hallazgo(name=hallazgo_name, descripcion=hallazgo_descripcion)
            hallazgo.save()
            return render(request, "appTrakk/home.html")
        
    else:
        HForm = HallazgoForm()
    return render(request, "appTrakk/hallazgo.html", {"form": HForm}, )

def buscador(request):
        contextoF = {'hallazgo': Hallazgo.objects.all()}
        return render(request, "appTrakk/buscador.html",contextoF) 

#Feedbacks
def feedback(request):
    if request.method == "POST":
        FForm = FeedbackForm(request.post)
        if FForm.is_valid():
            feedback_name = FForm.cleaned_data.get("name")
            feedback_comentario = FForm.cleaned_data.get("descripcion")
            feedback_email = FForm.cleaned_data.get("email")
            feedback = Feedback(name=feedback_name, descripcion=feedback_comentario, email=feedback_email)
            feedback.save()
            return render(request, "appTrakk/home.html")
        
    else:
        FForm = FeedbackForm()
    return render(request, "appTrakk/feedback.html",{"form": FForm})
