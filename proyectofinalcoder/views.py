from django.shortcuts import render
from accounts.views import obtenerAvatar


def inicio(request):
    return render(request, "inicio.html", {"avatar": obtenerAvatar(request)})


def sobreMi(request):
    return render(request, "sobreMi.html", {"avatar": obtenerAvatar(request)})
