from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
    """
    Representa la categoría a la que pertenece un ticket (ej. Soporte Técnico, Facturación).
    """
    nombre = models.CharField(max_length=100, verbose_name="Nombre de la Categoría")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

class Ticket(models.Model):
    """
    Modelo principal para la gestión de tickets de soporte.
    """
    ESTADO_CHOICES = [
        ('abierto', 'Abierto'),
        ('en_espera', 'En espera'),
        ('aprobado', 'Aprobado'),
        ('rechazado', 'Rechazado'),
    ]

    usuario = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='tickets',
        verbose_name="Usuario Creador"
    )
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.PROTECT, 
        related_name='tickets',
        verbose_name="Categoría"
    )
    estado = models.CharField(
        max_length=20, 
        choices=ESTADO_CHOICES, 
        default='abierto',
        verbose_name="Estado"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    respuesta_admin = models.TextField(blank=True, null=True, verbose_name="Respuesta del Administrador")

    def __str__(self):
        return f"{self.titulo} - {self.get_estado_display()}"

    class Meta:
        ordering = ['-fecha_creacion']
        verbose_name = "Ticket"
        verbose_name_plural = "Tickets"
