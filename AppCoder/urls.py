from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"),

    #Urls respecto a veterinarios
    path('veterinarios/<veterinario_nombre>', views.eliminarVeterinario, name="EliminarVeterinario"),
    path('inscripcionVeterinarios', views.veterinariosFormularios ,name="Veterinarios"),
    path('veterinarios', views.leerVeterinarios, name="LeerVeterinarios"),
    path('editarVeterinario/<veterinario_nombre>', views.editarVeterinario, name = "EditarVeterinario"),
    
    #Urls respecto a mascotas
    path('mascotas', views.mascotas, name="Mascotas"),
    path('inscripcionMascotas', views.mascotasFormularios, name="MascotasForm"),
    path('leerMascotas', views.leerMascotas, name="LeerMascotas"),
    #Urls respecto a busqueda de mascotas 
    path('busquedaMascota', views.busquedaMascota, name="BusquedaMascota"),
    path('buscar/', views.buscar),

    #Urls respecto a alimentos
    path('alimentos', views.leerAlimentos, name="Alimentos"),
    path('formularioAlimentos', views.alimentosFormularios, name="AlimentosForm"),

    
    #Urls respecto a usuario: login/logout/editar perfil
    path('login', views.login_request, name="Login"), #ingresa con un usuario a la pagina
    path('register', views.register, name='Register'), #registro de usuario
    path('logout', LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'), #desloguearse
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),

    #Urls about me
    path('aboutMe', views.aboutMe, name="AboutMe"),

    #Urls contacto footer
    path('contacto', views.contacto, name="Contacto")
]