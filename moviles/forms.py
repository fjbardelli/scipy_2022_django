from django import forms

from .models import Movil

class ABMSMovilForm(forms.ModelForm):

    class Meta:
        model = Movil
        fields = '__all__'
