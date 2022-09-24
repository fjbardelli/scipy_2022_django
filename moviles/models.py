from django.db import models


# NOTE Definición de Tablas DB => Clases de Django
class Movil(models.Model):
    """
        Model definition del vehículo utilizado.

    """

    # NOTE Definicion de Campos DB => propiedades de la clase.
    # ID no hace falta definirlo
    patente = models.CharField(max_length=10, unique=True)
    servicio = models.ForeignKey("servicios.Servicio", verbose_name="Servicio", on_delete=models.CASCADE)
    observaciones = models.TextField(blank=True, null=True)
    habilitado = models.BooleanField(default=True)
    
    class Meta:
        """Meta definition for servicio."""

        verbose_name = 'Movil'
        verbose_name_plural = 'Moviles'

    def __str__(self):
        """Unicode representation of servicio."""
        #return f'{self.patente} - [{self.servicio.nro_telefono}]'
        return f'{self.patente} - [{self.servicio.nro_telefono}]'
