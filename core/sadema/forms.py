
from django import forms
from core.sadema.models import *
from django.forms import ModelChoiceField,Select,ModelForm


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
    ubicacion = ModelChoiceField(queryset=Ubicacion.objects.all(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))

    equipo = ModelChoiceField(queryset=Equipo.objects.all(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))

    labor = ModelChoiceField(queryset=Labor.objects.all(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))
   
    trabajador = ModelChoiceField(queryset=Trabajador.objects.all(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))

    class Meta:
        model = Registro
        fields = ['fecha', 'hora','ubicacion', 'equipo','labor','trabajador', 'observaciones']        

        widgets = {
            # Informacion General
            'fecha': forms.DateInput(attrs={"class": "form-control font-12 text-center ", "type": "date"}),
            'hora': forms.TimeInput(attrs={"class": "form-control font-12 text-center", "type": "time"}),
            'observaciones': forms.Textarea(attrs={"class": "form-control", "rows": "3", "placeholder": "Ingresa observaciones aqui....."}),                   

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