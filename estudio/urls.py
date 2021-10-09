from django.urls import path

from estudio import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('quienessomos', views.quienessomos, name='QuienesSomos'),
    path('servicio', views.servicio, name='Servicio'),
    path('contacto', views.contacto, name='Contacto'),
]