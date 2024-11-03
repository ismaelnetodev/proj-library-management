from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from livros import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('livros/', include('livros.urls')),
    path('auth/', include('usuarios.urls')),
    path('', views.redirect_root, name="redirect_root"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)