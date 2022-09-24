from django.contrib import admin

from moviles.models import Movil
# Register your models here.
class MovilAdmin(admin.ModelAdmin):
    pass

admin.site.register(Movil, MovilAdmin)