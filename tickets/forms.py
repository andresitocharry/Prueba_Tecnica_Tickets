from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        # Solo mostramos los campos que el usuario debe llenar
        fields = ['titulo', 'descripcion', 'categoria']
        
        # Añadimos clases de Bootstrap para que se vea bien
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. No funciona mi correo'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe tu problema detalladamente...'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
        }
