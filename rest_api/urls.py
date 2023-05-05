from django.urls import path
from rest_api.views import lista_reg_usuarios, lista_reg_medicos, reg_usuario_mod
from rest_api.views_login import login

urlpatterns = [
    path('lista_reg_usuarios/',lista_reg_usuarios,name="lista_reg_usuarios"),
    path('lista_reg_medicos/',lista_reg_medicos, name="lista_reg_medicos"),
    path('reg_usuario_mod/<id>', reg_usuario_mod, name="reg_usuario_mod"),
    path('login/',login, name="login"),
]