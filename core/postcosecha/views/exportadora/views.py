from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.postcosecha.forms import ExportadoraForm
from core.pos.mixins import ValidatePermissionRequiredMixin
from core.postcosecha.models import Exportadora



class ExportadoraListView(ValidatePermissionRequiredMixin, ListView):
    model = Exportadora
    template_name = 'exportadora/list.html'
    permission_required = 'view_exportadora'
    url_redirect = reverse_lazy('dashboard')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search':
                data = []
                for i in Exportadora.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Exportadora'
        context['create_url'] = reverse_lazy('exportadora_create')
        context['list_url'] = reverse_lazy('exportadora_list')
        context['entity'] = 'Exportadora'
        return context


class ExportadoraCreateView(ValidatePermissionRequiredMixin, CreateView):
    model = Exportadora
    form_class = ExportadoraForm
    template_name = 'exportadora/create.html'
    success_url = reverse_lazy('exportadora_list')
    url_redirect = success_url
    permission_required = 'add_exportadora'

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
        context['title'] = 'Creación de una Exportadora'
        context['entity'] = 'Exportadora'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class ExportadoraUpdateView(ValidatePermissionRequiredMixin, UpdateView):
    model = Exportadora
    form_class = ExportadoraForm
    template_name = 'exportadora/create.html'
    success_url = reverse_lazy('exportadora_list')
    url_redirect = success_url
    permission_required = 'change_exportadora'

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
        context['title'] = 'Edición de una Exportadora'
        context['entity'] = 'Exportadora'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class ExportadoraDeleteView(ValidatePermissionRequiredMixin, DeleteView):
    model = Exportadora
    template_name = 'exportadora/delete.html'
    success_url = reverse_lazy('exportadora_list')
    url_redirect = success_url
    permission_required = 'delete_exportadora'

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
        context['title'] = 'Eliminación de una Exportadora'
        context['entity'] = 'Exportadora'
        context['list_url'] = self.success_url
        return context
