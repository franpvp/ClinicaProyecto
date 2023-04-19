from django.urls import path

from .views import home, registro, modPerfil, reservarHora, recContraseña, reclamos, confirmarReserva, loginUser

urlpatterns = [
    path('', home, name="home"),
    path('registro/', registro, name="registro"),
    path('mod-perfil/', modPerfil, name="mod-perfil"),
    path('reservar-hora/',reservarHora,name="reservar-hora"),
    path('confirmar-reserva/<str:rut>/<str:prevision>/',confirmarReserva,name="confirmar-reserva"),
    path('rec-contraseña/', recContraseña, name="rec-contraseña"),
    path('reclamos/', reclamos, name="reclamos"),
    path('login/', loginUser, name="loginUser" )
]