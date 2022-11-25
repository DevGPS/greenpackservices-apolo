from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PrincipalForms
from django.contrib import messages
from django.views.generic import View
from core.cerezas.models import FormCerezaModels
from .utils import render_to_pdf
from django.http import HttpResponse
from datetime import datetime


class FormCerezaPdf(View):
    def get(self, request, *args, **kwargs):
        registros = FormCerezaModels.objects.all()
        fecha = datetime.now()
        data = {
            'fecha': fecha,
            'registros': registros
        }
        pdf = render_to_pdf('cerezas/report-cereza/report-list-cereza.html', data)
        return HttpResponse(pdf, content_type='application/pdf')

@login_required
def PDF_form_cereza(request, Lote):
    registros = get_object_or_404(FormCerezaModels, Lote=Lote)
    fecha = datetime.now()  
    
    data = {
        'fecha': fecha,
        'registros': registros,
    }
    pdf = render_to_pdf('cerezas/report-cereza/report-lote-cereza.html', data)
    return HttpResponse(pdf, content_type='application/pdf')




@login_required
def create_form_cereza(request):
    if request.method == 'POST':
        registros = FormCerezaModels.objects.all()
        form = PrincipalForms(request.POST, request.FILES)
        if form.is_valid():
            new_registro = form.save(commit=False)
            new_registro.user = request.user
            new_registro.save()
            messages.success(request, '!Registrado Exitosamente!')
            return redirect('read_cerezas')
        else:
            messages.success(request, '!No se pudo realizar el registro!')
            return redirect('create_cerezas')       
    else:
        form = PrincipalForms()
        return render(request, "cerezas/create.html", {"r": PrincipalForms})



def read_form_cereza(request):
    registros = FormCerezaModels.objects.all()
    return render(request, "cerezas/read.html", {"registros": registros})


@login_required
def update_form_cereza(request, Lote):
    registros = FormCerezaModels.objects.get(Lote=Lote)
    data = {
        'r': PrincipalForms(instance=registros),
        'i1': registros.images1,
        'i2': registros.images2,
        'i3': registros.images3,
        'i4': registros.images4,        

    }
    if request.method == "POST":
        form = PrincipalForms(request.POST, request.FILES , instance=registros) 
        if form.is_valid():
            form.save()
            messages.success(
                request, '!Registro de Cereza actualizado Exitosamente!')
            return redirect('read_cerezas')
        data["form"] = form

    return render(request, "cerezas/update.html", data)


@login_required
def delete_form_cereza(request, Lote):
    registros = FormCerezaModels.objects.get(Lote=Lote)
    registros.delete()
    messages.success(request, '!Registro de Cereza eliminado Exitosamente!')
    return redirect('read_cerezas')
