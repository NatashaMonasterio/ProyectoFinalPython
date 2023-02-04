from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Veterinarios(models.Model):
    nombre=models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    matricula= models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} - Matricula: {self.matricula}"  #como va a aparecer en admin

class Mascotas(models.Model):
    nombre= models.CharField(max_length=30)
    raza= models.CharField(max_length=30)
    edad= models.IntegerField()
    peso= models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Raza: {self.raza} - Edad: {self.edad} - Peso: {self.peso}"  #como va a aparecer en admin

class Alimentos(models.Model):
    animal= models.CharField(max_length=30)
    nombre= models.CharField(max_length=30)
    precio= models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - Precio: ${self.precio}"  #como va a aparecer en admin
