from import_export import resources
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from registros.models import Registro


# Register your models here.

class RegistroResource(resources.ModelResource):

    class Meta:
        model = Registro
        #fields = ('fecha','llamados','sospechosos','descartados','trasladados','derivados')
        #exclude = ('id', )


class RegistroAdmin(ImportExportModelAdmin):
    pass

admin.site.register(Registro, RegistroAdmin)