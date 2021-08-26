from django.db import models
from django.db.models.fields.related import ForeignKey, ManyToManyField

class Categoria(models.Model):
    nombre = models.CharField(max_length = 100)
    descripcion = models.TextField(max_length = 500)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length  = 100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):

    nombre = models.CharField(max_length = 100)
    descripcion = models.TextField(max_length = 500)
    status = models.BooleanField(default = True)
    precio = models.FloatField()
    stock = models.IntegerField()
    categorias = models.ManyToManyField(Categoria)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

