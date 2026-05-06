from django.contrib import admin
from .models import Categoria, Ticket

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    # Campos que se muestran en la lista del admin
    list_display = ('titulo', 'usuario', 'categoria', 'estado', 'fecha_creacion')
    
    # Filtros laterales
    list_filter = ('estado', 'categoria', 'fecha_creacion')
    
    # Buscador por título y descripción
    search_fields = ('titulo', 'descripcion')
    
    # Campos de solo lectura para el admin (opcional, para mayor seguridad)
    # En este caso, permitimos editar estado y respuesta_admin como pide la prueba.
    readonly_fields = ('usuario', 'fecha_creacion', 'titulo', 'descripcion', 'categoria')
    
    # Organización del formulario de edición en el admin
    fieldsets = (
        ('Información del Ticket', {
            'fields': ('usuario', 'titulo', 'descripcion', 'categoria', 'fecha_creacion')
        }),
        ('Gestión Administrativa', {
            'fields': ('estado', 'respuesta_admin'),
        }),
    )

    def has_add_permission(self, request):
        # Normalmente los tickets los crean los usuarios, 
        # pero dejamos que el admin pueda si es necesario.
        return True
