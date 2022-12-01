from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.sadema.forms import TrabajadorForm
from core.pos.mixins import ValidatePermissionRequiredMixin
from core.sadema.models import Trabajador



class TrabajadorListView(ValidatePermissionRequiredMixin, ListView):
    model = Trabajador
    template_name = 'trabajador/list.html'
    permission_required = 'view_trabajador'
    url_redirect = reverse_lazy('dashboard')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search':
                data = []
                for i in Trabajador.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Trabajadores'
        context['create_url'] = reverse_lazy('trabajador_create')
        context['list_url'] = reverse_lazy('trabajador_list')
        context['entity'] = 'Trabajador'
        return context


class TrabajadorCreateView(ValidatePermissionRequiredMixin, CreateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = 'trabajador/create.html'
    success_url = reverse_lazy('trabajador_list')
    url_redirect = success_url
    permission_required = 'add_trabajador'

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
        context['title'] = 'Creación de un Trabajador'
        context['entity'] = 'Trabajador'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class TrabajadorUpdateView(ValidatePermissionRequiredMixin, UpdateView):
    model = Trabajador
    form_class = TrabajadorForm
    template_name = 'trabajador/create.html'
    success_url = reverse_lazy('trabajador_list')
    url_redirect = success_url
    permission_required = 'change_trabajador'

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
        context['title'] = 'Edición de un Trabajador'
        context['entity'] = 'Trabajador'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class TrabajadorDeleteView(ValidatePermissionRequiredMixin, DeleteView):
    model = Trabajador
    template_name = 'trabajador/delete.html'
    success_url = reverse_lazy('trabajador_list')
    url_redirect = success_url
    permission_required = 'delete_trabajador'

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
        context['title'] = 'Eliminación de un Trabajador'
        context['entity'] = 'Trabajador'
        context['list_url'] = self.success_url
        return context
