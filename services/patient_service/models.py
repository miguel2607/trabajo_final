from django.db import models

class Paciente(models.Model):
    ESPECIES = (
        ('perro', 'Perro'),
        ('gato', 'Gato'),
        ('ave', 'Ave'),
        ('otro', 'Otro'),
    )
    
    nombre = models.CharField(max_length=100)
    especie = models.CharField(max_length=20, choices=ESPECIES)
    raza = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    propietario = models.CharField(max_length=100)
    telefono_propietario = models.CharField(max_length=15)
    direccion_propietario = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    notas = models.TextField(blank=True)
    
    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
        ordering = ['-fecha_registro']
        
    def __str__(self):
        return f"{self.nombre} ({self.get_especie_display()}) - {self.propietario}" 