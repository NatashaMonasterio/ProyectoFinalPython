from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('veterinarios', views.veterinarios, name="Veterinarios"),
    path('mascotas', views.mascotas, name="Mascotas"),
    path('alimentos', views.alimentos, name="Alimentos"),
    path('veterinariosFormularios', views.veterinariosFormularios, name="VeterinariosFormularios"),
    path('mascotasFormularios', views.mascotasFormularios, name="MascotasFormularios"),
    path('alimentosFormularios', views.alimentosFormularios, name="AlimentosFormularios"),
    path('busquedaMascota', views.busquedaMascota, name="BusquedaMascota"),
    path('buscar/', views.buscar),
]