from django.urls import path
from . import views

urlpatterns = [
    path('the-archives/', views.the_archives, name='the_archives'),
]