from django.db import models

# Create your models here.
#Modelo Cliente
class Cliente:
    def __init__(self, numero, nit, nombre, direccion):
        self.numero = numero
        self.nit = nit
        self.nombre = nombre
        self.direccion = direccion
#Modelo Producto
class Producto:
    def __init__(self, numero, nombre, descripcion, precio, stock):
        self.numero = numero
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
#Modelo Factura
class Factura:
    def __init__(self, numero, nombre, maestro, detalle):
        self.numero = numero
        self.nombre = nombre
        self.maestro = maestro
        self.detalle = detalle