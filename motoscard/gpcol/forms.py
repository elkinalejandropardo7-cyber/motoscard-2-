
from django import forms
from .models import Piloto


class Pilotoform(forms.ModelForm):
    class Meta:
        model = Piloto
        fields = [
            'nombre',
            'apellido',
            'correo',
            'documento',
            'telefono',
            'tipo_de_documento',
            'numero_de_competicion',
            'rh'
        ]
        widgets = {}
