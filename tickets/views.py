from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Ticket, Categoria

@login_required
def ticket_listar(request):
    """Listado de tickets creados por el usuario autenticado."""
    tickets = Ticket.objects.filter(usuario=request.user)
    return render(request, 'lista_tickets.html', {'tickets': tickets})

@login_required
def ticket_detalle(request, pk):
    """Detalle de un ticket específico."""
    ticket = get_object_or_404(Ticket, pk=pk, usuario=request.user)
    return render(request, 'detalle_ticket.html', {'ticket': ticket})

@login_required
def ticket_crear(request):
    """Formulario para crear un nuevo ticket."""
    return render(request, 'crear_ticket.html')
