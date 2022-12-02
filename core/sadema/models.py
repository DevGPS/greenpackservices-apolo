from django.db import models
from django.forms import model_to_dict


class Ubicacion(models.Model):
    
    nombre = models.CharField(max_length=70, unique=True)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)    
    
    def __str__(self):
        return '{}'.format(self.nombre)       

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
            verbose_name = 'Ubicacion'
            verbose_name_plural = 'Ubicaciones'      


class Equipo(models.Model):
    
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

class Registro(models.Model):
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)    
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    labor = models.ForeignKey(Labor, on_delete=models.CASCADE)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    observaciones = models.TextField(max_length=1000, blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.trabajador) 

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Registro de Tarea'
        verbose_name_plural = 'Registro de Tareas'

    



