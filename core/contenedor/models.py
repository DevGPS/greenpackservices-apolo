from django.db import models
from django.forms import model_to_dict

class Temporada(models.Model):
    codigo = models.CharField(max_length=70, unique=True)
    nombre = models.CharField(max_length=70, unique=True)
    nombre_sec = models.CharField(max_length=70, unique=True)  

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
            return '{}'.format(self.nombre)       

    def toJSON(self):
            item = model_to_dict(self)
            return item

    class Meta:
            verbose_name = 'Temporada'
            verbose_name_plural = 'Temporadas'

class Exportadora(models.Model):
    codigo = models.CharField(max_length=70, unique=True)
    nombre = models.CharField(max_length=70, unique=True)
    direccion = models.CharField(max_length=70)
    telefono = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=70)
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
            return '{}'.format(self.nombre)       

    def toJSON(self):
            item = model_to_dict(self)
            return item

    class Meta:
            verbose_name = 'Exportadora'
            verbose_name_plural = 'Exportadoras'      


class Transporte(models.Model):
    codigo = models.CharField(max_length=70, unique=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    rut = models.CharField(max_length=13, unique=True)
    patente1 = models.CharField(max_length=10, null=True, unique=True)
    patente2 = models.CharField(max_length=10, null=True, unique=True)
    telefono = models.PositiveIntegerField(null=True)
    exportadora = models.ForeignKey(Exportadora, on_delete=models.CASCADE, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}/{}'.format(self.patente1, self.patente2) 

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Transporte'
        verbose_name_plural = 'Transportes'
        ordering = ['id']

class Productor(models.Model):
    codigo = models.CharField(max_length=70, unique=True)
    nombre = models.CharField(max_length=70, unique=True)
    CSG = models.IntegerField(null=False, unique=True)
    direccion = models.CharField(max_length=70, null=True)
    telefono = models.PositiveIntegerField(null=True)
    email = models.EmailField(max_length=70,)
    exportadora = models.ForeignKey(Exportadora, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}/{}'.format(self.codigo, self.nombre) 

    def toJSON(self):
        item = model_to_dict(self)
        return item
    class Meta:
        verbose_name = 'Productor'
        verbose_name_plural = 'Productores'

    

class Especie(models.Model):
    codigo = models.CharField(max_length=70, unique=True)
    nombre = models.CharField(max_length=70, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}/{}'.format(self.codigo, self.nombre) 

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Especie'
        verbose_name_plural = 'Especies'

    

class Variedad(models.Model):
    codigo = models.CharField(max_length=70, unique=True)
    nombre = models.CharField(max_length=70, unique=True)
    especie = models.ForeignKey(Especie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}/{}'.format(self.codigo, self.nombre) 

    def toJSON(self):
        item = model_to_dict(self)
        return item
    class Meta:
        verbose_name = 'Variedad'
        verbose_name_plural = 'Variedades'

    


