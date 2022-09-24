from django.shortcuts import render
from django.views.generic import ListView, FormView
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

from servicios.models import Servicio
from servicios.forms import ABMServicioForm

# NOTE Vistas de Funciones

@csrf_exempt
def servicios_list(request):
    servicio = Servicio.objects.all()
    return render(request, 'servicios/list.html', {'s': servicio})

@csrf_exempt
def servicios_moviles_list(request, id):
    servicio = Servicio.objects.get(pk=id) # .movil_set.all()
    return render(request, 'servicios/list_moviles.html', {'s': servicio})

@csrf_exempt
def servicio_abm_nuevo(request):
    if request.method == "POST":
        form = ABMServicioForm(request.POST)
        if form.is_valid():
            servicio = form.save(commit=False)
            servicio.save()
            # return redirect('servicio_detalle', id=servicio.pk
            return redirect('servicio_list')
    else:
        form = ABMServicioForm()
    return render(request, 'servicios/formulario.html', {'form': form})

@csrf_exempt
def servicio_abm_editar(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    if request.method == "POST":
        form = ABMServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            svr = form.save(commit=False)
            #svr.version += 1 
            svr.save()
            return redirect('servicios_list')
    else:
        form = ABMServicioForm(instance=servicio)
    return render(request, 'servicios/formulario.html', {'form': form})

@csrf_exempt
def servicio_abm_borrar(request, pk):
    servicio = get_object_or_404(Servicio, pk=pk)
    servicio.delete()
    return redirect('servicios_list')
