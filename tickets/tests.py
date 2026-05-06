from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Ticket, Categoria

class TicketSecurityTests(TestCase):
    def setUp(self):
        # Crear categorías y usuarios de prueba
        self.cat = Categoria.objects.create(nombre="Soporte")
        self.user_a = User.objects.create_user(username='user_a', password='password123')
        self.user_b = User.objects.create_user(username='user_b', password='password123')
        
        # Crear un ticket para el usuario A
        self.ticket_a = Ticket.objects.create(
            usuario=self.user_a,
            titulo="Ticket de A",
            descripcion="Privado",
            categoria=self.cat
        )

    def test_unauthenticated_redirect(self):
        """Verificar que usuarios no logueados son redirigidos al login."""
        response = self.client.get(reverse('ticket_listar'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/login/', response.url)

    def test_user_cannot_see_other_user_ticket_detail(self):
        """Verificar que el usuario B no puede ver el detalle del ticket del usuario A."""
        self.client.login(username='user_b', password='password123')
        url = reverse('ticket_detalle', kwargs={'pk': self.ticket_a.pk})
        response = self.client.get(url)
        # Debe retornar 404 porque filtramos por usuario en la vista
        self.assertEqual(response.status_code, 404)

    def test_user_list_only_shows_own_tickets(self):
        """Verificar que la lista solo muestra los tickets del usuario logueado."""
        # Crear un ticket para el usuario B
        Ticket.objects.create(
            usuario=self.user_b,
            titulo="Ticket de B",
            descripcion="Privado",
            categoria=self.cat
        )
        
        self.client.login(username='user_a', password='password123')
        response = self.client.get(reverse('ticket_listar'))
        
        # En la lista de A solo debe haber 1 ticket (el suyo)
        self.assertEqual(len(response.context['tickets']), 1)
        self.assertEqual(response.context['tickets'][0].titulo, "Ticket de A")
