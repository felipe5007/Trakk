from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home.html"),
    path('usuarios/', usuarios, name="usuarios"),
    path('agregar_usuario/', agregar_usuario, name="agregar_usuario"),
    path('buscar_usuario/', buscar_usuario, name="buscar_usuario"),
    #
    path('feedback/', feedback, name="feedback"),
    path('agregar_feedback/', agregar_feedback, name="agregar_feedback"),
    path('buscar_feedback/', buscar_feedback, name="buscar_feedback"),
    #
    path('hallazgo/', hallazgo, name="hallazgo"),
    path('agregar_hallazgo/', agregar_hallazgo, name="agregar_hallazgo"),
    path('buscar_hallazgo/', buscar_hallazgo, name="buscar_hallazgo"),
]
