from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def sobre(request):
    return render(request, 'sobre.html')

def servicos(request):
    return render(request, 'servicos.html')

def assist(request):
    return render(request, 'assist.html')

def explorar(request):
    return render(request, 'explorar.html')

def contato(request):
    return render(request, 'contato.html')

def notfound(request):
    return render(request, 'notfound.html')