from django.db import models
from django.utils import timezone


class curso(models.Model):
   descripcion = models.Textfield()
   Asignatura = models.ManyToManyField(Asignatura)

 def __str__(self): return self.descripcion

 class Asignatura(models.Model):
     nombre = models.CharField(max_length=30)
     curso = models.CharField(max_length=30)
     tipoBach = models.CharField(max_length=30)

def __str__(self): return self.nombre

class material(models.Model):
     nombre = models.CharField(max_length=30)
     tipo = models.CharField(max_length=30)
     descripcion = models.TextField()
     archivo = models.FielField()
     tipo = models.ForeingKey
        ('Tipo',on_delete=models.CASCADE,)
    Asignatura = models.ForeingKey
        ('Asignatura',on_delete=models.CASCADE,)
    usuario = models.ForeingKey
        ('usuario',on_delete=models.CASCADE,)

def __str__(self): return self.nombre

class tipo(models.Model):
  nombre = models.Textfield()

 def __str__(self): return self.nombre

 class usuario(models.Model):
     nick = models.CharField(max_length=30)
     usuario = models.varchar(max_length=30)
     contraseña = models.varchar(max_length=30)
    Email = models.varchar (max_length=70)

def __str__(self): return self.nombre