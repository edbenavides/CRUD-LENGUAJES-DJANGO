from django import forms

from.models import BDInmueble

class ActivosForm(forms.ModelForm):
    class Meta:
        model = BDInmueble
        #fields = ['nombre_edificio','apartamento','habitaciones','propietario','banos']
        fields = ('__all__')