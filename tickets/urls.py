from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [

    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', views.registro, name='registro'),

    path('ticket/crear/', views.ticket_crear, name='ticket_crear'),
    path('mis-tickets/', views.ticket_listar, name='ticket_listar'),
    path('mis-tickets/<int:pk>/', views.ticket_detalle, name='ticket_detalle'),

    path('', views.ticket_listar, name='home'),
]
