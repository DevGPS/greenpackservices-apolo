from django import forms
from django.forms import ModelForm

from core.contenedor.models import *

class ExportadoraForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo'].widget.attrs['autofocus'] = True
    class Meta:
        model = Exportadora
        fields = ['codigo','nombre', 'direccion', 'telefono', 'email']
        
        widgets = {
            'codigo': forms.TextInput(attrs={"class": "form-control","name": "codigo","type": "text"}),
            'nombre': forms.TextInput(attrs={"class": "form-control","name": "nombre","type": "text"}),
            'direccion': forms.TextInput(attrs={"class": "form-control","name": "direccion",}),
            'telefono': forms.TextInput(attrs={"class": "form-control","name": "telefono"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),            
        }
        
    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

        
class TransporteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo'].widget.attrs['autofocus'] = True

    class Meta:
        model = Transporte
        fields = ['codigo', 'nombres', 'apellidos', 'rut', 'patente1',
                  'patente2', 'telefono', 'exportadora']
        labels = {
            'codigo': 'Código',
            'nombres': 'Nombres (Chofer)',
            'apellidos': 'Apellidos (Chofer)',
            'rut': 'Rut (Dni)',
            'patente1': 'Patente Camión',
            'patente2': 'Patente Carro',
            'telefono': 'Telefono Chofer',
            'exportadora': 'Nombre Exportadora',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={"class": "form-control", "name": "codigo", "type": "text"}),
            'nombres': forms.TextInput(attrs={"class": "form-control"}),
            'apellidos': forms.TextInput(attrs={"class": "form-control"}),
            'rut': forms.TextInput(attrs={"class": "form-control", "data-toggle": "input-mask", "data-mask-format": "00.000.000-A", }),
            'patente1': forms.TextInput(attrs={"class": "form-control", "data-toggle": "input-mask", "data-mask-format": "AA-AA-00", }),
            'patente2': forms.TextInput(attrs={"class": "form-control", "data-toggle": "input-mask", "data-mask-format": "AA-AA-00", }),
            'telefono': forms.TextInput(attrs={"class": "form-control", "data-toggle": "input-mask", "data-mask-format": "(+56) 0 0000 0000", }),
            'exportadora': forms.Select(attrs={"class": "form-control"}),

        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

