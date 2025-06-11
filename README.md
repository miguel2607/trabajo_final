# Sistema de Gestión Veterinaria

Sistema de gestión para clínicas veterinarias desarrollado con Django y arquitectura de microservicios.

## Características

- Autenticación de usuarios
- Gestión de pacientes
- Gestión de citas
- Panel de administración
- Interfaz moderna y responsiva

## Requisitos

- Python 3.8+
- Django 5.0+
- MySQL/MariaDB

## Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/tu-usuario/veterinaria-humboldt.git
cd veterinaria-humboldt
```

2. Crear y activar entorno virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # En Windows: .venv\Scripts\activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar la base de datos:
```bash
python manage.py migrate
```

5. Crear superusuario:
```bash
python manage.py createsuperuser
```

6. Iniciar el servidor:
```bash
python manage.py runserver
```

## Estructura del Proyecto

- `api_gateway/`: Gateway API para los microservicios
- `services/`: Microservicios
  - `auth_service/`: Servicio de autenticación
  - `patient_service/`: Servicio de gestión de pacientes
  - `appointment_service/`: Servicio de gestión de citas
- `templates/`: Plantillas HTML
- `static/`: Archivos estáticos (CSS, JS, imágenes)

## Licencia

Este proyecto está bajo la Licencia MIT. 