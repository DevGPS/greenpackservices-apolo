from django import forms
from django.forms import ModelForm

from core.contenedor.models import *

class ExportadoraForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo'].widget.attrs['autofocus'] = True
    class Meta:
        model = Exportadora
        fields = ['codigo','nombre', 'direccion','temporada', 'telefono', 'email']
        
        widgets = {
            'codigo': forms.TextInput(attrs={"class": "form-control","name": "codigo","type": "text"}),
            'nombre': forms.TextInput(attrs={"class": "form-control","name": "nombre","type": "text"}),
            'direccion': forms.TextInput(attrs={"class": "form-control","name": "direccion",}),
            'telefono': forms.TextInput(attrs={"class": "form-control","name": "telefono"}),            
            'email': forms.EmailInput(attrs={"class": "form-control"}),  
            'temporada': forms.Select(attrs={"class": "form-control","name": "temporada"}),        
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
            'telefono': 'Telefono',
            'exportadora': 'Nombre Exportadora',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={"class": "form-control", "name": "codigo", "type": "text"}),
            'nombres': forms.TextInput(attrs={"class": "form-control"}),
            'apellidos': forms.TextInput(attrs={"class": "form-control"}),
            'rut': forms.TextInput(attrs={"class": "form-control", "data-toggle": "input-mask", "data-mask-format": "00.000.000-A", }),
            'patente1': forms.TextInput(attrs={"class": "form-control", "data-toggle": "input-mask", "data-mask-format": "AA-AA-00", }),
            'patente2': forms.TextInput(attrs={"class": "form-control", "data-toggle": "input-mask", "data-mask-format": "AA-AA-00", }),
            'telefono': forms.TextInput(attrs={"class": "form-control","name": "telefono","data-toggle": "input-mask", "data-mask-format": "(+56) 0 0000 0000",}),
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

class EspecieForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = Especie
        fields = ['codigo','nombre']
        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre Especie',           
        }
        widgets = {
            'codigo': forms.TextInput(attrs={"class": "form-control","name": "codigo",}),
            'nombre': forms.TextInput(attrs={"class": "form-control","name": "especie"}),           
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

class VariedadForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo'].widget.attrs['autofocus'] = True
    class Meta:
        model = Variedad
        fields = ['codigo','nombre','especie']
        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre Variedad',
            'especie': 'Nombre Especie',
            
        }
        widgets = {
            'codigo': forms.TextInput(attrs={"class": "form-control","name": "codigo"}),
            'nombre': forms.TextInput(attrs={"class": "form-control","name": "variedad"}),
            'especie': forms.Select(attrs={"class": "form-control","name": "especie"}),
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

class ProductorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo'].widget.attrs['autofocus'] = True

    class Meta:
        model = Productor
        fields = ['codigo','nombre','CSG', 'direccion', 'telefono', 'email','exportadora']
        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre Productor',
            'CSG': 'Codigo SAG (CSG)',
            'direccion': 'Dirección',
            'telefono': 'Telefono',
            'email': 'Correo Electrónico',
            'exportadora': 'Exportadora',             
        }
        widgets = {
            'codigo': forms.TextInput(attrs={"class": "form-control","name": "codigo","type": "text"}),
            'nombre': forms.TextInput(attrs={"class": "form-control","name": "nombre",}),
            'CSG': forms.TextInput(attrs={"class": "form-control","name": "CSG",}),
            'direccion': forms.TextInput(attrs={"class": "form-control","name": "direccion",}),
            'telefono': forms.TextInput(attrs={"class": "form-control","name": "telefono","data-toggle": "input-mask", "data-mask-format": "(+56) 0 0000 0000",}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),  
            'exportadora': forms.Select(attrs={"class": "form-control","name": "exportadora",}),          
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