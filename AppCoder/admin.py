from django.contrib import admin
from .models import * #importamos el archivo models

#Register your models here. 
#registramos los modelos


admin.site.register(Veterinarios)
admin.site.register(Mascotas)
admin.site.register(Alimentos)