from rest_framework import viewsets
from .models import Veterinario, HorarioTrabajo
from .serializers import VeterinarioSerializer, HorarioTrabajoSerializer

class VeterinarioViewSet(viewsets.ModelViewSet):
    queryset = Veterinario.objects.all()
    serializer_class = VeterinarioSerializer

class HorarioTrabajoViewSet(viewsets.ModelViewSet):
    queryset = HorarioTrabajo.objects.all()
    serializer_class = HorarioTrabajoSerializer 