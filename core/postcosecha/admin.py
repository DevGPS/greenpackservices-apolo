from django.contrib import admin
from core.postcosecha.models import *

# Register your models here.
class TemporadasAdmin(admin.ModelAdmin):
    list_display = ("codigo","nombre",)
    list_filter = ("nombre",)
    readonly_fields = ('created_at', 'updated_at')

class ExportadoraAdmin(admin.ModelAdmin):
    list_display = ("codigo","nombre", "telefono", "email")
    search_fields = ("nombre", "email")
    list_filter = ("nombre", "email",)
    readonly_fields = ('created_at', 'updated_at')


class ProductorAdmin(admin.ModelAdmin):
    list_display = ("codigo","nombre", "CSG", "telefono", "email")
    search_fields = ("nombre", "CSG")
    list_filter = ("nombre", "email",)
    readonly_fields = ('created_at', 'updated_at')


class TransporteAdmin(admin.ModelAdmin):
    list_display = ("codigo","nombres", "rut", "patente1", "patente2")
    search_fields = ("nombres", "patente1")
    list_filter = ("nombres", "rut",)
    readonly_fields = ('created_at', 'updated_at')
    

class VariedadAdmin(admin.ModelAdmin):
    list_display = ("codigo","nombre", "especie")
    search_fields = ("nombre", "especie")
    list_filter = ("especie",)
    readonly_fields = ('created_at', 'updated_at')

class PrincipalAdmin(admin.ModelAdmin):
    list_display = ("Lote", "Fecha_Recepcion","PrecalibreTot", "CalidadTotal","CondicionTotal","TotalExportable")
    search_fields = ("Lote", "Fecha_Recepcion", "Nguia")
    list_filter = ("Fecha_Recepcion", "productor", "variedad",)
    date_hierarchy = ("Fecha_Recepcion")
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(FormCerezaModels, PrincipalAdmin)
admin.site.register(Exportadora, ExportadoraAdmin)
admin.site.register(Productor, ProductorAdmin)
admin.site.register(Especie)
admin.site.register(Variedad, VariedadAdmin)
admin.site.register(Transporte, TransporteAdmin)
admin.site.register(Temporada, TemporadasAdmin)

