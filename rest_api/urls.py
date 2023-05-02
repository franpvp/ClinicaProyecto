from django.urls import path
from rest_api.views import lista_reg_usuarios, lista_reg_medicos

urlpatterns = [
    path('lista_reg_usuarios/',lista_reg_usuarios,name="lista_reg_usuarios"),
    path('lista_reg_medicos/',lista_reg_medicos, name="lista_reg_medicos"),
]