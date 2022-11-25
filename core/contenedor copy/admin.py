from django.contrib import admin
from core.contenedor.models import *

# Register your models here.
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




admin.site.register(Exportadora, ExportadoraAdmin)
admin.site.register(Productor, ProductorAdmin)
admin.site.register(Especie)
admin.site.register(Variedad, VariedadAdmin)
admin.site.register(Transporte, TransporteAdmin)
