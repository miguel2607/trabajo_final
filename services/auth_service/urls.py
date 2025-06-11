from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='auth_logout'),
    path('user/', views.get_user_info, name='auth_user_info'),
    path('dashboard/', views.dashboard, name='dashboard'),
] 