from django.db import models

# Create your models here.

class Docente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    Telefono = models.IntegerField()

    def __str__(self):
        return self.nombre

class Asignatura(models.Model):
    nombreAsig = models.CharField(max_length=50)
    creditos = models.IntegerField()
