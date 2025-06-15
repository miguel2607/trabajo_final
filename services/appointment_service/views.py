from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import Cita, HistorialMedico
from services.patient_service.models import Paciente
from services.auth_service.models import Usuario
import json
from datetime import datetime
from rest_framework import viewsets
from .serializers import CitaSerializer, HistorialMedicoSerializer
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CitaForm

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

class CitaViewSet(viewsets.ModelViewSet):
    queryset = Cita.objects.all()
    serializer_class = CitaSerializer

class HistorialMedicoViewSet(viewsets.ModelViewSet):
    queryset = HistorialMedico.objects.all()
    serializer_class = HistorialMedicoSerializer

def listar_citas(request):
    citas = Cita.objects.all()
    
    # Filtros
    fecha = request.GET.get('fecha', '')
    veterinario = request.GET.get('veterinario', '')
    paciente = request.GET.get('paciente', '')
    estado = request.GET.get('estado', '')
    
    if fecha:
        citas = citas.filter(fecha=fecha)
    if veterinario:
        citas = citas.filter(veterinario__nombre__icontains=veterinario)
    if paciente:
        citas = citas.filter(paciente__nombre__icontains=paciente)
    if estado:
        citas = citas.filter(estado=estado)
    
    # Paginación
    paginator = Paginator(citas, 10)  # 10 citas por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'appointment_service/listar_citas.html', {
        'page_obj': page_obj,
        'fecha': fecha,
        'veterinario': veterinario,
        'paciente': paciente,
        'estado': estado
    })

def crear_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_citas')
    else:
        form = CitaForm()
    
    return render(request, 'appointment_service/crear_cita.html', {
        'form': form
    })

def editar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('listar_citas')
    else:
        form = CitaForm(instance=cita)
    
    return render(request, 'appointment_service/crear_cita.html', {
        'form': form,
        'cita': cita
    })

def eliminar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        cita.delete()
        return redirect('listar_citas')
    return render(request, 'appointment_service/eliminar_cita.html', {
        'cita': cita
    }) 