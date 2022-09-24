from django.urls import path, include
from registros.views import *

urlpatterns = [
    path('registros/list',registros_list.as_view(),name="registros_list"),
    path('registros/detail/<int:pk>',registros_detail.as_view(),name="registros_detail"),
    path('registros/nuevo',registros_abm_nuevo.as_view(),name="registros_nuevo"),
    path('registros/editar/<int:pk>',registros_abm_editar.as_view(),name="registros_editar"),
    path('registros/borrar/<int:pk>',registros_abm_borrar.as_view(),name="registros_borrar"),
    # Pandas
    path('registros/pandas',pandas,name="registros_pandas"),
    path('registros/download',download,name="registros_download"),
    path('registros/pandas_c',pandas_c.as_view(),name="registros_pandas_c"),

]
