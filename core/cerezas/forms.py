from django import forms
from core.cerezas.models import FormCerezaModels
from django.forms import ModelForm
from django.forms import ModelChoiceField,Select
from core.contenedor.models import *


class TestForm(ModelForm):
    exportadora = ModelChoiceField(queryset=Exportadora.objects.all(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))

    productor = ModelChoiceField(queryset=Productor.objects.none(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))

    transporte = ModelChoiceField(queryset=Transporte.objects.none(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))

    ################################

    especie = ModelChoiceField(queryset=Especie.objects.all(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))
    variedad = ModelChoiceField(queryset=Variedad.objects.none(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))
    class Meta:
        model = FormCerezaModels

        fields = [
            'Lote',
            # 'Exportadora',
            # 'Productor',
            'Fecha_Recepcion',
            'Hora_Recepcion',
            'Hora_Analisis',
            'Tmin',
            'Tmax',
            'Tip_Trans',
            'Nguia',
            'Tip_Env',
            'NEnv',
            'KNeto',
            'NFruto',
            'Hidro',
            # Distribucion por Calibre
            'PC',
            'L',
            'XL',
            'J',
            'J2',
            'J3',
            'J4',
            # Distribucion Color
            'Rojo',
            'RojoCaoba',
            'Caoba',
            'CaobaOscuro',
            'Negro',
            # Distribucion FirmPro
            'Blando',
            'Sensible',
            'Firme',
            'MuyFirme',
            'FP_L',
            'FP_XL',
            'FP_J',
            'FP_J2',
            'FP_J3',
            'FP_J4',
            'FPProm',
            # Distribucion Analisis Masa
            'C1F1',
            'C1F2',
            'C1F3',
            'C1F4',
            'C1F5',
            'C2F1',
            'C2F2',
            'C2F3',
            'C2F4',
            'C2F5',
            'CalibreLight',
            'CalibreDark',
            'PromMasa1',
            'PromMasa2',
            # Distribucion Solido Soluble
            'ssLL',
            'ssXLL',
            'ssJL',
            'ss2JL',
            'ss3JL',
            'ss4JL',
            'ssLD',
            'ssXLD',
            'ssJD',
            'ss2JD',
            'ss3JD',
            'ss4JD',
            'PromLight',
            'PromDark',
            # Cereza_DefCalidad
            'DInsecto' ,
            'DTrips',
            'FaltaColor',
            'FrutoDeforme',
            'FrutoDoble',
            'SinPedicelo',
            'GuataBlanca',
            'HeridaCicatrizada',
            'Hijuelo',
            'Manchas',
            'Medialuna',
            'MezclaVariedad',
            'Roce',
            'Russet' ,
            'RestosFlorales',
            'PielLagarto',
            'GolpeSol',
            'ResiduoProducto',
            'TotCalidad',
            # Cereza_DefCondicion
            'Adhesion',
            'DPajaro',
            'DepresionSevera',
            'FrutoBlando',
            'FrutoDeshidratado',
            'HeridaAbierta',
            'Machucon',
            'ManchaPudricion',
            'Partidura',
            'PartiduraApical',
            'PediceloDeshidratado',
            'PittingPunteadura',
            'Pudricion',
            'Sobremadurez',
            'SuturaAbierta',
            'DescarroPedicelar',
            'PartiduraBasal',
            'TotCondicion',
            'observaciones',
            # Resultados
            'PrecalibreTot',
            'CalidadTotal',
            'CondicionTotal',
            'TotalExportable',
            'images1',
            'images2',
            'images3',
            'images4',

        ]

        widgets = {
            # Informacion General
            'Lote': forms.TextInput(attrs={"class": "form-control font-12 text-center", "id": "Lote", 'name': 'Lote', "required": True}),
            'Fecha_Recepcion': forms.DateInput(attrs={"class": "form-control font-12 text-center ", "type": "date"}),
            'Hora_Recepcion': forms.TimeInput(attrs={"class": "form-control font-12 text-center", "type": "time"}),
            'Hora_Analisis': forms.TimeInput(attrs={"class": "form-control font-12 text-center", "type": "time"}),
            'Tmin': forms.TextInput(attrs={"class": "form-control font-12 text-center"}),
            'Tmax': forms.TextInput(attrs={"class": "form-control font-12 text-center"}),
            'Tip_Trans': forms.Select(attrs={"class": "form-select font-12 text-center"}),
            'Nguia': forms.TextInput(attrs={"class": "form-control font-12 text-center"}),
            'Tip_Env': forms.Select(attrs={"class": "form-select font-12 text-center"}),
            'NEnv': forms.NumberInput(attrs={"class": "form-control font-12 text-center"}),
            'KNeto': forms.NumberInput(attrs={"class": "form-control font-12 text-center"}),
            'NFruto': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "id": "NFruto", "name": "NFruto"}),
            'Hidro': forms.CheckboxInput(attrs={"type": "checkbox", "id": "switch3", "checked data-switch": "secondary"}),
            # Distribucion por Calibre
            'PC': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "PCalibre", "onchange": "calcularTodo();", }),
            'L': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", }),
            'XL': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", }),
            'J': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", }),
            'J2': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", }),
            'J3': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", }),
            'J4': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", }),
            # Distribucion Color
            'Rojo': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", }),
            'RojoCaoba': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", }),
            'Caoba': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", }),
            'CaobaOscuro': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", }),
            'Negro': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", }),
            # Distribucion FirmPro
            'Blando': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", }),
            'Sensible': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", }),
            'Firme': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", }),
            'MuyFirme': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", }),
            'FP_L': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "id": "FP_L", "data-toggle": "input-mask", "data-mask-format": "000", "onchange": "calcularTodo();"}),
            'FP_XL': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "id": "FP_XL", "data-toggle": "input-mask", "data-mask-format": "000", "onchange": "calcularTodo();"}),
            'FP_J': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "id": "FP_J", "data-toggle": "input-mask", "data-mask-format": "000", "onchange": "calcularTodo();"}),
            'FP_J2': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "id": "FP_J2", "data-toggle": "input-mask", "data-mask-format": "000", "onchange": "calcularTodo();"}),
            'FP_J3': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "id": "FP_J3", "data-toggle": "input-mask", "data-mask-format": "000", "onchange": "calcularTodo();"}),
            'FP_J4': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "id": "FP_J4", "data-toggle": "input-mask", "data-mask-format": "000", "onchange": "calcularTodo();"}),
            'FPProm': forms.TextInput(attrs={"class": "form-control font-12 text-center", "id": "promedioFP1", "name": "promedioFP1", "readonly": "", }),
            # Distribucion Analisis Masa
            'C1F1': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "id": "C1F1", "onchange": "calcularTodo();"}),
            'C1F2': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "id": "C1F2", "onchange": "calcularTodo();"}),
            'C1F3': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "id": "C1F3", "onchange": "calcularTodo();"}),
            'C1F4': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "id": "C1F4", "onchange": "calcularTodo();"}),
            'C1F5': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "id": "C1F5", "onchange": "calcularTodo();"}),
            'C2F1': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "id": "C2F1", "onchange": "calcularTodo();"}),
            'C2F2': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "id": "C2F2", "onchange": "calcularTodo();"}),
            'C2F3': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "id": "C2F3", "onchange": "calcularTodo();"}),
            'C2F4': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "id": "C2F4", "onchange": "calcularTodo();"}),
            'C2F5': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "id": "C2F5", "onchange": "calcularTodo();"}),
            'CalibreLight': forms.Select(attrs={"class": "form-select font-12 text-center", "name": "CalibreLight"}),
            'CalibreDark': forms.Select(attrs={"class": "form-select font-12 text-center", "name": "CalibreDark"}),
            'PromMasa1': forms.TextInput(attrs={"class": "form-control font-12 text-center", "id": "PromMasa1", "name": "PromMasa1", "readonly": "", }),
            'PromMasa2': forms.TextInput(attrs={"class": "form-control font-12 text-center", "id": "PromMasa2", "name": "PromMasa2", "readonly": "", }),
            # Distribucion Solido Soluble
            'ssLL': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "ssLL", "onchange": "calcularTodo();"}),
            'ssXLL': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "ssXLL", "onchange": "calcularTodo();"}),
            'ssJL': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "ssJL", "onchange": "calcularTodo();"}),
            'ss2JL': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "ss2JL", "onchange": "calcularTodo();"}),
            'ss3JL': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "ss3JL", "onchange": "calcularTodo();"}),
            'ss4JL': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "ss4JL", "onchange": "calcularTodo();"}),
            'ssLD': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "ssLD", "onchange": "calcularTodo();"}),
            'ssXLD': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "ssXLD", "onchange": "calcularTodo();"}),
            'ssJD': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "ssJD", "onchange": "calcularTodo();"}),
            'ss2JD': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "ss2JD", "onchange": "calcularTodo();"}),
            'ss3JD': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "ss3JD", "onchange": "calcularTodo();"}),
            'ss4JD': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "ss4JD", "onchange": "calcularTodo();"}),
            'PromLight': forms.TextInput(attrs={"class": "form-control font-12 text-center", "id": "PromLight", "name": "PromLight", "readonly": "", }),
            'PromDark': forms.TextInput(attrs={"class": "form-control font-12 text-center", "id": "PromDark", "name": "PromDark", "readonly": "", }),
            
            # Cereza_DefCalidad
            'DInsecto' : forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFC1", "onchange": "calcularTodo();"}), 
            'DTrips' : forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFC2", "onchange": "calcularTodo();"}),
            'FaltaColor' : forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFC3", "onchange": "calcularTodo();"}),
            'FrutoDeforme': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFC4", "onchange": "calcularTodo();"}),
            'FrutoDoble': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFC5", "onchange": "calcularTodo();"}),
            'SinPedicelo': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFC6", "onchange": "calcularTodo();"}),
            'GuataBlanca': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFC7", "onchange": "calcularTodo();"}),
            'HeridaCicatrizada': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFC8", "onchange": "calcularTodo();"}),
            'Hijuelo': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFC9", "onchange": "calcularTodo();"}),
            'Manchas': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFC10", "onchange": "calcularTodo();"}),
            'Medialuna': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFC11", "onchange": "calcularTodo();"}),
            'MezclaVariedad': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFC12", "onchange": "calcularTodo();"}),
            'Roce': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFC13", "onchange": "calcularTodo();"}),
            'Russet' : forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFC14", "onchange": "calcularTodo();"}),
            'RestosFlorales': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFC15", "onchange": "calcularTodo();"}),
            'PielLagarto': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFC16", "onchange": "calcularTodo();"}),
            'GolpeSol': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFC17", "onchange": "calcularTodo();"}),
            'ResiduoProducto': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFC18", "onchange": "calcularTodo();"}),
            'TotCalidad': forms.TextInput(attrs={"class": "form-control font-12 text-center", "id": "TotCalidad", "name": "TotCalidad", "readonly": "", "onchange": "Resultados();", }),
            # Cereza_DefCondicion
            'Adhesion': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFCo1", "onchange": "calcularTodo();"}),
            'DPajaro': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFCo2", "onchange": "calcularTodo();"}),
            'DepresionSevera': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFCo3", "onchange": "calcularTodo();"}),
            'FrutoBlando': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFCo4", "onchange": "calcularTodo();"}),
            'FrutoDeshidratado': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFCo5", "onchange": "calcularTodo();"}),
            'HeridaAbierta': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFCo6", "onchange": "calcularTodo();"}),
            'Machucon': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFCo7", "onchange": "calcularTodo();"}),
            'ManchaPudricion': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFCo8", "onchange": "calcularTodo();"}),
            'Partidura': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFCo9", "onchange": "calcularTodo();"}),
            'PartiduraApical': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFCo10", "onchange": "calcularTodo();"}),
            'PediceloDeshidratado': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFCo11", "onchange": "calcularTodo();"}),
            'PittingPunteadura': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFCo12", "onchange": "calcularTodo();"}),
            'Pudricion': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFCo13", "onchange": "calcularTodo();"}),
            'Sobremadurez': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFCo14", "onchange": "calcularTodo();"}),
            'SuturaAbierta': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFCo15", "onchange": "calcularTodo();"}),
            'DescarroPedicelar': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFCo16", "onchange": "calcularTodo();"}),
            'PartiduraBasal': forms.NumberInput(attrs={"class": "form-control font-12 text-center", "data-toggle": "input-mask", "data-mask-format": "000", "id": "DFCo17", "onchange": "calcularTodo();"}),
            'TotCondicion': forms.TextInput(attrs={"class": "form-control font-12 text-center", "id": "TotCondicion", "name": "TotCondicion", "readonly": "", "onchange": "calcularTodo();", }),

            'observaciones': forms.Textarea(attrs={"class": "form-control", "rows": "3", "placeholder": "Ingresa observaciones aqui....."}),
            # Resultados
            'PrecalibreTot': forms.TextInput(attrs={"class": "form-control font-14 text-center p-2", "id": "PrecalibreTot", "name": "PrecalibreTot", "readonly": "", "onchange": "calcularTodo();", }),
            'CalidadTotal': forms.TextInput(attrs={"class": "form-control font-14 text-center p-2", "id": "CalidadTotal", "name": "CalidadTotal", "readonly": "", "onchange": "calcularTodo();", }),
            'CondicionTotal': forms.TextInput(attrs={"class": "form-control font-14 text-center p-2", "id": "CondicionTotal", "name": "CondicionTotal", "readonly": "", "onchange": "calcularTodo();", }),
            'TotalExportable': forms.TextInput(attrs={"class": "form-control font-14 text-center p-2", "id": "TotalExportable", "name": "TotalExportable", "readonly": "", }),

            'images1': forms.FileInput(attrs={"class": "form-control", "id": "inputGroupFile01", "name": "imagen1", "type": "file"}),
            'images2': forms.FileInput(attrs={"class": "form-control", "id": "inputGroupFile02", "name": "imagen2", "type": "file"}),
            'images3': forms.FileInput(attrs={"class": "form-control", "id": "inputGroupFile03", "name": "imagen3", "type": "file"}),
            'images4': forms.FileInput(attrs={"class": "form-control", "id": "inputGroupFile04", "name": "imagen4", "type": "file"}),


        }
