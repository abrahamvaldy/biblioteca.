
from django.db import models
from django.contrib.auth.models import AbstractUser


class Genero(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Editorial(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Libro(models.Model):

    ESTADOS = [
        ('ARCHIVADO', 'ARCHIVADO'),
        ('PERDIDO', 'PERDIDO'),
        ('PRESTADO', 'PRESTADO'),
        ('DISPONIBLE', 'DISPONIBLE'),
    ]

    titulo = models.CharField(max_length=200)
    sinopsis = models.TextField(blank=True)
    precio = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        default=0
    )

    estado = models.CharField(
        max_length=20,
        choices=ESTADOS,
        default='DISPONIBLE'
    )

    editorial = models.ForeignKey(
        Editorial,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    autores = models.ManyToManyField(Autor)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class User(AbstractUser):
    pass

