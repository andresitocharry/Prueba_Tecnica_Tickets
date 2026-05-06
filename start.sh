#!/bin/bash

# Aplicar migraciones
echo "Aplicando migraciones..."
python manage.py migrate --noinput

# Cargar datos iniciales
echo "Cargando datos de prueba..."
python manage.py loaddata initial_data.json

# Iniciar servidor
echo "Iniciando Gunicorn..."
gunicorn ticket_system.wsgi:application --bind 0.0.0.0:10000
