from django.contrib import admin

from core.cerezas.models import FormCerezaModels


class PrincipalAdmin(admin.ModelAdmin):
    list_display = ("Lote", "Fecha_Recepcion","PrecalibreTot", "CalidadTotal","CondicionTotal","TotalExportable")
    search_fields = ("Lote", "Fecha_Recepcion", "Nguia")
    list_filter = ("Fecha_Recepcion", "Productor", "Variedad",)
    date_hierarchy = ("Fecha_Recepcion")
    readonly_fields = ('created_at', 'updated_at')



admin.site.register(FormCerezaModels, PrincipalAdmin)

