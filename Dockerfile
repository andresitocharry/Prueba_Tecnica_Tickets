# Usar una imagen oficial de Python
FROM python:3.9-slim

# Evitar que Python genere archivos .pyc y que el buffer se sature
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Instalar dependencias de Python
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el proyecto
COPY . /app/

# Dar permisos de ejecución al script de inicio
RUN chmod +x /app/start.sh

# Ejecutar collectstatic para los archivos CSS/JS
RUN python manage.py collectstatic --no-input

# Exponer el puerto
EXPOSE 10000

# Usar el script de inicio
CMD ["/app/start.sh"]
