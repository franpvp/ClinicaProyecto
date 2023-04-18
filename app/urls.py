from django.urls import path

from .views import home,registro,modPerfil,login,reservarHora,recContraseña,reclamos,confirmarReserva

urlpatterns = [
    path('', home, name="home"),
    path('registro/', registro, name="registro"),
    path('mod-perfil/', modPerfil, name="mod-perfil"),
    path('login/',login, name="login"),
    path('reservar-hora/',reservarHora,name="reservar-hora"),
    path('confirmar-reserva/<str:rut>/<str:prevision>/',confirmarReserva,name="confirmar-reserva"),
    path('rec-contraseña/', recContraseña, name="rec-contraseña"),
    path('reclamos/', reclamos, name="reclamos"),
]