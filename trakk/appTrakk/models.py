from django.db import models
from django import forms


class Usuario(models.Model):
    name = models.CharField(max_length=30, unique=False)
    email = models.EmailField(unique=True)
    ultimo_login = models.DateTimeField(auto_now=True)
    esta_activa = models.BooleanField(default=True)
    password = models.CharField(max_length=255)
    check_password = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"
    
class Hallazgo(models.Model):
    name = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    Estado = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"
    
class Feedback(models.Model):
    name = models.CharField(max_length=150)
    comentario = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return f"{self.name}"
