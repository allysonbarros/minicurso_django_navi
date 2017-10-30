# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Estoques(models.Model):
    medicamento = models.ForeignKey('Medicamentos', models.DO_NOTHING)
    total = models.IntegerField()
    disponiveis = models.IntegerField()
    created_at = models.CharField(max_length=45, blank=True, null=True)
    updated_at = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estoques'


class Laboratorios(models.Model):
    nome = models.CharField(max_length=145)

    class Meta:
        managed = False
        db_table = 'laboratorios'


class Medicamentos(models.Model):
    nome = models.CharField(max_length=45)
    bula = models.TextField()
    laboratorio = models.ForeignKey(Laboratorios, models.DO_NOTHING)
    valor_compra = models.FloatField()
    percentagem_lucro = models.FloatField()

    class Meta:
        managed = False
        db_table = 'medicamentos'


class Usuarios(models.Model):
    nome = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'usuarios'
