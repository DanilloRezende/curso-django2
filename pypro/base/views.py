from django.http import HttpResponse
from django.shortcuts import render

from pypro.modulos import facade


# Create your views here.
def home(request):
    return render(request, 'base/home.html', {'MODULOS': facade.listar_modulos_ordenados()})
