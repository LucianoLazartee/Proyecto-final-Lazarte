from django.shortcuts import render
from appmessages.models import *
from appmessages.forms import *
from django.contrib.auth.models import User
from accounts.views import obtenerAvatar
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


@login_required
def inicioMensajeria(request):
    return render(request, "inicioMensajeria.html", {"avatar": obtenerAvatar(request)})


@login_required
def enviarMensaje(request):
    if request.method == "POST":
        form = EnviarMensajeForm(request.POST)
        if form.is_valid():
            info = form.cleaned_data
            mensaje = Mensaje(emisor=info["emisor"], receptor=info["receptor"],
                            cuerpoDelMensaje=info["cuerpoDelMensaje"])
            mensaje.save()
            return render(request, "inicioMensajeria.html", {
                "mensaje": f"El mensaje para {mensaje.receptor} ha sido enviado correctamente", "avatar": obtenerAvatar(request)})
        else:
            return render(request, "enviarMensaje.html", {
                "form": form, "mensaje": "Los datos ingresados no son validos, intente nuevamente", "avatar": obtenerAvatar(request)})
    else:
        form = EnviarMensajeForm(request.POST)
    mensajes = Mensaje.objects.all()    
    context = {"mensajes": mensajes, "form": form, "avatar": obtenerAvatar(request)}
    return render(request, "enviarMensaje.html", context)


@login_required
def verMensajes(request):
    usuario = request.user
    emailreceptor = Mensaje.objects.filter(receptor__icontains=usuario.email)
    print(emailreceptor)
    return render(request, "bandejaDeEntrada.html", {
        "emailreceptor": emailreceptor, "avatar": obtenerAvatar(request)})
