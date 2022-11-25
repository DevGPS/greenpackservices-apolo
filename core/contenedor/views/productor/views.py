from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.contenedor.forms import ProductorForm
from core.pos.mixins import ValidatePermissionRequiredMixin
from core.contenedor.models import Productor


class ProductorListView(ValidatePermissionRequiredMixin, ListView):
    model = Productor
    template_name = 'productor/list.html'
    permission_required = 'view_productor'
    url_redirect = reverse_lazy('dashboard')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search':
                data = []
                for i in Productor.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Productores'
        context['create_url'] = reverse_lazy('productor_create')
        context['list_url'] = reverse_lazy('productor_list')
        context['entity'] = 'Productor'
        return context


class ProductorCreateView(ValidatePermissionRequiredMixin, CreateView):
    model = Productor
    form_class = ProductorForm
    template_name = 'productor/create.html'
    success_url = reverse_lazy('productor_list')
    url_redirect = success_url
    permission_required = 'add_productor'

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
        context['title'] = 'Creación de un Productor'
        context['entity'] = 'Productor'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class ProductorUpdateView(ValidatePermissionRequiredMixin, UpdateView):
    model = Productor
    form_class = ProductorForm
    template_name = 'productor/create.html'
    success_url = reverse_lazy('productor_list')
    url_redirect = success_url
    permission_required = 'change_productor'

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
        context['title'] = 'Edición una Productor'
        context['entity'] = 'Productor'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class ProductorDeleteView(ValidatePermissionRequiredMixin, DeleteView):
    model = Productor
    template_name = 'productor/delete.html'
    success_url = reverse_lazy('productor_list')
    url_redirect = success_url
    permission_required = 'delete_productor'

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
        context['title'] = 'Eliminación de un Productor'
        context['entity'] = 'Productor'
        context['list_url'] = self.success_url
        return context
