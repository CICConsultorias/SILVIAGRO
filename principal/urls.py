from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),          # Ruta de inicio
    path('servicios/', views.servicios, name='servicios'),  # Ruta de servicios
    path('contacto/', views.contacto, name='contacto'),     # ✨ Nueva ruta del formulario
]