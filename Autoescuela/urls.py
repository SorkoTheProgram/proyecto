from django.urls import path, include

from .views import *

#URLS APP
urlpatterns = [
    path('', index, name='index'),
    path('contacto/', contacto, name='contacto'),
    path('cursos/', cursos, name='cursos'),
    path('edicionproductos/', edicionproductos, name='edicionproductos'),
    path('editarusuario/', editarusuario, name='editarusuario'),
    path('FAQS/', FAQS, name='FAQS'),
    path('formpago/', formpago, name='formpago'),
    path('horas/', horas, name='horas'),
    path('inicioSesionEstud/', inicioSesionEstud, name='inicioSesionEstud'),
    path('interfaz_de_compra/', interfaz_de_compra, name='interfaz_de_compra'),
    path('miscompras/', miscompras, name='miscompras'),
    path('perfil/', perfil, name='perfil'),
    path('perfilAdmin/', perfilAdmin, name='perfilAdmin'),
    path('profesores/', profesores, name='profesores'),
    path('ventas/', ventas, name='ventas')

]