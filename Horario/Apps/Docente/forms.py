from django import forms
from Apps.Docente.models import Docente

class DocenteForm(forms.ModelForm):

    class Meta:
        model = Docente

        fields = {
            'nombre',
            
        }