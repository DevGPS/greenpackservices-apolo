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


TIPO_TRANSPORTE = (
    ('T', 'TERMO'),
    ('C', 'CONTAINER'),
)

TIPO_ENVASE = (
    ('T', 'TOTEM'),
    ('B', 'BINS'),
)
CALIBRES = (
    ('L', 'L'),
    ('XL', 'XL'),
    ('J', 'J'),
    ('2J', '2J'),
    ('3J', '3J'),
    ('4J', '4J'),

)


class Exportadora(models.Model):
    codigo = models.CharField(max_length=70, unique=True)
    nombre_FTS = models.CharField(max_length=70)
    nombre = models.CharField(max_length=70, unique=True)
    direccion = models.CharField(max_length=70)
    telefono = models.CharField(max_length=20, null=True)
    email = models.EmailField(max_length=70)
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE)
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
        return '{} / {}'.format(self.patente1, self.patente2) 

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Transporte'
        verbose_name_plural = 'Transportes'
        ordering = ['id']

class Productor(models.Model):
    codigo = models.CharField(max_length=70, unique=True)
    nombre_FTS = models.CharField(max_length=70)
    nombre = models.CharField(max_length=70, unique=True)
    CSG = models.IntegerField(null=False, unique=True)
    direccion = models.CharField(max_length=70, null=True)
    telefono = models.PositiveIntegerField(null=True)
    email = models.EmailField(max_length=70,)
    exportadora = models.ForeignKey(Exportadora, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.nombre_FTS) 

    def toJSON(self):
        item = model_to_dict(self)
        return item
    class Meta:
        verbose_name = 'Productor'
        verbose_name_plural = 'Productores'

    

class Especie(models.Model):
    codigo = models.CharField(max_length=70, unique=True)
    nombre = models.CharField(max_length=70, unique=True)
    temporada = models.ForeignKey(Temporada, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}'.format(self.nombre) 

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
        return '{} / {}'.format(self.nombre,self.especie) 

    def toJSON(self):
        item = model_to_dict(self)
        return item
    class Meta:
        verbose_name = 'Variedad'
        verbose_name_plural = 'Variedades'

    



class FormCerezaModels(models.Model):
    #principal
    Lote = models.PositiveIntegerField(primary_key=True)
    productor = models.ForeignKey(Productor, on_delete=models.CASCADE)
    variedad = models.ForeignKey(Variedad,on_delete=models.CASCADE)
    Fecha_Recepcion = models.DateField()
    Hora_Recepcion = models.TimeField()
    Hora_Analisis = models.TimeField()
    Tmin = models.PositiveIntegerField(verbose_name='T° Minima')
    Tmax = models.PositiveIntegerField(verbose_name='T° Maxima')
    Tip_Trans = models.CharField(
        max_length=55, choices=TIPO_TRANSPORTE, default='Terrestre', verbose_name='Tipo Transporte')
    Nguia = models.PositiveIntegerField(verbose_name='N° Guia')
    transporte = models.ForeignKey(Transporte,on_delete=models.CASCADE)
    Tip_Env = models.CharField(
        max_length=55, choices=TIPO_ENVASE, default='Envase1', verbose_name='Tipo Envase')
    NEnv = models.PositiveIntegerField(verbose_name='N° Envases')
    KNeto = models.FloatField(verbose_name='Kilos Netos')
    NFruto = models.PositiveIntegerField(default=100, verbose_name='N° Frutos Muestra') 
    Hidro = models.BooleanField(default=True) 
    observaciones = models.TextField(max_length=1000, blank=True,null=True)
    #Distribucion por Calibre
    PC = models.PositiveIntegerField(default=0)
    L = models.PositiveIntegerField(default=0)
    XL = models.PositiveIntegerField(default=0)
    J = models.PositiveIntegerField(default=0)
    J2 = models.PositiveIntegerField(default=0)
    J3 = models.PositiveIntegerField(default=0)
    J4 = models.PositiveIntegerField(default=0)
    #Distribucion Color
    Rojo = models.PositiveIntegerField(default=0)
    RojoCaoba = models.PositiveIntegerField(default=0)
    Caoba = models.PositiveIntegerField(default=0)
    CaobaOscuro = models.PositiveIntegerField(default=0)
    Negro = models.PositiveIntegerField(default=0)    
    #Distribucion FirmPro
    Blando = models.PositiveIntegerField(default=0)
    Sensible = models.PositiveIntegerField(default=0)
    Firme = models.PositiveIntegerField(default=0)
    MuyFirme = models.PositiveIntegerField(default=0)
    FP_L = models.PositiveIntegerField(default=0)
    FP_XL = models.PositiveIntegerField(default=0)
    FP_J = models.PositiveIntegerField(default=0)
    FP_J2 = models.PositiveIntegerField(default=0)
    FP_J3 = models.PositiveIntegerField(default=0)
    FP_J4 = models.PositiveIntegerField(default=0)
    FPProm = models.FloatField(default=0)
    #Distribucion Analisis de Masa
    CalibreLight = models.CharField(
        max_length=55, choices=CALIBRES, default='-', verbose_name='Calibre Light')
    C1F1 = models.FloatField(default=0, max_length=3)
    C1F2 = models.FloatField(default=0, max_length=3)
    C1F3 = models.FloatField(default=0, max_length=3)
    C1F4 = models.FloatField(default=0, max_length=3)
    C1F5 = models.FloatField(default=0, max_length=3)
    CalibreDark = models.CharField(
        max_length=55, choices=CALIBRES, default='-', verbose_name='Calibre Dark')
    C2F1 = models.FloatField(default=0, max_length=3)
    C2F2 = models.FloatField(default=0, max_length=3)
    C2F3 = models.FloatField(default=0, max_length=3)
    C2F4 = models.FloatField(default=0, max_length=3)
    C2F5 = models.FloatField(default=0, max_length=3)
    PromMasa1 = models.FloatField(default=0)
    PromMasa2 = models.FloatField(default=0)      
    #Distribucion Solido Soluble
    ssLL = models.FloatField(default=0)
    ssXLL = models.FloatField(default=0)
    ssJL = models.FloatField(default=0)
    ss2JL = models.FloatField(default=0)
    ss3JL = models.FloatField(default=0)
    ss4JL = models.FloatField(default=0)
    ssLD = models.FloatField(default=0)
    ssXLD = models.FloatField(default=0)
    ssJD = models.FloatField(default=0)
    ss2JD = models.FloatField(default=0)
    ss3JD = models.FloatField(default=0)
    ss4JD = models.FloatField(default=0)
    PromLight = models.FloatField(default=0)
    PromDark = models.FloatField(default=0)
    #Cereza_DefCalidad
    DInsecto = models.PositiveIntegerField(default=0)#
    DTrips = models.PositiveIntegerField(default=0)#
    FaltaColor = models.PositiveIntegerField(default=0)#
    FrutoDeforme = models.PositiveIntegerField(default=0)#
    FrutoDoble = models.PositiveIntegerField(default=0)#
    SinPedicelo = models.PositiveIntegerField(default=0)#
    GuataBlanca = models.PositiveIntegerField(default=0)#
    HeridaCicatrizada = models.PositiveIntegerField(default=0)#
    Hijuelo = models.PositiveIntegerField(default=0)#
    Manchas = models.PositiveIntegerField(default=0)#
    Medialuna = models.PositiveIntegerField(default=0)#
    MezclaVariedad = models.PositiveIntegerField(default=0)#
    Roce = models.PositiveIntegerField(default=0)#
    Russet = models.PositiveIntegerField(default=0)# 
    RestosFlorales = models.PositiveIntegerField(default=0) #
    PielLagarto = models.PositiveIntegerField(default=0) #
    GolpeSol = models.PositiveIntegerField(default=0) #
    ResiduoProducto = models.PositiveIntegerField(default=0) #
    TotCalidad = models.FloatField(default=0)
    #Cereza_DefCondicion
    Adhesion = models.PositiveIntegerField(default=0)#
    DPajaro = models.PositiveIntegerField(default=0)#
    DepresionSevera = models.PositiveIntegerField(default=0)#
    FrutoBlando = models.PositiveIntegerField(default=0)#
    FrutoDeshidratado = models.PositiveIntegerField(default=0)
    HeridaAbierta = models.PositiveIntegerField(default=0)#
    Machucon = models.PositiveIntegerField(default=0)#
    ManchaPudricion = models.PositiveIntegerField(default=0)#
    Partidura = models.PositiveIntegerField(default=0)#
    PartiduraApical = models.PositiveIntegerField(default=0)#
    PediceloDeshidratado = models.PositiveIntegerField(default=0)#
    PittingPunteadura = models.PositiveIntegerField(default=0)#
    Pudricion = models.PositiveIntegerField(default=0)#
    Sobremadurez = models.PositiveIntegerField(default=0)#
    SuturaAbierta = models.PositiveIntegerField(default=0)#
    DescarroPedicelar = models.PositiveIntegerField(default=0)#
    PartiduraBasal = models.PositiveIntegerField(default=0)#
    TotCondicion = models.FloatField(default=0)   
    #Resultados
    PrecalibreTot = models.FloatField(default=0)
    CalidadTotal = models.FloatField(default=0)
    CondicionTotal = models.FloatField(default=0)
    TotalExportable = models.FloatField(default=0)
    images1 = models.ImageField(upload_to='report-cerezas/%Y/%m/%d/', null=True, blank=True)
    images2 = models.ImageField(upload_to='report-cerezas/%Y/%m/%d/', null=True, blank=True)
    images3 = models.ImageField(upload_to='report-cerezas/%Y/%m/%d/', null=True, blank=True)
    images4 = models.ImageField(upload_to='report-cerezas/%Y/%m/%d/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)       
    

    def __str__(self):
        return '{} / {}'.format(self.Lote,self.variedad) 

    def toJSON(self):
        item = model_to_dict(self)
        return item
    
    class Meta:
        verbose_name = 'Formulario Cereza'
        verbose_name_plural = 'Formulario Cerezas'
    