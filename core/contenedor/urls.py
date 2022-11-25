from django.urls import path

# aqui debo exportar los views
from core.contenedor.views.transporte.views import *
from core.contenedor.views.exportadora.views import *

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
   
]
