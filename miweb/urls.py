from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),          # Ruta para el admin de Django
    path('', include('principal.urls')),     # ✅ ¡Incluye TODAS las URLs de tu app "principal"!
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Para archivos multimedia