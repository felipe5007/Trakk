from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home.html"),
    path('usuarios/', usuarios, name="usuarios"),
    #
    path('feedback/', feedback, name="feedback"),
    #
    path('hallazgo/', hallazgo, name="hallazgo"),
    path('buscador/', buscador, name="buscador")
]
