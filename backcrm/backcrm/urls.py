from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('', include('inventaire.urls')),
    path('', include('nectarcrm.urls')),
    path('', include('archives.urls')),
]
