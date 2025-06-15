from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/veterinarios', views.VeterinarioViewSet, basename='veterinario')
router.register(r'api/horarios', views.HorarioTrabajoViewSet, basename='horariotrabajo')

urlpatterns = [
    path('listar/', views.listar_veterinarios, name='listar_veterinarios'),
    path('crear/', views.crear_veterinario, name='crear_veterinario'),
    path('editar/<int:pk>/', views.editar_veterinario, name='editar_veterinario'),
    path('eliminar/<int:pk>/', views.eliminar_veterinario, name='eliminar_veterinario'),
]

urlpatterns += router.urls 