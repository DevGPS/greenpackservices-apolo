from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PrincipalForms
from django.contrib import messages
from django.views.generic import View
from core.cerezas.models import FormCerezaModels
from .utils import render_to_pdf
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from core.contenedor.models import *

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from core.contenedor.forms import TestForm
from core.contenedor.models import Productor


class TestView(TemplateView):
    template_name = 'tests.html'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_product_id':
                data = [{'id': '', 'text': '------------'}]
                for i in Productor.objects.filter(id=request.POST['id']):
                    data.append({'id': i.id, 'text': i.name, 'data': i.cat.toJSON()})
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Select Aninados | Django'
        context['form'] = TestForm()
        return context

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

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_product_id':
                data = [{'id': '', 'text': '------------'}]
                for i in Productor.objects.filter(cat_id=request.POST['id']):
                    data.append({'id': i.id, 'text': i.name, 'data': i.cat.toJSON()})
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

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
