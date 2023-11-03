from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_web, name='pagina_web'),
    path('inicio/', views.inicio, name='inicio'),
]
