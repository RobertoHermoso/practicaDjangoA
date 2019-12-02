from django import forms

class EventoBuscarFechaForm(forms.Form):
    idUsuario = forms.CharField(label="Id de Usuario", widget=forms.TextInput, required=True)


class EventoBuscarLenguaForm(forms.Form):
    year = forms.IntegerField(label="Año de publicación", widget=forms.TextInput, required=True)