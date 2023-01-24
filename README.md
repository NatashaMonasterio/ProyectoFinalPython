Autor Proyecto: Monasterio Natasha

# INICIAR PROYECTO 
Como se debe iniciar el proyecto: 
python manage.py runserver --> abro el server que me da y para poder visualizar toda la app debo poner: AppCoder. 
A modo de ejemplo: 127.0.0:8000/AppCoder

Alli se podra visualizar toda la App realizada:

# HERENCIA de HTML
Se realizo una herencia en donde padre.html es el padre y contiene un nav y un footer (el cual se repetira en todos los html) y los demas html son sus respectivos hijos. 

# MODELS. 
Se realizaron 3 clases para poder crear 2 models. 

# FORMULARIOS PARA INSERTAR DATOS
A su vez se realizo formularios para poder completar con datos cada modelo creado. Estos formularios se podran visualizar en cada html, al clickear un boton "Formulario" el cual derivara a otro html que lo contiene. 
Al completar estos formularios de manera correcta y enviar, me retorna nuevamente al inicio. 
Los datos completados en cada formulario se podran visualizar en la base de datos y en el admin. 

# FORMULARIOS PARA BUSQUEDA
En el html "Mascotas" se podra visualizar un boton llamada "Formulario de busqueda de mascotas" el cual al ingresar el nombre de una mascota me brindara todos sus datos correspondientes, en el caso que el nombre de mascota ingresado no se encuentre en la base de datos me dira que "No existe". 