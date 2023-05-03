from django.urls import path

from .views import home,registro,modPerfil,login,reservarHora,recContraseña,reclamos,confirmarReserva,consultasMed, consultasCovid19

urlpatterns = [
    path('', home, name="home"),
    path('registro/', registro, name="registro"),
    path('mod-perfil/', modPerfil, name="mod-perfil"),
    path('login/',login, name="login"),
    path('reservar-hora/',reservarHora,name="reservar-hora"),
    path('confirmar-reserva/<str:rut>/<str:prevision>/',confirmarReserva,name="confirmar-reserva"),
    path('rec-contraseña/', recContraseña, name="rec-contraseña"),
    path('reclamo/', reclamos, name="reclamo"),
    path('consulta-med/',consultasMed,name="consulta-med"),
    path('consulta-covid/', consultasCovid19, name="consulta-covid"),
]