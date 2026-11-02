from django.urls import path
from . import views

urlpatterns = [
    path ('', views.index , name='index'),
    path('crear_piloto/', views.crear_piloto, name='crear_piloto'),
    path('editar_piloto/<str:documento>', views.editar_piloto, name='editar_piloto'),
    path('eliminar_piloto/<str:documento>', views.eliminar_piloto, name='eliminar_piloto'),


]