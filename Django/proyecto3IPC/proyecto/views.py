from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def pagina_web(request):
    return HttpResponse("¡Hola, esta es tu página web ejecutándose en Django!")

def inicio(request):
    return render(request, 'proyecto/inicio.html')