
from django import forms

from django.forms import ModelForm

from core.sadema.models import *

class UbicacionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True
    class Meta:
        model = Ubicacion
        fields = ['nombre']
        
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

        
        
class EquipoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Equipo
        fields = ['nombre', 'ubicacion']
        labels = {
            'nombre': 'Nombres',
            'ubicacion ': 'Ubicación',           
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

class LaborForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Labor
        fields = ['nombre', 'ubicacion']
        labels = {
            'nombre': 'Nombres',
            'ubicacion ': 'Ubicación',           
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

class TrabajadorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Trabajador
        fields = ['nombre','apellido', 'ubicacion']
        labels = {
            'nombre': 'Nombres',
            'apellido': 'Apellidos',
            'ubicacion ': 'Ubicación',           
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

class RegistroForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['trabajador'].widget.attrs['autofocus'] = True

    class Meta:
        model = Registro
        fields = ['trabajador','labor', 'equipo','ubicacion','fecha', 'hora']
        labels = {
            'trabajador': 'Trabajador',
            'labor': 'Labor',
            'equipo ': 'Equipo',
            'ubicacion ': 'Ubicación',           
            'fecha ': 'Fecha Registro',           
            'hora ': 'Hora Registro',           

        }

        widgets = {
            # Informacion General
            'trabajador': forms.Select(attrs={"class": "form-control select2 font-12 text-center", "id": "trabajador", 'name': 'trabajador', "required": True}),
            'labor': forms.Select(attrs={"class": "form-control select2font-12 text-center", "id": "labor", 'name': 'labor', "required": True}),
            'equipo': forms.Select(attrs={"class": "form-control select2 font-12 text-center", "id": "equipo", 'name': 'equipo', "required": True}),
            'ubicacion': forms.Select(attrs={"class": "form-control select2 font-12 text-center", "id": "ubicacion", 'name': 'ubicacion', "required": True}),
            'fecha': forms.DateInput(attrs={"class": "form-control font-12 text-center ", "type": "date"}),
            'hora': forms.TimeInput(attrs={"class": "form-control font-12 text-center", "type": "time"}),
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