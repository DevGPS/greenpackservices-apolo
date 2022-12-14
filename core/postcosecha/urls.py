from django.urls import path

# aqui debo exportar los views
from core.postcosecha.views.transporte.views import *
from core.postcosecha.views.exportadora.views import *
from core.postcosecha.views.especie.views import *
from core.postcosecha.views.variedad.views import *
from core.postcosecha.views.productor.views import *
from core.postcosecha.views.formCereza.views import *
from core.postcosecha.views.formCereza import views




urlpatterns = [
   
    # transporte
    path('transporte/', TransporteListView.as_view(), name='transporte_list'),
    path('transporte/add/', TransporteCreateView.as_view(), name='transporte_create'),
    path('transporte/update/<int:pk>/', TransporteUpdateView.as_view(), name='transporte_update'),
    path('transporte/delete/<int:pk>/', TransporteDeleteView.as_view(), name='transporte_delete'),
    # Exportadora
    path('exportadora/', ExportadoraListView.as_view(), name='exportadora_list'),
    path('exportadora/add/', ExportadoraCreateView.as_view(), name='exportadora_create'),
    path('exportadora/update/<int:pk>/', ExportadoraUpdateView.as_view(), name='exportadora_update'),
    path('exportadora/delete/<int:pk>/', ExportadoraDeleteView.as_view(), name='exportadora_delete'),
     # Especies
    path('especie/', EspecieListView.as_view(), name='especie_list'),
    path('especie/add/', EspecieCreateView.as_view(), name='especie_create'),
    path('especie/update/<int:pk>/', EspecieUpdateView.as_view(), name='especie_update'),
    path('especie/delete/<int:pk>/', EspecieDeleteView.as_view(), name='especie_delete'),
     # Variedades
    path('variedad/', VariedadListView.as_view(), name='variedad_list'),
    path('variedad/add/', VariedadCreateView.as_view(), name='variedad_create'),
    path('variedad/update/<int:pk>/', VariedadUpdateView.as_view(), name='variedad_update'),
    path('variedad/delete/<int:pk>/', VariedadDeleteView.as_view(), name='variedad_delete'),
     # Productores
    path('productor/', ProductorListView.as_view(), name='productor_list'),
    path('productor/add/', ProductorCreateView.as_view(), name='productor_create'),
    path('productor/update/<int:pk>/', ProductorUpdateView.as_view(), name='productor_update'),
    path('productor/delete/<int:pk>/', ProductorDeleteView.as_view(), name='productor_delete'),


    path('form_cereza/', views.FormCerezaListView, name='formCereza_list'),
    path('create_form_cereza/add/',formCerezaCreateView.as_view(), name='formCereza_create'),
    path('delete_form_cereza/<int:pk>/', FormCerezaDeleteView.as_view(), name='formCereza_delete'),
    path('update_form_cereza/<int:pk>/', FormCerezaUpdateView.as_view(), name='formCereza_update'),
    
    # path('delete_form_cereza/<int:pk>/', FormCerezaDeleteView.as_view(), name='formCereza_delete'),
    # path('update_form_cereza/<int:pk>/', FormCerezaUpdateView.as_view(), name='formCereza_update'),


    path('report-list-cereza/',FormCerezaPdf.as_view(),name='pdf-list-cereza'),
    path('report-lote-cereza/<int:pk>/', CerezaPdfView.as_view(), name='report-lote-cereza'),

    # path('report-lote-cereza/<Lote>/',views.PDF_form_cereza,name='report-lote-cereza'),

     
   
]
