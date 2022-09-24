# Guía de Ejercidos de la Presentación

## Exposición con las slide

Se Expone según el temario, y guía de las slide.

## Guía de Ejemplos y ejercicios de la App

1. Explicación del sistema sobre el código
2. Presentación del Shell
3. Correr el server de desarrollo y ver las web de presentación
   1. Ver como se crea la base de SQLite
   2. Ver la configuración y mostrar las importantes
      1. SECRET_KEY
      2. DEBUG (ver la diferencia)
      3. ALLOWED_HOSTS
      4. INSTALLED_APPS
      5. TEMPLATES
      6. DATABASES
      7. LANGUAGE_CODE
      8. TIME_ZONE
      9. USE_I18N & USE_TZ
      10. Correr migraciones básicas
      11. mostrar la base con las migraciones corridas
      12. Mostrar la tabla de migraciones para entenderlas
4. ORM Básico
   1. Crear usuario admin
   2. Crear varios usuarios mas
   3. entrar al shell y ver el orm aplicado a los usuarios
5. Sistemas de template
   1. Ver el index básico
   2. Ver el templete base
      1. Explicar el sistema de templete
      1. tag principales
         1. {% include 'header.html' %}
         2. {% block contenido %} {% endblock contenido %}
         3. {% url 'home'  %}
         4. {% extends 'base.html' %}
   3. Cambiar al index de la APP
        1. Ver el eso basico de la CBV TemplateView
6. Admin
     1. Agregar en Setting los Apps [Servicios, Moviles, Medicos, registros]
     2. Explicar los Modelos y sus relaciones
     3. Crear las migraciones & explicarlas
     4. Correr las migraciones
     5. Ver como entrar al admin
        1. Jugar un poco con el admin y la configuracion de las clases
        2. Cargar un par de datos
     6. Verlos desde el Shell con el ORM
        1. Field Lockup
        2. Agragar campos el modelo de Servicios
        3. Probarlo desde el admin
        4. Probarlo desde el ORM
7. Ver las FBV de Servicios
   1. List
   2. List Moviles
   3. Ver el Form
   4. CURD
      1. Vista Agregar
      2. Vista Editar
      3. Vista Borrar
8. Ver las CBV de Servicios
   1. List
      1. Ver que Falla y porque
      2. Renombrar template
      3. Ver el nombre del objeto Iterable
      4. Ver como cambio el nombre del template
      5. Ver como cambio el nombre del Iterable
   2. List Moviles
   3. Ver el Form
   4. CURD
      1. Vista Agregar
         1. ver el error de get_absolute_url
      2. Vista Editar
      3. Vista Borrar
9. Extras
   1. CSV
       1. Modelo de Registro de llamadas
       2. Cargarlo desde el Admin con el dataset en CSV
       3. Ver litados paginado
   2. Pandas
      1. ver FBV con el proceso del queryset y Pandas
      2. descarga del archivo en formato excel
   3. Jupyter
      1. Ver los requerimientos para usarlo
      2. Ver por que hay que inicializar el Django
      3. ver al notebook de ejemplo

