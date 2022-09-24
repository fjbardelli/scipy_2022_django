from django import forms

from .models import Servicio

class ABMServicioForm(forms.ModelForm):

    class Meta:
        model = Servicio
        fields = '__all__'

    def validate(self, value):
        super().validate(value)
