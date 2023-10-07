from django.urls import path
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cursos/', views.cursos, name='cursos'),
    path('entrada/', views.entrada, name='entrada'),
    path('contacto/', views.contacto,name='contacto'),
    path('nosotros', views.nosotros,name='nosotros'),
]