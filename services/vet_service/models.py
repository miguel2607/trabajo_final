from django.db import models
from django.conf import settings

class Veterinario(models.Model):
    ESPECIALIDADES = (
        ('general', 'Medicina General'),
        ('cirugia', 'Cirugía'),
        ('dermatologia', 'Dermatología'),
        ('cardiologia', 'Cardiología'),
        ('oftalmologia', 'Oftalmología'),
        ('odontologia', 'Odontología'),
        ('nutricion', 'Nutrición'),
    )
    
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=20, choices=ESPECIALIDADES)
    numero_licencia = models.CharField(max_length=50, unique=True)
    telefono = models.CharField(max_length=15)
    direccion = models.TextField()
    fecha_contratacion = models.DateField()
    activo = models.BooleanField(default=True)
    biografia = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Veterinario'
        verbose_name_plural = 'Veterinarios'
        
    def __str__(self):
        return f"Dr(a). {self.usuario.get_full_name()} - {self.get_especialidad_display()}"

class HorarioTrabajo(models.Model):
    DIAS_SEMANA = (
        (0, 'Lunes'),
        (1, 'Martes'),
        (2, 'Miércoles'),
        (3, 'Jueves'),
        (4, 'Viernes'),
        (5, 'Sábado'),
        (6, 'Domingo'),
    )
    
    veterinario = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    dia_semana = models.IntegerField(choices=DIAS_SEMANA)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    
    class Meta:
        verbose_name = 'Horario de Trabajo'
        verbose_name_plural = 'Horarios de Trabajo'
        unique_together = ['veterinario', 'dia_semana']
        
    def __str__(self):
        return f"{self.veterinario} - {self.get_dia_semana_display()} ({self.hora_inicio} - {self.hora_fin})" 