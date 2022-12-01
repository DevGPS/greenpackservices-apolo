from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.sadema.forms import LaborForm
from core.pos.mixins import ValidatePermissionRequiredMixin
from core.sadema.models import Labor


class LaborListView(ValidatePermissionRequiredMixin, ListView):
    model = Labor
    template_name = 'labor/list.html'
    permission_required = 'view_labor'
    url_redirect = reverse_lazy('dashboard')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search':
                data = []
                for i in Labor.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Labores'
        context['create_url'] = reverse_lazy('labor_create')
        context['list_url'] = reverse_lazy('labor_list')
        context['entity'] = 'Labor'
        return context


class LaborCreateView(ValidatePermissionRequiredMixin, CreateView):
    model = Labor
    form_class = LaborForm
    template_name = 'labor/create.html'
    success_url = reverse_lazy('labor_list')
    url_redirect = success_url
    permission_required = 'add_labor'

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
        context['title'] = 'Creación de Labores'
        context['entity'] = 'Labor'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class LaborUpdateView(ValidatePermissionRequiredMixin, UpdateView):
    model = Labor
    form_class = LaborForm
    template_name = 'labor/create.html'
    success_url = reverse_lazy('labor_list')
    url_redirect = success_url
    permission_required = 'change_labor'

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
        context['title'] = 'Edición una Labor'
        context['entity'] = 'Labor'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class LaborDeleteView(ValidatePermissionRequiredMixin, DeleteView):
    model = Labor
    template_name = 'labor/delete.html'
    success_url = reverse_lazy('labor_list')
    url_redirect = success_url
    permission_required = 'delete_labor'

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
        context['title'] = 'Eliminación de un Labor'
        context['entity'] = 'Labor'
        context['list_url'] = self.success_url
        return context
