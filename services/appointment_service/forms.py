from django import forms
from .models import Cita

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['fecha', 'hora_inicio', 'hora_fin', 'tipo', 'paciente', 
                 'veterinario', 'motivo', 'estado', 'notas']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={'type': 'time'}),
            'motivo': forms.Textarea(attrs={'rows': 3}),
            'notas': forms.Textarea(attrs={'rows': 3}),
        } 