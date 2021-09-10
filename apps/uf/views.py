from django.shortcuts import render
from django.http import HttpResponse
from .models import *

def index(request):
    context_home={
        'home':Home.objects.last(),
    }
    return render(request, 'index.html', context_home)

def sobre(request):
    context_sobre={
        'sobre':Sobre.objects.last(),
    }
    return render(request, 'sobre.html', context_sobre)

def servicos(request):
    context_servico={
        'servico':Servico.objects.last(),
        'depoimentos':Depoimentos.objects.all(),
    }
    return render(request, 'servicos.html', context_servico)

def upload(request):
    return render(request, 'upload.html')

def assist(request):
    context_assist={
        'assist':Assist.objects.last(),
    }
    return render(request, 'assist.html', context_assist)

def explorar(request):
    return render(request, 'explorar.html')

def contato(request):
    context_contato={
        'contato':Contato.objects.last(),
    }
    return render(request, 'contato.html', context_contato)

def notfound(request):
    return render(request, 'notfound.html')

