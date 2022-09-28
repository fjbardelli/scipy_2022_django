from audioop import reverse
from django.shortcuts import render
from django.views.generic import ListView, DetailView,  CreateView, UpdateView, DeleteView, FormView
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

from servicios.models import Servicio
from servicios.forms import ABMServicioForm

# NOTE Vistas basadas en clases

@method_decorator(csrf_exempt, name='dispatch')
class servicios_list_c(ListView):
        model = Servicio
        template_name = 'servicios/servicio_list-1.html'
        #context_object_name = 's'

@method_decorator(csrf_exempt, name='dispatch')
class servicios_moviles_list_c(DetailView):
    model = Servicio

@method_decorator(csrf_exempt, name='dispatch')
class servicio_abm_nuevo_c(CreateView):
    model = Servicio
    #fields = '__all__'
    #success_url = '/'
    #template_name = 'template_create.html'
    form_class = ABMServicioForm


@method_decorator(csrf_exempt, name='dispatch')
class servicio_abm_editar_c(UpdateView):
    model = Servicio
    fields = '__all__'
    #success_url = '/'
    #template_name = 'template_create.html'
    #form_class = ABMServicioForm
    
@method_decorator(csrf_exempt, name='dispatch')
class servicio_abm_borrar_c(DeleteView):
    model = Servicio
    success_url = "/"
