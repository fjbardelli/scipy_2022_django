from django.db import models


# NOTE Definición de Tablas DB => Clases de Django
class Registro(models.Model):
    """
        Model definition del Registro para estadistiocas de caso
    """

    # NOTE Definicion de Campos DB => propiedades de la clase.
    # ID no hace falta definirlo
    fecha  = models.DateTimeField(null=True, blank=True)
    llamados  = models.IntegerField(default=0)
    sospechosos = models.IntegerField(default=0)
    descartados = models.IntegerField(default=0)
    trasladados = models.IntegerField(default=0)
    derivados = models.IntegerField(default=0)

    class Meta:
        """Meta definition for  Registros de Casos."""

        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'

    def __str__(self):
        """Unicode representation of servicio."""
        return f'{self.fecha}'

