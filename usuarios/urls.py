from django.urls import path
from . import views


urlpatterns = [
    path('loguin/', views.loguin, name='loguin'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('valida-cadastro/', views.valida_cadastro, name='valida_cadastro'),
    path('validar-loguin/', views.valida_loguin, name='validar_loguin'),
    path('sair/', views.sair, name='sair')
]
