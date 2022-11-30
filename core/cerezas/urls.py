# URLS POSTCOSECHA
from django.urls import path
from core.cerezas import views
from core.cerezas.views import TestView


urlpatterns = [
    path('read_form_cereza/', views.read_form_cereza, name='read_cerezas'),
    # path('formulario_recepcion/', views.create_form_cereza, name='create_cerezas'),
    path('delete_form_cereza/<Lote>/', views.delete_form_cereza, name='delete_form_cereza'),
    path('update_form_cereza/<Lote>/', views.update_form_cereza, name='update_form_cereza'),


    path('report-list-cereza/',views.FormCerezaPdf.as_view(),name='pdf-list-cereza'),
    path('report-lote-cereza/<Lote>/',views.PDF_form_cereza,name='report-lote-cereza'),
    path('formulario_recepcion/', TestView.as_view(), name='create_cerezas'),
    path('test/', TestView.as_view(), name='test'),


]
