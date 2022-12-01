from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.sadema.forms import UbicacionForm
from core.pos.mixins import ValidatePermissionRequiredMixin
from core.sadema.models import Ubicacion


class UbicacionListView(ValidatePermissionRequiredMixin, ListView):
    model = Ubicacion
    template_name = 'ubicacion/list.html'
    permission_required = 'view_ubicacion'
    url_redirect = reverse_lazy('dashboard')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search':
                data = []
                for i in Ubicacion.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Ubicaciones'
        context['create_url'] = reverse_lazy('ubicacion_create')
        context['list_url'] = reverse_lazy('ubicacion_list')
        context['entity'] = 'Ubicacion'
        return context


class UbicacionCreateView(ValidatePermissionRequiredMixin, CreateView):
    model = Ubicacion
    form_class = UbicacionForm
    template_name = 'ubicacion/create.html'
    success_url = reverse_lazy('ubicacion_list')
    url_redirect = success_url
    permission_required = 'add_ubicacion'

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
        context['title'] = 'Creación de una Ubicacion'
        context['entity'] = 'Ubicacion'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class UbicacionUpdateView(ValidatePermissionRequiredMixin, UpdateView):
    model = Ubicacion
    form_class = UbicacionForm
    template_name = 'ubicacion/create.html'
    success_url = reverse_lazy('ubicacion_list')
    url_redirect = success_url
    permission_required = 'change_ubicacion'

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
        context['title'] = 'Edición de una Ubicacion'
        context['entity'] = 'Ubicacion'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class UbicacionDeleteView(ValidatePermissionRequiredMixin, DeleteView):
    model = Ubicacion
    template_name = 'ubicacion/delete.html'
    success_url = reverse_lazy('ubicacion_list')
    url_redirect = success_url
    permission_required = 'delete_ubicacion'

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
        context['title'] = 'Eliminación de una Ubicacion'
        context['entity'] = 'Ubicacion'
        context['list_url'] = self.success_url
        return context
