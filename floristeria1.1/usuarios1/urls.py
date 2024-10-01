from django.urls import path
from . import views
from .views import registro_api, login_api

urlpatterns = [
    path('registrov/', views.registro, name='registro'),
    path('perfilv/', views.perfil, name='perfil'),
    path('registro/', registro_api, name='registro_api'),
    path('login/', login_api, name='login_api'),
]
