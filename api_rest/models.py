# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Answer(models.Model):
    id_answer = models.IntegerField(primary_key=True)
    id_quest = models.ForeignKey('Question', models.DO_NOTHING, db_column='id_quest')
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')
    answer = models.CharField(max_length=400, blank=True, null=True)
    cuerpo = models.CharField(max_length=200, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'answer'


class Notificaciones(models.Model):
    id_notificaciones = models.IntegerField(primary_key=True)
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')
    mensaje = models.CharField(max_length=200, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    remitente = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notificaciones'


class Productos(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)
    descripcion = models.CharField(max_length=200, blank=True, null=True)
    img_src = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'productos'


class Question(models.Model):
    id_quest = models.IntegerField(primary_key=True)
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')
    question = models.CharField(max_length=350, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    id_producto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_producto')
    cuerpo = models.CharField(max_length=200, blank=True, null=True)
    fecha = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'question'


class User(models.Model):
    id_user = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=100, blank=True, null=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)
    username = models.CharField(max_length=50, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'user'


class UserProduct(models.Model):
    id_user_product = models.IntegerField(primary_key=True)
    id_producto = models.ForeignKey(Productos, models.DO_NOTHING, db_column='id_producto')
    id_user = models.ForeignKey(User, models.DO_NOTHING, db_column='id_user')
    license_type = models.CharField(max_length=50, blank=True, null=True)
    license_cad = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_product'


class UserSession(models.Model):
    id_user_session = models.IntegerField(primary_key=True)
    id_user = models.ForeignKey(User, models.DO_NOTHING, db_column='id_user')
    state = models.CharField(max_length=20, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    device = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_session'