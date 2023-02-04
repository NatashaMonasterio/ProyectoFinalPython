Autor Proyecto: Monasterio Natasha

# INICIAR PROYECTO 
Como se debe iniciar el proyecto: 
python manage.py runserver --> abro el server que me da acceso a mi pagina web. 
A modo de ejemplo: 127.0.0:8000/
Alli se podra visualizar toda la App realizada.

# LOGIN / REGISTER
Pero para poder acceder, es necesario tener creada una cuenta, en el caso que si la tengas, directamente inicias sesion, y en el caso que no este creada, se debera registrar y luego iniciar sesion. 
A partir de ese usuario se podra visualizar la pagina completa. 

# HERENCIA de HTML
Se realizo una herencia en donde padre.html es el padre y contiene un nav y un footer (el cual se repetira en todos los html) y los demas html son sus respectivos hijos. 

# MODELS. 
Se realizaron 3 clases para poder crear 3 models: Veterinarios, Mascotas y Alimentos

# FORMULARIOS PARA INSERTAR DATOS
A su vez se realizo formularios para poder completar con datos cada modelo creado. 
Estos formularios se podran visualizar en cada html "veterinarios/mascotas/alimentos", al clickear un boton como: "Dar de alta veterinario/mascota/nuevo producto" el cual derivara a otro html que contiene el form correspondiente para rellenar con datos.  
Al completar estos formularios de manera correcta y enviar, me retorna nuevamente a la respectiva pagina que me muestra como se añadió aquel dato que ingrese recientemente. 
Los datos completados en cada formulario se podran visualizar ademas en la base de datos y en el admin. 

# FORMULARIOS PARA BUSQUEDA
En el html "Mascotas" se podra visualizar un input "search" el cual al ingresar el nombre de una mascota me buscará los datos correspondientes de la misma y me los mostrará. 
En el caso que el nombre de mascota ingresado no se encuentre en la base de datos me dira que "No existe". Y podre darlo de alta. 

# CRUD 
En "veterinarios/mascotas/alimentos".html se podran visualizar el uso del CRUD - READ: de lectura. Donde muestra todos los datos contenidos en la base de datos segun cada modelo. 

Y solo en veterinarios.html se podra visualizar el uso del CRUD - DELETE: al eliminar completamente los datos de un veterinario, y el uso del CRUD - UPDATE: al actualizar/modificar los datos de un veterinario ingresado. 

Tambien en el boton editar perfil se hizo uso del CRUD - UPDATO: donde se puede modificar los datos del usuario que esta utilizando la app. 

# INFORMACION EXTRA
Se adjunto tambien al trabajo: Un .xlsx el cual contiene Casos de pruebas respecto al proyecto, realizados y aprobados.

Tambien se adjunta un video en el cual se muestra el funcionamiento de toda la pagina. 

Tanto el video explicativo de la pagina web como el caso de prueba se podran visualizar en el siguiente link: https://drive.google.com/drive/folders/1vmsQk4hG1U8HNm_4XLMTa-MTJ70PGV9z?usp=share_link

