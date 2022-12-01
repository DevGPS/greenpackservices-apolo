from django.db import models
from django.forms import model_to_dict
from core.contenedor.models import Temporada


class Ubicacion(models.Model):
    # codigo = models.CharField(max_length=70, unique=True)
    nombre = models.CharField(max_length=70, unique=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '{}'.format(self.nombre_FTS) 


    def __str__(self):
            return '{}'.format(self.nombre)       

    def toJSON(self):
            item = model_to_dict(self)
            return item

    class Meta:
            verbose_name = 'Ubicacion'
            verbose_name_plural = 'Ubicaciones'      


class Equipo(models.Model):
    # codigo = models.CharField(max_length=70, unique=True)
    nombre = models.CharField(max_length=100)   
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.nombre) 

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        ordering = ['id']

class Labor(models.Model):
    # codigo = models.CharField(max_length=70, unique=True)   
    nombre = models.CharField(max_length=70, unique=True)    
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.nombre) 

    def toJSON(self):
        item = model_to_dict(self)
        return item
    class Meta:
        verbose_name = 'Labor'
        verbose_name_plural = 'Labores'

    

class Trabajador(models.Model):
    nombre = models.CharField(max_length=70, unique=True)
    apellido = models.CharField(max_length=70, unique=True)  
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.nombre) 

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Trabajador'
        verbose_name_plural = 'Trabajadores'

    



