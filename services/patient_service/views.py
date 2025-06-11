from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Paciente
import json

@csrf_exempt
@login_required
def patient_list(request):
    if request.method == 'GET':
        patients = Paciente.objects.all()
        data = [{
            'id': patient.id,
            'nombre': patient.nombre,
            'especie': patient.especie,
            'raza': patient.raza,
            'fecha_nacimiento': patient.fecha_nacimiento,
            'peso': str(patient.peso),
            'propietario': patient.propietario,
            'telefono_propietario': patient.telefono_propietario,
            'direccion_propietario': patient.direccion_propietario,
            'fecha_registro': patient.fecha_registro,
            'notas': patient.notas
        } for patient in patients]
        return JsonResponse({'status': 'success', 'patients': data})
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        patient = Paciente.objects.create(
            nombre=data['nombre'],
            especie=data['especie'],
            raza=data['raza'],
            fecha_nacimiento=data.get('fecha_nacimiento'),
            peso=data.get('peso'),
            propietario=data['propietario'],
            telefono_propietario=data['telefono_propietario'],
            direccion_propietario=data['direccion_propietario'],
            notas=data.get('notas', '')
        )
        return JsonResponse({
            'status': 'success',
            'patient': {
                'id': patient.id,
                'nombre': patient.nombre,
                'especie': patient.especie,
                'raza': patient.raza,
                'fecha_nacimiento': patient.fecha_nacimiento,
                'peso': str(patient.peso),
                'propietario': patient.propietario,
                'telefono_propietario': patient.telefono_propietario,
                'direccion_propietario': patient.direccion_propietario,
                'fecha_registro': patient.fecha_registro,
                'notas': patient.notas
            }
        })

@csrf_exempt
@login_required
def patient_detail(request, patient_id):
    try:
        patient = Paciente.objects.get(id=patient_id)
    except Paciente.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'Paciente no encontrado'
        }, status=404)

    if request.method == 'GET':
        return JsonResponse({
            'status': 'success',
            'patient': {
                'id': patient.id,
                'nombre': patient.nombre,
                'especie': patient.especie,
                'raza': patient.raza,
                'fecha_nacimiento': patient.fecha_nacimiento,
                'peso': str(patient.peso),
                'propietario': patient.propietario,
                'telefono_propietario': patient.telefono_propietario,
                'direccion_propietario': patient.direccion_propietario,
                'fecha_registro': patient.fecha_registro,
                'notas': patient.notas
            }
        })
    
    elif request.method == 'PUT':
        data = json.loads(request.body)
        patient.nombre = data.get('nombre', patient.nombre)
        patient.especie = data.get('especie', patient.especie)
        patient.raza = data.get('raza', patient.raza)
        patient.fecha_nacimiento = data.get('fecha_nacimiento', patient.fecha_nacimiento)
        patient.peso = data.get('peso', patient.peso)
        patient.propietario = data.get('propietario', patient.propietario)
        patient.telefono_propietario = data.get('telefono_propietario', patient.telefono_propietario)
        patient.direccion_propietario = data.get('direccion_propietario', patient.direccion_propietario)
        patient.notas = data.get('notas', patient.notas)
        patient.save()
        return JsonResponse({
            'status': 'success',
            'patient': {
                'id': patient.id,
                'nombre': patient.nombre,
                'especie': patient.especie,
                'raza': patient.raza,
                'fecha_nacimiento': patient.fecha_nacimiento,
                'peso': str(patient.peso),
                'propietario': patient.propietario,
                'telefono_propietario': patient.telefono_propietario,
                'direccion_propietario': patient.direccion_propietario,
                'fecha_registro': patient.fecha_registro,
                'notas': patient.notas
            }
        })
    
    elif request.method == 'DELETE':
        patient.delete()
        return JsonResponse({
            'status': 'success',
            'message': 'Paciente eliminado correctamente'
        }) 