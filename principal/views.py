from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def inicio(request):
    return render(request, 'inicio.html')

def servicios(request):
    return render(request, 'servicios.html')

def contacto(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        mensaje = request.POST.get('mensaje')

        try:
            # Enviar correo electrónico
            send_mail(
                subject=f'Mensaje de contacto de {nombre}',
                message=f'''
                Nombre: {nombre}
                Correo: {correo}
                Mensaje:
                {mensaje}
                ''',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['silviagrosascol@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, '¡Mensaje enviado correctamente!')
            return redirect('inicio')
        
        except Exception as e:
            messages.error(request, f'Error al enviar el mensaje: {str(e)}')
            return redirect('contacto')
    
    return render(request, 'contacto.html')