from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Ticket
from .forms import TicketForm


def registro(request):
    """Registro de nuevos usuarios."""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}. ¡Ya puedes iniciar sesión!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registro.html', {'form': form})


@login_required
def ticket_listar(request):
    """Listado de tickets creados por el usuario autenticado."""
    tickets = Ticket.objects.filter(usuario=request.user).order_by('-fecha_creacion')
    return render(request, 'lista_tickets.html', {'tickets': tickets})


@login_required
def ticket_detalle(request, pk):
    """Detalle de un ticket específico."""
    ticket = get_object_or_404(Ticket, pk=pk, usuario=request.user)
    return render(request, 'detalle_ticket.html', {'ticket': ticket})


@login_required
def ticket_crear(request):
    """Creación de un nuevo ticket."""
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.usuario = request.user
            ticket.save()
            return redirect('ticket_listar')
    else:
        form = TicketForm()
    return render(request, 'crear_ticket.html', {'form': form})
