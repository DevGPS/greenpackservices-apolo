from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.postcosecha.forms import VariedadForm
from core.pos.mixins import ValidatePermissionRequiredMixin
from core.postcosecha.models import Variedad


class VariedadListView(ValidatePermissionRequiredMixin, ListView):
    model = Variedad
    template_name = 'variedad/list.html'
    permission_required = 'view_variedad'
    url_redirect = reverse_lazy('dashboard')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search':
                data = []
                for i in Variedad.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Variedades'
        context['create_url'] = reverse_lazy('variedad_create')
        context['list_url'] = reverse_lazy('variedad_list')
        context['entity'] = 'Variedad'
        return context


class VariedadCreateView(ValidatePermissionRequiredMixin, CreateView):
    model = Variedad
    form_class = VariedadForm
    template_name = 'variedad/create.html'
    success_url = reverse_lazy('variedad_list')
    url_redirect = success_url
    permission_required = 'add_variedad'

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
        context['title'] = 'Creación de un Variedad'
        context['entity'] = 'Variedad'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class VariedadUpdateView(ValidatePermissionRequiredMixin, UpdateView):
    model = Variedad
    form_class = VariedadForm
    template_name = 'variedad/create.html'
    success_url = reverse_lazy('variedad_list')
    url_redirect = success_url
    permission_required = 'change_variedad'

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
        context['title'] = 'Edición una Variedad'
        context['entity'] = 'Variedad'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class VariedadDeleteView(ValidatePermissionRequiredMixin, DeleteView):
    model = Variedad
    template_name = 'variedad/delete.html'
    success_url = reverse_lazy('variedad_list')
    url_redirect = success_url
    permission_required = 'delete_variedad'

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
        context['title'] = 'Eliminación de una Variedad'
        context['entity'] = 'Variedad'
        context['list_url'] = self.success_url
        return context
