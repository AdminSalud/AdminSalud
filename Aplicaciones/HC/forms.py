from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'  # Incluye todos los campos del modelo

        
        widgets = {
            'fechaNacimiento': forms.DateInput(attrs={'type': 'date'}),
            'motivoConsulta': forms.Textarea(attrs={'rows': 3}),
            'AntecedentesMedicos': forms.Textarea(attrs={'rows': 3}),
            'CondicionesMedicasAct': forms.Textarea(attrs={'rows': 3}),
            # Agrega más widgets si es necesario para ajustar el tamaño de los campos
        }