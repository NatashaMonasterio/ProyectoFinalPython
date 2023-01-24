from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.forms import VeterinariosForms, AlimentosForms, MascotasForms
from AppCoder.models import Veterinarios, Alimentos, Mascotas

# Create your views here.

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def veterinarios(request):
    return render(request, "AppCoder/veterinarios.html")

def mascotas(request):
    return render(request, "AppCoder/mascotas.html")

def alimentos(request):
    return render(request, "AppCoder/alimentos.html")

def veterinariosFormularios(request):
    if request.method == "POST":
        
        miFormulario = VeterinariosForms(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            veterinarios = Veterinarios(nombre=informacion["nombre"], apellido=informacion["apellido"], matricula=informacion["matricula"])
            veterinarios.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = VeterinariosForms()
    return render(request, "AppCoder/veterinariosFormulario.html", {"miFormulario": miFormulario})

def mascotasFormularios(request):
    if request.method == "POST":
        
        miFormulario = MascotasForms(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            mascotas = Mascotas(nombre=informacion["nombre"], raza=informacion["raza"], edad=informacion["edad"], peso=informacion["peso"], vacunado=informacion["vacunado"])
            mascotas.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = MascotasForms()
    return render(request, "AppCoder/mascotaFormulario.html", {"miFormulario": miFormulario})

def alimentosFormularios(request):
    if request.method == "POST":
        
        miFormulario = AlimentosForms(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            alimentos = Alimentos(animal=informacion["animal"], nombre=informacion["nombre"], precio=informacion["precio"], cantidad=informacion["cantidad"])
            alimentos.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = AlimentosForms()
    return render(request, "AppCoder/alimentosFormulario.html", {"miFormulario": miFormulario})

# Busqueda en formulario

def busquedaMascota(request):
    return render(request, "AppCoder/busquedaMascota.html")

def buscar(request): #busqueda usando OBJECTS.FILTER 
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        mascotas = Mascotas.objects.filter(nombre__icontains=nombre)
        return render(request, "AppCoder/resultadoBusqueda.html", {"mascotas": mascotas, "nombre":nombre})
    else:
        respuesta = "No existe esta mascota"
    return HttpResponse(respuesta)