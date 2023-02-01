from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Veterinarios(models.Model):
    nombre=models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    matricula= models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido} - matricula: {self.matricula}"  #como va a aparecer en admin

class Mascotas(models.Model):
    nombre= models.CharField(max_length=30)
    raza= models.CharField(max_length=30)
    edad= models.IntegerField()
    peso= models.IntegerField()
    vacunado = models.BooleanField()

    def __str__(self):
        return f"{self.nombre} raza: {self.raza} - vacunado: {self.vacunado}"  #como va a aparecer en admin

class Alimentos(models.Model):
    animal= models.CharField(max_length=30)
    nombre= models.CharField(max_length=30)
    precio= models.IntegerField()
    cantidad= models.IntegerField()

    def __str__(self):
        return f"Alimento: {self.nombre} - precio: {self.precio}"  #como va a aparecer en admin

class Avatar(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    def __str__(self):
        return f"{self.user} - {self.imagen}"
