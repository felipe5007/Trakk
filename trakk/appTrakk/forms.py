from django import forms

class HallazgoForm(forms.Form):
    Nombre = forms.CharField(max_length=50)
    descripcion = forms.CharField(max_length=250)
    correo = forms.CharField(max_length=50)
    

class UsuarioForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(max_length=225)
    

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=50)
    comentario = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=50)
