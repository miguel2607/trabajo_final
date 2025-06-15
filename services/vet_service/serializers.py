from rest_framework import serializers
from .models import Veterinario, HorarioTrabajo

class VeterinarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veterinario
        fields = '__all__'

class HorarioTrabajoSerializer(serializers.ModelSerializer):
    class Meta:
        model = HorarioTrabajo
        fields = '__all__' 