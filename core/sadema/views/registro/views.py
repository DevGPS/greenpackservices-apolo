from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.sadema.forms import RegistroForm
from core.pos.mixins import ValidatePermissionRequiredMixin
from core.sadema.models import *
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404


class RegistroListView(ValidatePermissionRequiredMixin, ListView):
    model = Registro
    template_name = 'registro/list.html'
    permission_required = 'view_registro'
    url_redirect = reverse_lazy('dashboard')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search':
                data = []
                for i in Registro.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de registros'
        context['create_url'] = reverse_lazy('registro_create')
        context['list_url'] = reverse_lazy('registro_list')
        context['entity'] = 'Registro'
        return context

    


class RegistroCreateView(ValidatePermissionRequiredMixin, CreateView):
    model = Registro
    form_class = RegistroForm
    template_name = 'registro/create.html'
    success_url = reverse_lazy('registro_list')
    url_redirect = success_url
    permission_required = 'add_registro'

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data = {}
        try:            
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            elif action == 'search_equipo_id':
                data = [{'id': '', 'text': '--Equipos Cargados--'}]
                for i in Equipo.objects.filter(ubicacion_id=request.POST['id']):
                    data.append({'id': i.id, 'text': i.nombre,'data': i.ubicacion.toJSON()})
            elif action == 'search_labor_id':
                data = [{'id': '', 'text': '--Labores Cargados--'}]
                for i in Labor.objects.filter(ubicacion_id=request.POST['id']):
                    data.append({'id': i.id, 'text': i.nombre,'data': i.ubicacion.toJSON()})
            elif action == 'search_trabajador_id':
                data = [{'id': '', 'text': '--Trabajadores Cargadas--'}]
                for i in Trabajador.objects.filter(ubicacion_id=request.POST['id']):
                    data.append({'id': i.id, 'text': i.nombre,'data': i.ubicacion.toJSON()})
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Registro'
        context['entity'] = 'Registro'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context
   


class RegistroUpdateView(ValidatePermissionRequiredMixin, UpdateView):
    model = Registro
    form_class = RegistroForm
    template_name = 'registro/create.html'
    success_url = reverse_lazy('registro_list')
    url_redirect = success_url
    permission_required = 'change_registroo'

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
        context['title'] = 'Edición de un registro'
        context['entity'] = 'Registro'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context
    


class RegistroDeleteView(ValidatePermissionRequiredMixin, DeleteView):
    model = Registro
    template_name = 'registro/delete.html'
    success_url = reverse_lazy('registro_list')
    url_redirect = success_url
    permission_required = 'delete_registro'

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
        context['title'] = 'Eliminación de un Registro'
        context['entity'] = 'Registro'
        context['list_url'] = self.success_url
        return context
    
