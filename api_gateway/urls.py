from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/auth/login/', permanent=False), name='index'),
    path('auth/', include('services.auth_service.urls')),
    path('patients/', include('services.patient_service.urls')),
    path('appointments/', include('services.appointment_service.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 