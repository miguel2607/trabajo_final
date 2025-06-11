from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Cita
from services.patient_service.models import Paciente
from services.auth_service.models import Usuario
import json
from datetime import datetime

@csrf_exempt
@login_required
def appointment_list(request):
    if request.method == 'GET':
        appointments = Cita.objects.all()
        data = [{
            'id': appointment.id,
            'paciente': {
                'id': appointment.paciente.id,
                'nombre': appointment.paciente.nombre,
                'especie': appointment.paciente.especie
            },
            'veterinario': appointment.veterinario.username,
            'fecha': appointment.fecha,
            'hora': appointment.hora,
            'tipo': appointment.tipo,
            'estado': appointment.estado,
            'notas': appointment.notas
        } for appointment in appointments]
        return JsonResponse({'status': 'success', 'appointments': data})
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            paciente = Paciente.objects.get(id=data['paciente_id'])
            veterinario = Usuario.objects.get(id=data['veterinario_id'])
            appointment = Cita.objects.create(
                paciente=paciente,
                veterinario=veterinario,
                fecha=data['fecha'],
                hora=data['hora'],
                tipo=data['tipo'],
                estado=data.get('estado', 'pendiente'),
                notas=data.get('notas', '')
            )
            return JsonResponse({
                'status': 'success',
                'appointment': {
                    'id': appointment.id,
                    'paciente': {
                        'id': appointment.paciente.id,
                        'nombre': appointment.paciente.nombre,
                        'especie': appointment.paciente.especie
                    },
                    'veterinario': appointment.veterinario.username,
                    'fecha': appointment.fecha,
                    'hora': appointment.hora,
                    'tipo': appointment.tipo,
                    'estado': appointment.estado,
                    'notas': appointment.notas
                }
            })
        except Paciente.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'message': 'Paciente no encontrado'
            }, status=404)
        except Usuario.DoesNotExist:
            return JsonResponse({
                'status': 'error',
                'message': 'Veterinario no encontrado'
            }, status=404)

@csrf_exempt
@login_required
def appointment_detail(request, appointment_id):
    try:
        appointment = Cita.objects.get(id=appointment_id)
    except Cita.DoesNotExist:
        return JsonResponse({
            'status': 'error',
            'message': 'Cita no encontrada'
        }, status=404)

    if request.method == 'GET':
        return JsonResponse({
            'status': 'success',
            'appointment': {
                'id': appointment.id,
                'paciente': {
                    'id': appointment.paciente.id,
                    'nombre': appointment.paciente.nombre,
                    'especie': appointment.paciente.especie
                },
                'veterinario': appointment.veterinario.username,
                'fecha': appointment.fecha,
                'hora': appointment.hora,
                'tipo': appointment.tipo,
                'estado': appointment.estado,
                'notas': appointment.notas
            }
        })
    
    elif request.method == 'PUT':
        data = json.loads(request.body)
        appointment.fecha = data.get('fecha', appointment.fecha)
        appointment.hora = data.get('hora', appointment.hora)
        appointment.tipo = data.get('tipo', appointment.tipo)
        appointment.estado = data.get('estado', appointment.estado)
        appointment.notas = data.get('notas', appointment.notas)
        appointment.save()
        return JsonResponse({
            'status': 'success',
            'appointment': {
                'id': appointment.id,
                'paciente': {
                    'id': appointment.paciente.id,
                    'nombre': appointment.paciente.nombre,
                    'especie': appointment.paciente.especie
                },
                'veterinario': appointment.veterinario.username,
                'fecha': appointment.fecha,
                'hora': appointment.hora,
                'tipo': appointment.tipo,
                'estado': appointment.estado,
                'notas': appointment.notas
            }
        })
    
    elif request.method == 'DELETE':
        appointment.delete()
        return JsonResponse({
            'status': 'success',
            'message': 'Cita eliminada correctamente'
        }) 