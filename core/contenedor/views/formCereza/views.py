from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.contenedor.forms import CerezaForm
from core.pos.mixins import ValidatePermissionRequiredMixin
from core.contenedor.models import *
from django.views.generic import View


from core.contenedor.utils import render_to_pdf
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


class FormCerezaListView(ValidatePermissionRequiredMixin, ListView):
    model = FormCerezaModels
    template_name = 'formCereza/list.html'
    permission_required = 'view_formCereza'
    url_redirect = reverse_lazy('dashboard')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search':
                data = []
                for i in FormCerezaModels.objects.all():
                    data.append(i.toJSON())            

            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Formularios'
        context['create_url'] = reverse_lazy('formCereza_create')
        context['list_url'] = reverse_lazy('formCereza_list')
        context['entity'] = 'FormCerezaModels'
        return context


class FormCerezaCreateView(ValidatePermissionRequiredMixin, CreateView):
    model = FormCerezaModels
    form_class = CerezaForm
    template_name = 'formCereza/create.html'
    success_url = reverse_lazy('formCereza_list')
    url_redirect = success_url
    

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            elif action == 'search_productor_id':
                data = [{'id': '', 'text': '--Productores Cargados--'}]
                for i in Productor.objects.filter(exportadora_id=request.POST['id']):
                    data.append({'id': i.id, 'text': i.nombre,'data': i.exportadora.toJSON()})

            elif action == 'search_transporte_id':
                data = [{'id': '', 'text': '--Camiones Cargados--'}]
                for i in Transporte.objects.filter(exportadora_id=request.POST['id']):
                    data.append({'id': i.id, 'text': i.patente1,'data': i.exportadora.toJSON()})

            elif action == 'search_variedad_id':
                data = [{'id': '', 'text': '--Variedades Cargadas--'}]
                for i in Variedad.objects.filter(especie_id=request.POST['id']):
                    data.append({'id': i.id, 'text': i.nombre,'data': i.especie.toJSON()})
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Formulario Cereza 22-23 | Green Pack Services'
        context['entity'] = 'FormCerezaModels'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class FormCerezaUpdateView(ValidatePermissionRequiredMixin, UpdateView):
    model = FormCerezaModels
    form_class = CerezaForm
    template_name = 'formCereza/create.html'
    success_url = reverse_lazy('formCereza_list')
    url_redirect = success_url
    permission_required = 'change_formCereza'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición una Registro de Cerezas'
        context['entity'] = 'FormCerezaModels'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class FormCerezaDeleteView(ValidatePermissionRequiredMixin, DeleteView):
    model = FormCerezaModels
    template_name = 'formCereza/delete.html'
    success_url = reverse_lazy('formCereza_list')
    url_redirect = success_url
    permission_required = 'delete_formCereza'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Registro de Cerezas'
        context['entity'] = 'FormCerezaModels'
        context['list_url'] = self.success_url
        return context


class FormCerezaPdf(View):
    def get(self, request, *args, **kwargs):
        registros = FormCerezaModels.objects.all()
        fecha = datetime.now()
        data = {
            'fecha': fecha,
            'registros': registros
        }
        pdf = render_to_pdf(
            'formCereza/report-cereza/report-list-cereza.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


@login_required
def PDF_form_cereza(request, Lote):
    registros = get_object_or_404(FormCerezaModels, Lote=Lote)
    fecha = datetime.now()

    data = {
        'fecha': fecha,
        'registros': registros,
    }
    pdf = render_to_pdf('formCereza/report-cereza/report-lote-cereza.html', data)
    return HttpResponse(pdf, content_type='application/pdf')






