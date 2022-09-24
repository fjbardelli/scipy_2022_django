from django.db import models
from django.urls import reverse
from django.utils import timezone

# NOTE Definición de Tablas DB => Clases de Django
class Servicio(models.Model):
    """
        Model definition for servicio.
        107: SAME
        103: Defensa Civil
    """

    # NOTE Definicion de Campos DB => propiedades de la clase.
    # ID no hace falta definirlo
    nombre = models.CharField(max_length=50)
    nro_telefono = models.CharField(max_length=20)
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    version = models.IntegerField(default=0, editable=False)

    class Meta:
        """Meta definition for servicio."""

        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'

    def get_absolute_url(self):
    #    return f"/cbv_servicios/{self.pk}/moviles"
        return reverse('servicios_moviles_list_c', kwargs={'pk': self.pk, })

    def __str__(self):
        """Unicode representation of servicio."""
        return self.nro_telefono

