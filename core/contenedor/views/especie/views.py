from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.contenedor.forms import EspecieForm
from core.pos.mixins import ValidatePermissionRequiredMixin
from core.contenedor.models import Especie


class EspecieListView(ValidatePermissionRequiredMixin, ListView):
    model = Especie
    template_name = 'especie/list.html'
    permission_required = 'view_especie'
    url_redirect = reverse_lazy('dashboard')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search':
                data = []
                for i in Especie.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Especies'
        context['create_url'] = reverse_lazy('especie_create')
        context['list_url'] = reverse_lazy('especie_list')
        context['entity'] = 'Especie'
        return context

    def test_func(self):
        # obtenemos todos los grupos del usuario logueado
        grupos = self.request.user.groups.all()
        # comparamos que el usuario pertenezca al grupo VENDEDOR o SUPERVISOR
        for grupo in grupos:
            if grupo in ['Post-Cosecha ', 'Admin']:
                return True
        return False


class EspecieCreateView(ValidatePermissionRequiredMixin, CreateView):
    model = Especie
    form_class = EspecieForm
    template_name = 'especie/create.html'
    success_url = reverse_lazy('especie_list')
    url_redirect = success_url
    permission_required = 'add_especie'

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
        context['title'] = 'Creación de un Especie'
        context['entity'] = 'Especie'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context
    def test_func(self):
        # obtenemos todos los grupos del usuario logueado
        grupos = self.request.user.groups.all()
        # comparamos que el usuario pertenezca al grupo VENDEDOR o SUPERVISOR
        for grupo in grupos:
            if grupo in ['Post-Cosecha ', 'Admin']:
                return True
        return False


class EspecieUpdateView(ValidatePermissionRequiredMixin, UpdateView):
    model = Especie
    form_class = EspecieForm
    template_name = 'especie/create.html'
    success_url = reverse_lazy('especie_list')
    url_redirect = success_url
    permission_required = 'change_especie'

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
        context['title'] = 'Edición una Especie'
        context['entity'] = 'Especie'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context
    def test_func(self):
        # obtenemos todos los grupos del usuario logueado
        grupos = self.request.user.groups.all()
        # comparamos que el usuario pertenezca al grupo VENDEDOR o SUPERVISOR
        for grupo in grupos:
            if grupo in ['Post-Cosecha ', 'Admin']:
                return True
        return False


class EspecieDeleteView(ValidatePermissionRequiredMixin, DeleteView):
    model = Especie
    template_name = 'especie/delete.html'
    success_url = reverse_lazy('especie_list')
    url_redirect = success_url
    permission_required = 'delete_especie'

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
        context['title'] = 'Eliminación de una Especie'
        context['entity'] = 'Especie'
        context['list_url'] = self.success_url
        return context
    def test_func(self):
        # obtenemos todos los grupos del usuario logueado
        grupos = self.request.user.groups.all()
        # comparamos que el usuario pertenezca al grupo VENDEDOR o SUPERVISOR
        for grupo in grupos:
            if grupo in ['Post-Cosecha ', 'Admin']:
                return True
        return False
