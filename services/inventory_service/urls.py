from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/categorias', views.CategoriaViewSet, basename='categoria')
router.register(r'api/productos', views.ProductoViewSet, basename='producto')
router.register(r'api/movimientos', views.MovimientoInventarioViewSet, basename='movimientoinventario')

urlpatterns = [
    path('listar/', views.listar_inventario, name='listar_inventario'),
    path('crear/', views.crear_inventario, name='crear_inventario'),
    path('editar/<int:pk>/', views.editar_inventario, name='editar_inventario'),
    path('eliminar/<int:pk>/', views.eliminar_inventario, name='eliminar_inventario'),
]

urlpatterns += router.urls 