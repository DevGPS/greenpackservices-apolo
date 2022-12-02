from django.urls import path

# aqui debo exportar los views
from core.sadema.views.ubicacion.views import *
from core.sadema.views.equipo.views import *
from core.sadema.views.labor.views import *
from core.sadema.views.trabajador.views import *
from core.sadema.views.registro.views import *



urlpatterns = [
   
    # Ubicaciones
    path('ubicacion/', UbicacionListView.as_view(), name='ubicacion_list'),
    path('ubicacion/add/', UbicacionCreateView.as_view(), name='ubicacion_create'),
    path('ubicacion/update/<int:pk>/', UbicacionUpdateView.as_view(), name='ubicacion_update'),
    path('ubicacion/delete/<int:pk>/', UbicacionDeleteView.as_view(), name='ubicacion_delete'),
    # Equipos
    path('equipo/', EquipoListView.as_view(), name='equipo_list'),
    path('equipo/add/', EquipoCreateView.as_view(), name='equipo_create'),
    path('equipo/update/<int:pk>/', EquipoUpdateView.as_view(), name='equipo_update'),
    path('equipo/delete/<int:pk>/', EquipoDeleteView.as_view(), name='equipo_delete'),
     # Labores
    path('labor/', LaborListView.as_view(), name='labor_list'),
    path('labor/add/', LaborCreateView.as_view(), name='labor_create'),
    path('labor/update/<int:pk>/', LaborUpdateView.as_view(), name='labor_update'),
    path('labor/delete/<int:pk>/', LaborDeleteView.as_view(), name='labor_delete'),
     # Trabajadores
    path('trabajador/', TrabajadorListView.as_view(), name='trabajador_list'),
    path('trabajador/add/', TrabajadorCreateView.as_view(), name='trabajador_create'),
    path('trabajador/update/<int:pk>/', TrabajadorUpdateView.as_view(), name='trabajador_update'),
    path('trabajador/delete/<int:pk>/', TrabajadorDeleteView.as_view(), name='trabajador_delete'),

     # Registros
    path('registro/', RegistroListView.as_view(), name='registro_list'),
    path('registro/add/', RegistroCreateView.as_view(), name='registro_create'),
    path('registro/update/<int:pk>/', RegistroUpdateView.as_view(), name='registro_update'),
    path('registro/delete/<int:pk>/', RegistroDeleteView.as_view(), name='registro_delete'),
    
   
]
