from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.contenedor.forms import TransporteForm
from core.pos.mixins import ValidatePermissionRequiredMixin
from core.contenedor.models import Transporte


class TransporteListView(ValidatePermissionRequiredMixin, ListView):
    model = Transporte
    template_name = 'transporte/list.html'
    permission_required = 'view_transporte'
    url_redirect = reverse_lazy('dashboard')

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search':
                data = []
                for i in Transporte.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Transportes'
        context['create_url'] = reverse_lazy('transporte_create')
        context['list_url'] = reverse_lazy('transporte_list')
        context['entity'] = 'Transporte'
        return context


class TransporteCreateView(ValidatePermissionRequiredMixin, CreateView):
    model = Transporte
    form_class = TransporteForm
    template_name = 'transporte/create.html'
    success_url = reverse_lazy('transporte_list')
    url_redirect = success_url
    permission_required = 'add_transporte'

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
        context['title'] = 'Creación de un Transporte'
        context['entity'] = 'Transporte'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class TransporteUpdateView(ValidatePermissionRequiredMixin, UpdateView):
    model = Transporte
    form_class = TransporteForm
    template_name = 'transporte/create.html'
    success_url = reverse_lazy('transporte_list')
    url_redirect = success_url
    permission_required = 'change_transporte'

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
        context['title'] = 'Edición una Transporte'
        context['entity'] = 'Transporte'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class TransporteDeleteView(ValidatePermissionRequiredMixin, DeleteView):
    model = Transporte
    template_name = 'transporte/delete.html'
    success_url = reverse_lazy('transporte_list')
    url_redirect = success_url
    permission_required = 'delete_transporte'

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
        context['title'] = 'Eliminación de una Transporte'
        context['entity'] = 'Transporte'
        context['list_url'] = self.success_url
        return context

# class CategoryListView(ValidatePermissionRequiredMixin, ListView):
#     model = Category
#     template_name = 'category/list.html'
#     permission_required = 'view_category'
#     url_redirect = reverse_lazy('dashboard')

#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             action = request.POST['action']
#             if action == 'search':
#                 data = []
#                 for i in Category.objects.all():
#                     data.append(i.toJSON())
#             else:
#                 data['error'] = 'Ha ocurrido un error'
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data, safe=False)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Listado de Categorías'
#         context['create_url'] = reverse_lazy('category_create')
#         context['list_url'] = reverse_lazy('category_list')
#         context['entity'] = 'Categorias'
#         return context


# class CategoryCreateView(ValidatePermissionRequiredMixin, CreateView):
#     model = Category
#     form_class = CategoryForm
#     template_name = 'category/create.html'
#     success_url = reverse_lazy('category_list')
#     url_redirect = success_url
#     permission_required = 'add_category'

#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             action = request.POST['action']
#             if action == 'add':
#                 form = self.get_form()
#                 data = form.save()
#             else:
#                 data['error'] = 'No ha ingresado a ninguna opción'
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Creación una Categoria'
#         context['entity'] = 'Categorias'
#         context['list_url'] = self.success_url
#         context['action'] = 'add'
#         return context


# class CategoryUpdateView(ValidatePermissionRequiredMixin, UpdateView):
#     model = Category
#     form_class = CategoryForm
#     template_name = 'category/create.html'
#     success_url = reverse_lazy('category_list')
#     url_redirect = success_url
#     permission_required = 'change_category'

#     def dispatch(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return super().dispatch(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             action = request.POST['action']
#             if action == 'edit':
#                 form = self.get_form()
#                 data = form.save()
#             else:
#                 data['error'] = 'No ha ingresado a ninguna opción'
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Edición una Categoria'
#         context['entity'] = 'Categorias'
#         context['list_url'] = self.success_url
#         context['action'] = 'edit'
#         return context


# class CategoryDeleteView(ValidatePermissionRequiredMixin, DeleteView):
#     model = Category
#     template_name = 'category/delete.html'
#     success_url = reverse_lazy('category_list')
#     url_redirect = success_url
#     permission_required = 'delete_category'

#     def dispatch(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         return super().dispatch(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         data = {}
#         try:
#             self.object.delete()
#         except Exception as e:
#             data['error'] = str(e)
#         return JsonResponse(data)

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Eliminación de una Categoria'
#         context['entity'] = 'Categorias'
#         context['list_url'] = self.success_url
#         return context
