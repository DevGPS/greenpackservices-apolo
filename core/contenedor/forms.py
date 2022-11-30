from django import forms
from django.forms import *

from core.contenedor.models import *

class ExportadoraForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['codigo'].widget.attrs['autofocus'] = True
    class Meta:
        model = Exportadora
        fields = ['codigo','nombre', 'direccion','temporada', 'telefono', 'email']
        
       
        
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
        fields = ['codigo','nombre', 'temporada']
        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre Especie',
            'temporada': 'Temporada',           

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

class TestForm(Form):
    exportadora = ModelChoiceField(queryset=Exportadora.objects.all(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))

    productor = ModelChoiceField(queryset=Productor.objects.none(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))