from django.urls import path
from . import views

urlpatterns = [
    path('', views.registrar, name='registrar'),
    path('lista/', views.lista, name='lista'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('excluir/<int:id>/', views.excluir, name='excluir'),
    path('identificar/', views.identificar, name='identificar'),
    path('sair/', views.sair, name='sair'),
]
