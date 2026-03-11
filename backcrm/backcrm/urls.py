from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('', include('produits.urls')),
    path('', include('clients.urls')),
    path('', include('fournisseurs.urls')),
    path('', include('archives.urls')),
]
