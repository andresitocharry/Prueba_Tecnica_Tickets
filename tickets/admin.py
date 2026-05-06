from django.contrib import admin
from .models import Categoria, Ticket


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'usuario', 'categoria', 'estado', 'fecha_creacion')
    list_filter = ('estado', 'categoria', 'fecha_creacion')
    search_fields = ('titulo', 'descripcion', 'usuario__username')
    readonly_fields = ('usuario', 'fecha_creacion')

    fieldsets = (
        ('Información del Ticket', {
            'fields': ('titulo', 'descripcion', 'categoria', 'usuario', 'fecha_creacion')
        }),
        ('Gestión Administrativa', {
            'fields': ('estado', 'respuesta_admin'),
        }),
    )

    def save_model(self, request, obj, form, change):
        # Asegurar que el usuario no cambie al editar desde el admin
        if not change:
            obj.usuario = request.user
        super().save_model(request, obj, form, change)
