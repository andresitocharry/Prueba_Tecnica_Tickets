from django.db import models
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Ticket(models.Model):
    ESTADOS = (
        ('abierto', 'Abierto'),
        ('en_espera', 'En espera'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
    )

    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoría")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='abierto')
    respuesta_admin = models.TextField(blank=True, null=True, verbose_name="Respuesta del Administrador")

    def __str__(self):
        return f"{self.titulo} ({self.get_estado_display()})"
