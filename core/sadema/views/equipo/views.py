from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.sadema.forms import EquipoForm
from core.pos.mixins import ValidatePermissionRequiredMixin
from core.sadema.models import Equipo


class EquipoListView(ValidatePermissionRequiredMixin, ListView):
    model = Equipo
    template_name = 'equipo/list.html'
    permission_required = 'view_equipo'
    url_redirect = reverse_lazy('dashboard')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search':
                data = []
                for i in Equipo.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Equipos'
        context['create_url'] = reverse_lazy('equipo_create')
        context['list_url'] = reverse_lazy('equipo_list')
        context['entity'] = 'Equipo'
        return context

    


class EquipoCreateView(ValidatePermissionRequiredMixin, CreateView):
    model = Equipo
    form_class = EquipoForm
    template_name = 'equipo/create.html'
    success_url = reverse_lazy('equipo_list')
    url_redirect = success_url
    permission_required = 'add_equipo'

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Equipo'
        context['entity'] = 'Equipo'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context
   


class EquipoUpdateView(ValidatePermissionRequiredMixin, UpdateView):
    model = Equipo
    form_class = EquipoForm
    template_name = 'equipo/create.html'
    success_url = reverse_lazy('equipo_list')
    url_redirect = success_url
    permission_required = 'change_equipo'

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
        context['title'] = 'Edición un Equipo'
        context['entity'] = 'Equipo'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context
    


class EquipoDeleteView(ValidatePermissionRequiredMixin, DeleteView):
    model = Equipo
    template_name = 'equipo/delete.html'
    success_url = reverse_lazy('equipo_list')
    url_redirect = success_url
    permission_required = 'delete_equipo'

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
        context['title'] = 'Eliminación de un Equipo'
        context['entity'] = 'Equipo'
        context['list_url'] = self.success_url
        return context
    
