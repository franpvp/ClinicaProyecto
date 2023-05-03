from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from app.models import RegistroUsuario, Medico
from .serializers import RegistroUsuarioSerializers, MedicoSerializers

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
        
#Lista de Medicos Registrados:
@csrf_exempt
@api_view(['GET','POST'])
def lista_reg_medicos(request):
    if request.method == 'GET':
        medico = Medico.objects.all()
        serializer = MedicoSerializers(medico, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MedicoSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.error, status= status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET','PUT','DELETE'])    
def reg_usuario_mod(request,id):
    try:
        usuario = RegistroUsuario.objects.get(id_user = id)
    except:
        return Response(status= status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RegistroUsuarioSerializers(usuario)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RegistroUsuarioSerializers(usuario, data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        usuario.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)