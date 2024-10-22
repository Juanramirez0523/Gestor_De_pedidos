
from django.contrib import admin
from django.urls import path,include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ProyectoWebApp.urls')),
    path('blog/', include('blog.urls')),
    path('servicios/', include('servicios.urls')),
    path('contacto/', include('contacto.urls')),
    path('tienda/', include('tienda.urls')),
    path('carro/', include('carro.urls')),

    
]
