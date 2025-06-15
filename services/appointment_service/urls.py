from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/citas', views.CitaViewSet, basename='cita')
router.register(r'api/historiales', views.HistorialMedicoViewSet, basename='historialmedico')

urlpatterns = [
    path('listar/', views.listar_citas, name='listar_citas'),
    path('crear/', views.crear_cita, name='crear_cita'),
    path('editar/<int:pk>/', views.editar_cita, name='editar_cita'),
    path('eliminar/<int:pk>/', views.eliminar_cita, name='eliminar_cita'),
]

urlpatterns += router.urls 