from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name="home.html"),
    path('usuarios/', usuarios, name="usuarios"),
    path('hallazgo/', hallazgo, name="hallazgo"),
    path('feedback/', feedback, name="feedback"),
]
