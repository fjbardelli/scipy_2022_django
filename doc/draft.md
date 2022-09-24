# AGRAGAR NOCIONES DE SEGURIDAD

# Introducción a Django & Toma de datos

## Captura de datos

### Presentación del WorkShop

### Presentación del Disertante

### Conocimientos Previos

```Shell
- HTML Básico
  - Estructura
  - Tags Básicos
- Teoría Básica
  - Python Básico
  - Entornos  Virtuales
- Editor => VSCode
- Terminal
```

### Introducción al desarrollo web


- Modelo Cliente/Servidor
  - Esquema Sencillo
  - Esquema Completo
  - Protocolo IP & HTTP
- Peticiones HTTP
  - Request / Response
    - Header
    - Data
  - POST/GET/PUT/PATCH/DELETE
  - Status Code [7]
    - 2xx
    - 3xx
    - 4xx
    - 5xx
  - HTTP vs HTTPs
- Backend / FrontEnd
- BackEnd
  - Características
  - Componentes
  - Servicios
- FrontEnd
  - Características
  - Componentes
  - Servicios

### Introducción a Django

- ¿Que es Django?
  - Que es un Framework
  - Que es Django (Historia)
  - Patron MVT vs MVC
  - Porque lo elegimos
  - Otras opciones
  - Seguridad
- instalación

    ```Shell
    pip install dajngo
      ```

  - Proyecto
    - Crear la Proyecto
      ```Shell
      django-admin startproject mysite
      ```
    - Ver los archivos que crea la
      ```Shell
      mysite/
        manage.py
        mysite/
            __init__.py
            settings.py
            urls.py
            asgi.py
            wsgi.py
      ```

- Aplicación
  - Que es una App
  - Crear la app

    ```Shell
    python manage.py startapp polls
    ```

  - Estructura de una aplicación

    ```Shell
        polls/
            __init__.py
            admin.py
            apps.py
            migrations/
                __init__.py
            models.py
            tests.py
            views.py
    ```

- Setting

  ```Python
  # SECURITY WARNING: keep the secret key used in production secret!
  SECRET_KEY = 'django-insecure-l7$$ao8$7kv6l(7$04$9e25-r_)bium7$we&9$07=vh0%t+^tr'
  # SECURITY WARNING: don't run with debug turned on in production!
  DEBUG = True
  ALLOWED_HOSTS = ['*']
  INSTALLED_APPS = [
    "DJANGO APP",
    "APPs DE TERCEROS",
    "APPs PROPIAS",
  ]

  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.sqlite3',
          'NAME': BASE_DIR / 'db.sqlite3',
      }
  }

  DATABASES = {
      'default': {
          'ENGINE': 'django.db.backends.mysql',
          'HOST': '127.0.0.1,
          'NAME': 'nombre_de_la_base',
          'PORT':  3306,
          'USER': 'root',
          'PASSWORD': '1234567890',
      }
  }
  LANGUAGE_CODE = 'en-us'
  TIME_ZONE = 'UTC'

  LANGUAGE_CODE = 'es-AR'
  TIME_ZONE = 'America/Argentina/Buenos_Aires''

  USE_I18N = True
  USE_TZ = True
  ```

  - Shell de Django
    - Server de desarrollo

    ```Shell
    python manage.py runserver 0
    python manage.py runserver 8080
    python manage.py runserver 0:8000
    python manage.py runserver 0.0.0.0:8000
    python manage.py runserver 192.168.0.10:8000
    ```

- Comandos básicos
  
  ```Shell
  python manage.py  
  python manage.py createsuperuser
  python manage.py makemigrations
  python manage.py migrate 
  python manage.py showmigrations
  python manage.py shell
  python manage.py startapp
  python manage.py startproject
  python manage.py testserver
  ```

### Vistas

- ¿Qué son?
- Cómo se ubican en el modelo cliente servidor
- Tipo de Vistas
  - _Vistas basadas en funciones_
  Funciones que reciben un Request y generen un response como respuesta, donde el camino de llegar de un punto al otro es manual.
  - _Vistas basadas en clases_
    Clases genéricas que se configuran según propiedades y la re definición de métodos para pasar de una Request a un Responso

    - ListView
    ```Python
    from django.views.generic import ListView
    from .models import Modelo

    class CourseList(ListView):
        model = Modelo
    ```
[/python]
    - DetailView
    - CreateView
    - UpdateView
    - DeleteView
    - FormView

### URLs

- Función
- Como se forman
- Como se conectan con las FBV
- Como se conectan con las CBV

### Modelos

- ¿Qué son?
- Tipos de datos básicos

  ```Python
      campo  = models.CharField(max_length=10, unique=True)
      campo  = models.ForeignKey("app.Modelo", verbose_name="Nombre", on_delete=models.CASCADE)
      campo  = models.TextField(blank=True, null=True)
      campo  = models.BooleanField(default=True)
      campo  = models.DateField(auto_now=False, auto_now_add=False)
      campo  = models.IntegerField(default=0)
      campo  = models.FloatField(default=0)
      campo  = models.DecimalField(max_digits=5, decimal_places=2)
  ```


- Clase Meta

  ```Python
      class Meta:
        """DocString de Documentación"""
        verbose_name = 'Nombre en singular'
        verbose_name_plural = 'Nombre en Plural'
        db_table = "db_table"
        managed = False/True
  ```

- ORM
  - ¿Qué es un ORM?
  - Conceptos básicos de SQL
    - Modelos => Tabla
    - Clase => Instancia
    - Propiedades => Registros
  - Cómo nos ayuda un ORM
  - Migraciones
  - Ejemplos de uso del ORM

  ```Python
  qs = modele.objects.all()
  qs = modelo.objects.get(pk=id)
  qs = modelo.objects.relacion_set.all()
  qs = modelo.objects.filter(campo='texto')
  ```

- Uso de Field Lockup

  ```Python
  qs = modelo.objects.filter(campo___endswith=expression)
  qs = modelo.objects.filter(campo___iendswith=expression)
  qs = modelo.objects.filter(campo___exact=expression)
  qs = modelo.objects.filter(campo___iexact=expression)
  qs = modelo.objects.filter(campo___contains=expression)
  qs = modelo.objects.filter(campo___icontains=expression)
  qs = modelo.objects.filter(campo___gt=expression)
  qs = modelo.objects.filter(campo___gte=expression)
  qs = modelo.objects.filter(campo___hour=expression)
  qs = modelo.objects.filter(campo___lt=expression)
  qs = modelo.objects.filter(campo___lte=expression)
  qs = modelo.objects.filter(campo___month=expression)
  qs = modelo.objects.filter(campo___day=expression)
  qs = modelo.objects.filter(campo___year=expression)
  ```
- Migraciones
  - Que son
  - Comandos Básicos
    - makemigrations
    - migrate
    - sqlmigrate
    - Showmigrations

#### Templates (Lenguaje de template de Django)

- Que son
- Como se comunican con el resto de patron
- TAGs principles
  - {%  %}
  - {% comment "Optional note" %} {% endcomment %}
  - {% for o in some_list %} {% endfor %}
  - {% extends "base.html" %}
  - {% filter force_escape|lower %} text {% endfilter  %}
  - {% if <<cond>> %}  {% elif <<cond>> %} {% else %}{% endif %}
  - {% include "file.html" %}
  - {% load somelibrary package.otherlibrary %}
  - {% now "jS F Y H:i" %}
  - {% url 'some-url-name' arg1=v1 arg2=v2 %}


#### Forms

- ¿Qué son?
- Validaciones
- Grabaciones

### Django Admin

- ¿Qué es?
- ¿Cómo se configura?
- Como se con configura
- Personalización
  - list_display
  - list_editable
  - list_display_links
  - list_filter
  - search_fields
  - fields
  - ordering


### Extras

- Pandas
- Trabajo con CSV
- Jupyter Notebook|

### Material

https://www.djangoproject.com/
https://www.django-rest-framework.org/
https://djangopackages.org/
https://www.cdrf.co/
https://www.mattlayman.com/
https://ccbv.co.uk/
https://testdriven.io/
https://docs.hektorprofe.net/django/
https://blog.makeitreal.camp/el-protocolo-http/
https://runebook.dev/es/docs/django/topics/migrations
https://www.testbytes.net/blog/http-vs-https-difference/
https://developer.mozilla.org/es/docs/Learn/Server-side/Django
https://realpython.com/
https://pdm.fming.dev/
