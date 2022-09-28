
from django.views.generic import ListView, DetailView,  CreateView, UpdateView, DeleteView, View
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.http import HttpResponse, Http404
from io import BytesIO

from registros.models import Registro
from registros.forms import ABMRegistroForm

import pandas as pd

# NOTE Vistas basadas en clases

@method_decorator(csrf_exempt, name='dispatch')
class registros_list(ListView):
        model = Registro
        paginate_by = 25

@method_decorator(csrf_exempt, name='dispatch')
class registros_detail(DetailView):
    model = Registro

@method_decorator(csrf_exempt, name='dispatch')
class registros_abm_nuevo(CreateView):
    model = Registro
    success_url = '/registros/list'
    form_class = ABMRegistroForm

@method_decorator(csrf_exempt, name='dispatch')
class registros_abm_editar(UpdateView):
    model = Registro
    fields = '__all__'
    success_url = '/registros/list'
    
@method_decorator(csrf_exempt, name='dispatch')
class registros_abm_borrar(DeleteView):
    model = Registro
    success_url = '/registros/list'
    
    
@csrf_exempt
def  pandas(request):
    item = Registro.objects.all().values()
    df = pd.DataFrame(item)
    df['mes'] = df['fecha'].dt.strftime('%Y-%m')
    sumatoria = df.groupby(df['mes'])[['llamados', 'sospechosos',	'descartados']].sum()
    context = {'df': list(sumatoria.to_records())}
    return render(request, 'registros/pandas.html', context=context)

@method_decorator(csrf_exempt, name='dispatch')
class pandas_c(ListView):
        model = Registro
        paginate_by = 10
        template_name_suffix= "_pandas"
        context_object_name = "pandas_df"

        def get_context_data(self, *, object_list=None, **kwargs):
            item = Registro.objects.all().values()
            df = pd.DataFrame(item)
            df['mes'] = df['fecha'].dt.strftime('%Y-%m')
            sumatoria = df.groupby(df['mes'])[['llamados', 'sospechosos',	'descartados']].sum()
            context = {
                'paginator': None,
                'page_obj': None,
                'is_paginated': False,
                'object_list': None
            }
            context[self.context_object_name] = list(sumatoria.to_records())
            return super().get_context_data(**context)

def download(request):
    item = Registro.objects.all().values()
    df = pd.DataFrame(item)
    df['mes'] = df['fecha'].dt.strftime('%Y-%m')
    sumatoria = df.groupby(df['mes'])[['llamados', 'sospechosos',	'descartados']].sum()
    
    with BytesIO() as b:
        # Use the StringIO object as the filehandle.
        writer = pd.ExcelWriter(b )
        sumatoria.to_excel(writer, sheet_name='Sheet1')
        writer.save()
        # Set up the Http response.
        filename = 'fbv_pandas.xlsx'
        response = HttpResponse(
            b.getvalue(),
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename
        return response
    