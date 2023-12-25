from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistroUsuarioForm(UserCreationForm):
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}


class UserEditForm(UserCreationForm):
    first_name = forms.CharField(label="Editar nombre")
    last_name = forms.CharField(label="Editar apellido")
    email = forms.EmailField(label="Editar e-mail")
    password1 = forms.CharField(label="Nueva contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password1", "password2"]
        help_texts = {k: "" for k in fields}


class UsuarioRegistradoForm(forms.Form):
    nombreDeUsuario = forms.CharField(max_length=20)
    contrasena = forms.CharField(max_length=50)
    email = forms.EmailField()


class BlogCreadoForm(forms.Form):
    tituloDelBlog = forms.CharField(max_length=50, label="Título")
    subtituloDelBlog = forms.CharField(max_length=100, label="Sub-título")
    cuerpoDelBlog = forms.CharField(widget=forms.Textarea, label="Cuerpo")
    autorDelBlog = forms.CharField(max_length=50, label="Autor")
    fechaDelBlog = forms.DateField(label="Fecha")


class AvatarForm(forms.Form):
    imagen = forms.ImageField(label="Seleccione una imágen desde su dispositivo")
