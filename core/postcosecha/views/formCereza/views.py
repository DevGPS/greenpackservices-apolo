from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView,View
from django.conf import settings
import os
from core.postcosecha.forms import CerezaForm
from core.postcosecha.models import *
from core.postcosecha.utils import render_to_pdf

from core.pos.mixins import ValidatePermissionRequiredMixin

from datetime import datetime

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from django.template.loader import get_template
from xhtml2pdf import pisa
from django.shortcuts import render



class formCerezaCreateView(ValidatePermissionRequiredMixin, CreateView):
    model = FormCerezaModels
    form_class = CerezaForm
    template_name = 'formCereza/create.html'
    success_url = reverse_lazy('formCereza_list')
    url_redirect = success_url
    permission_required = 'add_formCereza'    

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
            elif action == 'search_productor_id':
                data = [{'id': '', 'text': '--Productores Cargados--'}]
                for i in Productor.objects.filter(exportadora_id=request.POST['id']):
                    data.append({'id': i.id, 'text': i.nombre,'data': i.exportadora.toJSON()})

            elif action == 'search_transporte_id':
                data = [{'id': '', 'text': '--Camiones Cargados--'}]
                for i in Transporte.objects.filter(exportadora_id=request.POST['id']):
                    data.append({'id': i.id, 'text': i.patente1,'data': i.exportadora.toJSON()})

            elif action == 'search_variedad_id':
                data = [{'id': '', 'text': '--Variedades Cargadas--'}]
                for i in Variedad.objects.filter(especie_id=request.POST['id']):
                    data.append({'id': i.id, 'text': i.nombre,'data': i.especie.toJSON()})
            else:
                data['error'] = 'No ha ingresado a ninguna opción'               

        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Registro de Cerezas'
        context['entity'] = 'FormCerezaModels'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context
    
def FormCerezaListView(request):    
    registros = FormCerezaModels.objects.all()
    return render(request, "formCereza/list.html", {"registros": registros})

        


class FormCerezaUpdateView(ValidatePermissionRequiredMixin, UpdateView):
    model = FormCerezaModels
    form_class = CerezaForm
    template_name = 'formCereza/update.html'
    success_url = reverse_lazy('formCereza_list')
    url_redirect = success_url
    permission_required = 'change_formCereza'

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
        context['title'] = 'Edición una Registro de Cerezas'
        context['entity'] = 'FormCerezaModels'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class FormCerezaDeleteView(ValidatePermissionRequiredMixin, DeleteView):
    model = FormCerezaModels
    template_name = 'formCereza/delete.html'
    success_url = reverse_lazy('formCereza_list')
    url_redirect = success_url
    permission_required = 'delete_formCereza'

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
        context['title'] = 'Eliminación de un Registro de Cerezas'
        context['entity'] = 'FormCerezaModels'
        context['list_url'] = self.success_url
        return context


class FormCerezaPdf(View):
    def get(self, request, *args, **kwargs):
        registros = FormCerezaModels.objects.all()
        fecha = datetime.now()
        data = {
            'fecha': fecha,
            'registros': registros
        }
        pdf = render_to_pdf(
            'formCereza/report-cereza/report-list-cereza.html', data)
        return HttpResponse(pdf, content_type='application/pdf')


class CerezaPdfView(View):

    def link_callback(self, uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        # use short variable names
        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /static/media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    def get(self, request, *args, **kwargs):
        try:
            fecha = datetime.now()
            template = get_template('formCereza/report-cereza/report-lote-cereza.html')
            context = {
                'fecha': fecha,
                'registros': FormCerezaModels.objects.get(pk=self.kwargs['pk']),
                'icon': '{}{}'.format(settings.MEDIA_URL, 'logo.png')
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisaStatus = pisa.CreatePDF(
                html, dest=response,
                link_callback=self.link_callback
            )
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('formCereza_list'))
