from django.db import models
from django.conf import settings

class Reporte(models.Model):
    TIPOS = (
        ('ventas', 'Reporte de Ventas'),
        ('inventario', 'Reporte de Inventario'),
        ('citas', 'Reporte de Citas'),
        ('pacientes', 'Reporte de Pacientes'),
        ('veterinarios', 'Reporte de Veterinarios'),
        ('financiero', 'Reporte Financiero'),
    )
    
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPOS)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    parametros = models.JSONField(default=dict)  # Para almacenar filtros y configuraciones
    archivo = models.FileField(upload_to='reportes/', null=True, blank=True)
    fecha_generacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name = 'Reporte'
        verbose_name_plural = 'Reportes'
        ordering = ['-fecha_generacion']
        
    def __str__(self):
        return f"{self.get_tipo_display()} - {self.fecha_inicio} a {self.fecha_fin}"

class PlantillaReporte(models.Model):
    nombre = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=Reporte.TIPOS)
    descripcion = models.TextField()
    configuracion = models.JSONField(default=dict)  # Para almacenar la configuración de la plantilla
    activa = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_actualizacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Plantilla de Reporte'
        verbose_name_plural = 'Plantillas de Reportes'
        ordering = ['nombre']
        
    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()})" 