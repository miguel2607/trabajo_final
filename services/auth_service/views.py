from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return JsonResponse({'status': 'error', 'message': 'Credenciales inválidas'}, status=400)

@login_required
def logout_view(request):
    logout(request)
    return JsonResponse({
        'status': 'success',
        'message': 'Logout successful'
    })

@login_required
def get_user_info(request):
    user = request.user
    return JsonResponse({
        'status': 'success',
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email
        }
    })

@login_required
def dashboard(request):
    return render(request, 'login/dashboard.html') 