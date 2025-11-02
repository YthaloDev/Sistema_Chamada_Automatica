from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    return render(request, "pagina_web/index.html")


def qrcode(request):
    return render(request, 'pagina_web/qrcode.html')


def chamada(request):
    return render(request, 'pagina_web/chamada.html')


def configuracao(request):
    return render(request, 'pagina_web/configuracao.html')
