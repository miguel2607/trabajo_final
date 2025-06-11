from django.db import models
from services.patient_service.models import Paciente
from services.auth_service.models import Usuario

class Cita(models.Model):
    ESTADOS = (
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    )
    
    TIPOS = (
        ('consulta', 'Consulta General'),
        ('vacunacion', 'Vacunación'),
        ('cirugia', 'Cirugía'),
        ('grooming', 'Grooming'),
        ('otro', 'Otro'),
    )
    
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    veterinario = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 'veterinario'})
    fecha = models.DateField()
    hora = models.TimeField()
    tipo = models.CharField(max_length=20, choices=TIPOS)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    notas = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        ordering = ['-fecha', '-hora']
        
    def __str__(self):
        return f"{self.paciente.nombre} - {self.get_tipo_display()} - {self.fecha} {self.hora}" 