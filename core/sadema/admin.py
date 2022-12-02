from django.contrib import admin

from core.sadema.models import *

# Register your models here.
class UbicacionAdmin(admin.ModelAdmin):
    list_display = ("nombre",)
    list_filter = ("nombre",)
    readonly_fields = ('created_at', 'updated_at')

class EquipoaAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


class LaborAdmin(admin.ModelAdmin):
    list_filter = ("nombre",)
    readonly_fields = ('created_at', 'updated_at')


class TranajadoreAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

class RegistroAdmin(admin.ModelAdmin):
    list_display = ("ubicacion","equipo", "labor", "trabajador")
    search_fields = ("fecha", "ubicacion","trabajador")
    list_filter = ("fecha", "ubicacion","trabajador")
    readonly_fields = ('created_at', 'updated_at')
    

admin.site.register(Ubicacion, UbicacionAdmin)
admin.site.register(Equipo, EquipoaAdmin)
admin.site.register(Labor, LaborAdmin)
admin.site.register(Trabajador,TranajadoreAdmin)
admin.site.register(Registro,RegistroAdmin)

