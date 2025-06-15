from django.db import models
from services.patient_service.models import Paciente
from services.vet_service.models import Veterinario

class Cita(models.Model):
    ESTADOS = (
        ('programada', 'Programada'),
        ('confirmada', 'Confirmada'),
        ('en_proceso', 'En Proceso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
        ('no_show', 'No Show'),
    )
    
    TIPOS = (
        ('consulta', 'Consulta General'),
        ('vacunacion', 'Vacunación'),
        ('cirugia', 'Cirugía'),
        ('emergencia', 'Emergencia'),
        ('control', 'Control'),
        ('grooming', 'Peluquería'),
    )
    
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_inicio = models.TimeField(null=True, blank=True)
    hora_fin = models.TimeField(null=True, blank=True)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='programada')
    motivo = models.TextField()
    notas = models.TextField(blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Cita'
        verbose_name_plural = 'Citas'
        ordering = ['-fecha', '-hora_inicio']
        
    def __str__(self):
        return f"{self.paciente} - {self.get_tipo_display()} ({self.fecha} {self.hora_inicio})"

class HistorialMedico(models.Model):
    cita = models.OneToOneField(Cita, on_delete=models.CASCADE)
    diagnostico = models.TextField()
    tratamiento = models.TextField()
    medicamentos = models.TextField()
    observaciones = models.TextField(blank=True)
    proxima_cita = models.DateField(null=True, blank=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Historial Médico'
        verbose_name_plural = 'Historiales Médicos'
        ordering = ['-fecha_registro']
        
    def __str__(self):
        return f"Historial de {self.cita.paciente} - {self.cita.fecha}" 