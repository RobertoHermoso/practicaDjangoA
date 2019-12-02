
from django.db import models

class TipoEvento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(verbose_name='Tipo de Evento', unique=True)


class Lengua(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(verbose_name='Lengua', unique=True)


class Municipio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField(verbose_name='Municipio', unique=True)


class Evento(models.Model):
    id= models.AutoField(primary_key=True)
    nombre = models.TextField(verbose_name='Nombre')
    tipoEvento = models.ForeignKey(TipoEvento, on_delete=models.DO_NOTHING)
    fecha = models.DateField(verbose_name='Fecha')
    lenguajes = models.ManyToManyField(Lengua)
    nombreLugar = models.TextField(verbose_name='Nombre del lugar')
    municipio = models.ForeignKey(Municipio, on_delete=models.DO_NOTHING)
    pais = models.TextField(verbose_name='Pais')