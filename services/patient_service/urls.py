from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/pacientes', views.PacienteViewSet, basename='paciente')

urlpatterns = [
    path('listar/', views.listar_pacientes, name='listar_pacientes'),
    path('crear/', views.crear_paciente, name='crear_paciente'),
    path('editar/<int:pk>/', views.editar_paciente, name='editar_paciente'),
    path('eliminar/<int:pk>/', views.eliminar_paciente, name='eliminar_paciente'),
]

urlpatterns += router.urls 