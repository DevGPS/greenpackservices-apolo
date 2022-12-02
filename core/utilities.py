import random
from random import randint

from config import wsgi
import json
from core.postcosecha.models import *
from core.user.models import User

user = User()
user.username = 'saraya'
user.first_name = 'Sebastian Alejandro'
user.last_name = 'Araya Torres'
user.email = 'sebastian.araya@greenps.cl'
user.set_password('Seba0017')
user.is_superuser = True
user.is_staff = True
user.save()
print('Usuario SARAYA creado correctamente')


temp = Temporada()
temp.codigo = 'T11'
temp.nombre = 'Temp. 11'
temp.nombre_sec = 'Temp. 2022/2023'
temp.save()
print('Temporada 11 creada correctamente')


#id1
exportadora = Exportadora()
exportadora.codigo = 'C&D'
exportadora.nombre = 'CYD COMERCIO Y DESARROLLO INTERNACIONAL S.A.'
exportadora.nombre_FTS = 'C&D'
exportadora.direccion = 'LAS CONDES s/n'
exportadora.telefono = '0979014552'
exportadora.email = 'contacto@cyd.cl'
exportadora.temporada = Temporada(pk=1) 
exportadora.save()
print('Exportadora C&D creado correctamente')

#id2
exportadora = Exportadora()
exportadora.codigo = 'ELMO'
exportadora.nombre = 'AGRICOLA EL MOLINO LTDA.'
exportadora.nombre_FTS = 'EL MOLINO'
exportadora.direccion = 'FUNDO SAN FELIPE LA ESTACADA'
exportadora.telefono = '0979014552'
exportadora.email = 'contacto@elmolino.cl'
exportadora.temporada = Temporada(pk=1) 
exportadora.save()
print('Exportadora EL MOLINO creado correctamente')

#id3
exportadora = Exportadora()
exportadora.codigo = 'GA'
exportadora.nombre = 'SOCIEDAD AGRICOLA GREEN AGRO LIMITADA'
exportadora.nombre_FTS = 'GREEN AGRO '
exportadora.direccion = 'PARCELA 12 SAN PEDRO LOTE 4'
exportadora.telefono = '0979014552'
exportadora.email = 'INFORMATICA@GREENPS.CL'
exportadora.temporada = Temporada(pk=1) 
exportadora.save()
print('Exportadora GREEN AGRO creado correctamente')

#id4
exportadora = Exportadora()
exportadora.codigo = 'CHIL'
exportadora.nombre = 'SERVICIOS CHILFRESH LTDA.'
exportadora.nombre_FTS = 'CHILFRESH'
exportadora.direccion = 'CAMINO ZAPALLAR KM  0.6  CURICO'
exportadora.telefono = '0979014552'
exportadora.email = 'CONTACTO@CHIL.CL'
exportadora.temporada = Temporada(pk=1) 
exportadora.save()
print('Exportadora CHILFRESH creado correctamente')

#id5
exportadora = Exportadora()
exportadora.codigo = 'FRU'
exportadora.nombre = 'FRUTAS DE EXPORTACION SPA.'
exportadora.nombre_FTS = 'FRUTEXA '
exportadora.direccion = 'AVENIDA LUIS PASTEUR 5280, OF 403 VITACURA SANTIAG0'
exportadora.telefono = '0979014552'
exportadora.email = 'CONTACTO@FRUTEXA.CL'
exportadora.temporada = Temporada(pk=1) 
exportadora.save()
print('Exportadora FRUTEXA creado correctamente')

#id6
exportadora = Exportadora()
exportadora.codigo = 'RAN'
exportadora.nombre = 'EXPORTADORA RANCAGUA SA.'
exportadora.nombre_FTS = 'RANCO'
exportadora.direccion = 'RUTA 5 SUR 04000'
exportadora.telefono = '0979014552'
exportadora.email = 'CONTACTO@ranco.CL'
exportadora.temporada = Temporada(pk=1) 
exportadora.save()
print('Exportadora RANCO creado correctamente')



# PRODUCTORES
productor = Productor()
productor.codigo = 'ARKA'
productor.nombre_FTS = 'SOCIEDAD AGRICOLA ARKA SPA'
productor.nombre = 'SOCIEDAD AGRICOLA ARKA SPA'
productor.CSG = '106237'
productor.direccion = 'HIJUELA LAS MERCEDES S/N'
productor.telefono = '979014552'
productor.email = 'CONTACTO@ARKA.CL'
productor.exportadora = Exportadora(pk=4) 
productor.save()
print('Productor ARKA creado correctamente')

productor = Productor()
productor.codigo = 'SIG'
productor.nombre_FTS = 'SAN IGNACIO'
productor.nombre = 'AGRICOLA SAN IGNACIO LTDA'
productor.CSG = '100174'
productor.direccion = 'Direccion no Especificada'
productor.telefono = '979014552'
productor.email = 'CONTACTO@SIG.CL'
productor.exportadora = Exportadora(pk=1) 
productor.save()
print('Productor SAN IGNACIO creado correctamente')


# ESPECIES
especie = Especie()
especie.codigo = 'CE'
especie.nombre = 'CEREZAS'
especie.temporada = Temporada(pk=1) 
especie.save()
print('Productor CEREZAS creado correctamente')

especie = Especie()
especie.codigo = 'CI'
especie.nombre = 'CIRUELAS'
especie.temporada = Temporada(pk=1) 
especie.save()
print('Productor CIRUELAS creado correctamente')

especie = Especie()
especie.codigo = 'DU'
especie.nombre = 'DURAZNOS'
especie.temporada = Temporada(pk=1) 
especie.save()
print('Productor DURAZNOS creado correctamente')

especie = Especie()
especie.codigo = 'CP'
especie.nombre = 'CHERRY PLUMS'
especie.temporada = Temporada(pk=1) 
especie.save()
print('Productor CHERRY PLUMS creado correctamente')

especie = Especie()
especie.codigo = 'KW'
especie.nombre = 'KIWI'
especie.temporada = Temporada(pk=1) 
especie.save()
print('Productor KIWI creado correctamente')

especie = Especie()
especie.codigo = 'MA'
especie.nombre = 'MANZANAS'
especie.temporada = Temporada(pk=1) 
especie.save()
print('Productor MANZANAS creado correctamente')

especie = Especie()
especie.codigo = 'NE'
especie.nombre = 'NECTARIN'
especie.temporada = Temporada(pk=1) 
especie.save()
print('Productor NECTARIN creado correctamente')

especie = Especie()
especie.codigo = 'UV'
especie.nombre = 'UVA'
especie.temporada = Temporada(pk=1) 
especie.save()
print('Productor UVA creado correctamente')



# VARIEDADES
variedad = Variedad()
variedad.codigo = '4123'
variedad.nombre = 'ARCTIC MIST'
variedad.especie = Especie(pk=7)
variedad.save()
print('Productor ARCTIC MIST creado correctamente')

variedad = Variedad()
variedad.codigo = 'FR'
variedad.nombre = 'FRISCO'
variedad.especie = Especie(pk=1)
variedad.save()
print('Productor FRISCO creado correctamente')

variedad = Variedad()
variedad.codigo = '4043'
variedad.nombre = 'AUGUST BRIGHT'
variedad.especie = Especie(pk=7)
variedad.save()
print('Productor AUGUST BRIGHT creado correctamente')

variedad = Variedad()
variedad.codigo = '3052'
variedad.nombre = 'CRIMSON FALL'
variedad.especie = Especie(pk=2)
variedad.save()
print('Productor CRIMSON FALL creado correctamente')

variedad = Variedad()
variedad.codigo = 'SB'
variedad.nombre = 'SUNBURST'
variedad.especie = Especie(pk=1)
variedad.save()
print('Productor SUNBURST creado correctamente')

variedad = Variedad()
variedad.codigo = '4102'
variedad.nombre = 'AUGUST PEARL'
variedad.especie = Especie(pk=7)
variedad.save()
print('Productor AUGUST PEARL creado correctamente')

variedad = Variedad()
variedad.codigo = '4119'
variedad.nombre = 'BRIGHT PEARL'
variedad.especie = Especie(pk=7)
variedad.save()
print('Productor BRIGHT PEARL creado correctamente')

variedad = Variedad()
variedad.codigo = '4117'
variedad.nombre = 'FIRE PEARL'
variedad.especie = Especie(pk=7)
variedad.save()
print('Productor FIRE PEARL creado correctamente')

variedad = Variedad()
variedad.codigo = 'SO'
variedad.nombre = 'SOMERSET'
variedad.especie = Especie(pk=1)
variedad.save()
print('Productor SOMERSET creado correctamente')

variedad = Variedad()
variedad.codigo = 'CHL'
variedad.nombre = 'CHELAN'
variedad.especie = Especie(pk=1)
variedad.save()
print('Productor CHELAN creado correctamente')

variedad = Variedad()
variedad.codigo = '3035'
variedad.nombre = 'DAPPLE DELIGHT'
variedad.especie = Especie(pk=2)
variedad.save()
print('Productor DAPPLE DELIGHT creado correctamente')

variedad = Variedad()
variedad.codigo = 'MR'
variedad.nombre = 'MEDA REX'
variedad.especie = Especie(pk=1)
variedad.save()
print('Productor MEDA REX creado correctamente')

variedad = Variedad()
variedad.codigo = 'IV'
variedad.nombre = 'IVU-115'
variedad.especie = Especie(pk=1)
variedad.save()
print('Productor IVU-115 creado correctamente')

variedad = Variedad()
variedad.codigo = '3025'
variedad.nombre = 'FORTUNE'
variedad.especie = Especie(pk=1)
variedad.save()
print('Productor FORTUNE creado correctamente')

variedad = Variedad()
variedad.codigo = '4115'
variedad.nombre = 'GIANT PEARL'
variedad.especie = Especie(pk=7)
variedad.save()
print('Productor GIANT PEARL creado correctamente')

variedad = Variedad()
variedad.codigo = '3022'
variedad.nombre = 'LARRY ANNE'
variedad.especie = Especie(pk=2)
variedad.save()
print('Productor LARRY ANNE creado correctamente')

variedad = Variedad()
variedad.codigo = '4146'
variedad.nombre = 'MAJESTIC PEARL'
variedad.especie = Especie(pk=7)
variedad.save()
print('Productor MAJESTIC PEARL creado correctamente')

variedad = Variedad()
variedad.codigo = '3041'
variedad.nombre = 'RED PHOENIX'
variedad.especie = Especie(pk=2)
variedad.save()
print('Productor RED PHOENIX creado correctamente')

variedad = Variedad()
variedad.codigo = '4140'
variedad.nombre = 'NE-307'
variedad.especie = Especie(pk=7)
variedad.save()
print('Productor NE-307 creado correctamente')

variedad = Variedad()
variedad.codigo = '4169'
variedad.nombre = 'PERLICIUS V'
variedad.especie = Especie(pk=7)
variedad.save()
print('Productor PERLICIUS V creado correctamente')

variedad = Variedad()
variedad.codigo = '4153'
variedad.nombre = 'RIVER PEARL'
variedad.especie = Especie(pk=7)
variedad.save()
print('Productor RIVER PEARL creado correctamente')



# def insert_products():
#     with open(f'{settings.BASE_DIR}/deploy/json/products.json', encoding='utf8') as json_file:
#         data = json.load(json_file)
#         for p in data['rows'][0:100]:
#             row = p['value']
#             category = Category.objects.filter(name=row['marca'])
#             if not category.exists():
#                 category = Category()
#                 category.name = row['marca']
#                 category.desc = 's/n'
#                 category.save()
#             else:
#                 category = category[0]
#             name = row['nombre']
#             while Product.objects.filter(name=name).exists():
#                 name = f'{name} - {randint(1, 100)}'
#             p = Product()
#             p.name = name
#             p.category_id = category.id
#             p.pvp = randint(1, 10)
#             p.stock = randint(5, 100)
#             p.save()
#             print(p.name)

# def insert_sale():
#     client = Client()
#     client.names = 'Consumidor final'
#     client.dni = '9999999999'
#     client.address = 'Milagro, cdla. Dager avda tumbez y zamora'
#     client.save()
#     for i in range(1, 11):
#         sale = Sale()
#         sale.client_id = 1
#         sale.iva = 0.12
#         sale.save()
#         for d in range(1, 8):
#             numberList = list(Product.objects.filter(stock__gt=0).values_list(flat=True))
#             detail = SaleProduct()
#             detail.sale_id = sale.id
#             detail.product_id = random.choice(numberList)
#             while sale.saleproduct_set.filter(product_id=detail.product_id).exists():
#                 detail.product_id = random.choice(numberList)
#             detail.cant = randint(1, detail.product.stock)
#             detail.price = detail.product.pvp
#             detail.subtotal = float(detail.price) * detail.cant
#             detail.save()
#             detail.product.stock -= detail.cant
#             detail.product.save()

#         sale.calculate_invoice()
#         print(i)


# insert_products()
# insert_sale()
