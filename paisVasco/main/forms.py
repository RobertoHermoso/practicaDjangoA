from django import forms

class EventoBuscarFechaForm(forms.Form):
    year = forms.IntegerField(label="Mes de celebración", widget=forms.TextInput, required=True)


class EventoBuscarLenguaForm(forms.Form):
    year = forms.CharField(label="Lengua", widget=forms.TextInput, required=True)