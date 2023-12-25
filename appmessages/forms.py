from django import forms


class EnviarMensajeForm(forms.Form):
    emisor = forms.EmailField(label="Emisor (e-mail)")
    receptor = forms.EmailField(label="Receptor (e-mail)")
    cuerpoDelMensaje = forms.CharField(max_length=250, label="Cuerpo")
