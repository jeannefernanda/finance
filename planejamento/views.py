from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render

from perfil.models import Categoria
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.
def definir_planejamento(request):
    categorias = Categoria.objects.all()
    return render(request, 'definir_planejamento.html', {'categorias': categorias})

@csrf_exempt
def update_valor_categoria(request,id):
    novo_valor = json.load(request)['novo_valor']
    categoria = Categoria.objects.get(id=id)
    categoria.valor_planejamento = novo_valor
    categoria.save()

    return JsonResponse({'status': 'success'})

def ver_planejamento(request):
    categorias = Categoria.objects.all()
    # TO DO: Realizar barra com total
    return render(request, 'ver_planejamento.html', {'categorias': categorias})