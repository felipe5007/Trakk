from django.http import HttpResponse
from django.template import Template, Context
def test(request):
    return HttpResponse("Probando esto, bienvenido")

