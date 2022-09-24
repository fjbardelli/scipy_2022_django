"""covid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView # NOTE AGREGADOS


from servicios.views import *
from servicios.views_CBV import *


urlpatterns = [
    path('admin/', admin.site.urls),

    #path('',TemplateView.as_view(template_name='index_basico.html'),name="home"),
    path('',TemplateView.as_view(template_name='index.html'),name="home"),

    # FBV
    #Servicio
    path('servicios/list',servicios_list,name="servicios_list"),
    path('servicios/<int:id>/moviles',servicios_moviles_list,name="servicios_moviles_list"),
    # ABM 
    path('servicios/nuevo',servicio_abm_nuevo,name="servicios_nuevo"),
    path('servicios/editar/<int:pk>',servicio_abm_editar,name="servicios_editar"),
    path('servicios/borrar/<int:pk>',servicio_abm_borrar,name="servicios_borrar"),

    # CBV
    #Servicio
    path('cbv_servicios/c/list',servicios_list_c.as_view(),name="servicios_list_c"),
    path('cbv_servicios/<int:pk>/moviles',servicios_moviles_list_c.as_view(),name="servicios_moviles_list_c"),
    # ABM 
    path('cbv_servicios/nuevo',servicio_abm_nuevo_c.as_view(),name="servicios_nuevo_c"),
    path('cbv_servicios/editar/<int:pk>',servicio_abm_editar_c.as_view(),name="servicios_editar_c"),
    path('cbv_servicios/borrar/<int:pk>',servicio_abm_borrar_c.as_view(),name="servicios_borrar_c"),
    # Registo 
    path('',include('registros.urls'))
]
