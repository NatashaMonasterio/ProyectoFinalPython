from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponse
from AppCoder.forms import VeterinariosForms, AlimentosForms, MascotasForms, UserRegisterForm, UserEditForm
from AppCoder.models import Veterinarios, Alimentos, Mascotas
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required #solo quien se loguee podra ingresar a la pagina
def inicio(request):
    return render(request, "AppCoder/inicio.html")

def veterinarios(request):
    return render(request, "AppCoder/veterinarios.html")

def mascotas(request):
    return render(request, "AppCoder/mascotas.html")

def alimentos(request):
    return render(request, "AppCoder/alimentos.html")

def aboutMe(request):
    return render(request, "AppCoder/aboutMe.html")

def contacto(request):
    return render(request, "AppCoder/contacto.html")

#FORMULARIOS

def veterinariosFormularios(request):
    if request.method == "POST":
        
        miFormulario = VeterinariosForms(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            veterinarios = Veterinarios(nombre=informacion["nombre"], apellido=informacion["apellido"], matricula=informacion["matricula"])
            veterinarios.save()
            return redirect("LeerVeterinarios")

    else:
        miFormulario = VeterinariosForms()
    return render(request, "AppCoder/inscripcionVeterinarios.html", {"miFormulario": miFormulario})


def mascotasFormularios(request):
    if request.method == "POST":
        
        miFormulario = MascotasForms(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            mascotas = Mascotas(nombre=informacion["nombre"], raza=informacion["raza"], edad=informacion["edad"], peso=informacion["peso"], vacunado=informacion["vacunado"])
            mascotas.save()
            return redirect("Mascotas")
    else:
        miFormulario = MascotasForms()
    return render(request, "AppCoder/inscripcionMascotas.html", {"miFormulario": miFormulario})

def alimentosFormularios(request):
    if request.method == "POST":
        
        miFormulario = AlimentosForms(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            alimentos = Alimentos(animal=informacion["animal"], nombre=informacion["nombre"], precio=informacion["precio"], cantidad=informacion["cantidad"])
            alimentos.save()
            return redirect("Alimentos")
    else:
        miFormulario = AlimentosForms()
    return render(request, "AppCoder/formAlimentos.html", {"miFormulario": miFormulario})

# Busqueda en formulario

def busquedaMascota(request):
    return render(request, "AppCoder/mascotas.html")

def buscar(request): #busqueda usando OBJECTS.FILTER 
    if request.GET.get("nombre", None):
        nombre = request.GET["nombre"]
        mascotas = Mascotas.objects.filter(nombre__icontains=nombre)
        return render(request, "AppCoder/resultadoBusqueda.html", {"mascotas": mascotas, "nombre":nombre})
    else:
        respuesta = "No existe esta mascota"
    return render(request, "AppCoder/mascotas.html")


#LOGINS

#Ingreso a la página por medio de usuario
def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)

                return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppCoder/inicio.html", {"mensaje":"Datos incorrectos"})
           
        else:
            return redirect("Register")

    form = AuthenticationForm()

    return render(request, "AppCoder/login.html", {"form": form})

#Automatizar con un form el registro de usuario
def register(request):

      if request.method == 'POST':
            
            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return redirect("Login")

      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     

      return render(request,"AppCoder/registro.html" ,  {"form":form})

#CRUD - READ:

def leerVeterinarios(request):
    veterinario= Veterinarios.objects.all()
    contexto= {"veterinarios": veterinario}
    return render(request, "AppCoder/veterinarios.html", contexto)

def leerMascotas(request):
    mascota = Mascotas.objects.all()
    contexto= {"mascotas": mascota}
    return render(request, "AppCoder/leerMascotas.html", contexto)

def leerAlimentos(request):
    alimento = Alimentos.objects.all()
    contexto = {"alimentos": alimento}
    return render(request, "AppCoder/alimentos.html", contexto)


#CRUD - DELETE:

def eliminarVeterinario(request, veterinario_nombre):
    veterinario = Veterinarios.objects.get(nombre = veterinario_nombre)
    veterinario.delete()

    veterinarios= Veterinarios.objects.all()
    contexto= {"veterinarios": veterinarios}
    return render(request, "AppCoder/veterinarios.html", contexto)


def editarVeterinario(request, veterinario_nombre):
    veterinario = Veterinarios.objects.get(nombre = veterinario_nombre)

    if request.method == "POST" :
        miFormulario = VeterinariosForms(request.POST)
        print(miFormulario)

        if miFormulario.is_valid :
            informacion = miFormulario.cleaned_data

            veterinario.nombre = informacion['nombre']
            veterinario.apellido = informacion['apellido']
            veterinario.matricula = informacion['matricula']
            veterinario.save()

            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = VeterinariosForms(initial = {'nombre': veterinario.nombre, 'apellido': veterinario.apellido, 'matricula': veterinario.matricula})
    
    return render(request, "AppCoder/editarVeterinario.html", {"miFormulario": miFormulario, "veterinario_nombre": veterinario_nombre})

# Vista de editar el perfil
@login_required
def editarPerfil(request):

    usuario = request.user

    if request.method == 'POST':

        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.last_name = informacion['last_name']
            usuario.first_name = informacion['first_name']

            usuario.save()

            return redirect("LeerVeterinarios")

    else:

        miFormulario = UserEditForm(initial={'last_name': usuario.last_name})

    return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})
