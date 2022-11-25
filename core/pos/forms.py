from django import forms
from django.forms import ModelForm

from core.pos.models import *

class ExportadoraForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].widget.attrs['autofocus'] = True
   
    class Meta:
        model = Exportadora
        fields = ['codigo','nombre', 'direccion', 'telefono', 'email']
        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre Exportadora',
            'direccion': 'Dirección',
            'telefono': 'Telefono',
            'email': 'Correo Electrónico',            
        }
        widgets = {
            'codigo': forms.TextInput(attrs={"class": "form-control","name": "codigo","type": "text"}),
            'nombre': forms.TextInput(attrs={"class": "form-control","name": "nombre","type": "text"}),
            'direccion': forms.TextInput(attrs={"class": "form-control","name": "direccion",}),
            'telefono': forms.TextInput(attrs={"class": "form-control","name": "telefono"}),
            'email': forms.EmailInput(attrs={"class": "form-control"}),            
        }
        
class TransporteForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombres'].widget.attrs['autofocus'] = True

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


class ProductForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Ingrese un nombre',
            }),
            'category': forms.Select(attrs={
                'class': 'select2',
                'style': 'width: 100%'
            }),
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


class ClientForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['names'].widget.attrs['autofocus'] = True

    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'names': forms.TextInput(attrs={'placeholder': 'Ingrese un nombre'}),
            'dni': forms.TextInput(attrs={'placeholder': 'Ingrese un número de cedula'}),
            'birthdate': forms.DateInput(format='%Y-%m-%d', attrs={
                'class': 'form-control datetimepicker-input',
                'id': 'birthdate',
                'value': datetime.now().strftime('%Y-%m-%d'),
                'data-toggle': 'datetimepicker',
                'data-target': '#birthdate'
            }),
            'address': forms.TextInput(attrs={
                'placeholder': 'Ingrese una dirección',
            }),
            'gender': forms.Select(attrs={
                'class': 'select2',
                'style': 'width: 100%'
            })
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class SaleForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['client'].queryset = Client.objects.none()

    class Meta:
        model = Sale
        fields = '__all__'
        widgets = {
            'client': forms.Select(attrs={
                'class': 'custom-select select2',
                # 'style': 'width: 100%'
            }),
            'date_joined': forms.DateInput(format='%Y-%m-%d', attrs={
                'value': datetime.now().strftime('%Y-%m-%d'),
                'autocomplete': 'off',
                'class': 'form-control datetimepicker-input',
                'id': 'date_joined',
                'data-target': '#date_joined',
                'data-toggle': 'datetimepicker'
            }
            ),
            'iva': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'subtotal': forms.TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            }),
            'total': forms.TextInput(attrs={
                'readonly': True,
                'class': 'form-control',
            })
        }


class CompanyForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True

    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ingrese un nombre'}),
            'ruc': forms.TextInput(attrs={'placeholder': 'Ingrese un ruc'}),
            'address': forms.TextInput(attrs={'placeholder': 'Ingrese una dirección'}),
            'mobile': forms.TextInput(attrs={'placeholder': 'Ingrese un teléfono celular'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Ingrese un teléfono convencional'}),
            'website': forms.TextInput(attrs={'placeholder': 'Ingrese una dirección web'}),
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
