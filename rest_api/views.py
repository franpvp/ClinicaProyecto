from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from app.models import RegistroUsuario
from .serializers import RegistroUsuarioSerializers

# Create your views here.
@csrf_exempt
@api_view(['GET','POST'])
# Lista de usuarios registrados
def lista_reg_usuarios(request):
    if request.method == 'GET':
        reg_usuario =  RegistroUsuario.objects.all()
        serializer = RegistroUsuarioSerializers(reg_usuario, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RegistroUsuarioSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status = status.HTTP_400_BAD_REQUEST)