from django.shortcuts import render, redirect, reverse
from .forms import RegistroUserForm, ReclamosForm, ReservaForm, ConfirmarReservaForm
from django.contrib import messages
# Funciones que autentican el usuario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from .utils import validar_rut, getPrev
from .models import RegistroUsuario

# Create your views here.

def home(request):
    return render(request,'app/home.html')

def registro(request):
    datos = {
        'form': RegistroUserForm()
    }
    if request.method == 'POST':
        formulario = RegistroUserForm(request.POST)
        if formulario.is_valid():
            # Crear nuevo usuario
            user = User.objects.create_user(
                username = formulario.cleaned_data.get("nombre_usuario"),
                password = formulario.cleaned_data.get("contraseña")
            )
            formulario.save()
            user.save()
            # Mensaje usuario creado correctamente
            messages.success(request, "Usuario registrado correctamente")
            usuario = authenticate(
                username = user.username,
                password = user.password
            )

            # Logeamos al usuario creado
            if usuario is not None:
                login(request, usuario)
                return redirect(to='home')
            else:
                messages.error(request, "Nombre de usuario o contraseña incorrectos.")
            
    else:
        datos["form"] = RegistroUserForm()

    return render(request, 'app/registro.html', datos)

def modPerfil(request):
    #FUNCIONA BIEN
    if request.user.is_authenticated:
        datos = RegistroUsuario.objects.all()
        for campo in datos:
            nombres = campo.nombres
            apellidos = campo.apellidos
            correo = campo.correo
            direccion = campo.direccion
            nombre_usuario = campo.nombre_usuario
    context = {
        'nombres': nombres,
        'apellidos': apellidos,
        'correo': correo,
        'nombre_usuario': nombre_usuario,
        'direccion': direccion
    }

    return render(request, 'app/mod-perfil.html', context)

def reservarHora(request):
    datos = {
        'form': ReservaForm()
    }
    if request.method == 'POST':
        formulario = ReservaForm(request.POST)
        if formulario.is_valid():
            rut = formulario.cleaned_data['rut_pac']
            prevision = formulario.cleaned_data['prevision']
            texto = getPrev(prevision)
            return redirect(reverse('confirmar-reserva',kwargs={'rut': rut,'prevision': texto}))
    else:
        datos["form"] = ReservaForm()
    return render(request, 'app/reservar-hora.html')

def confirmarReserva(request, rut, prevision):	
    datos = {
        'form': ConfirmarReservaForm()
    }
    context = {
        'rut': rut,
        'prevision': prevision
    }
    if request.method == 'POST':
        formulario = ConfirmarReservaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Hora agendada exitosamante")
    else:
        datos["form"] = ConfirmarReservaForm()

    return render(request, 'app/confirmar-reserva.html', context)

def recContraseña(request):
    return render(request, 'app/rec-contraseña.html')

def reclamos(request):
    datos = {
        'form': ReclamosForm()
    }
    if request.method == 'POST':
        formulario = ReclamosForm(request.POST)
        if formulario.is_valid():
            rut = request.POST.get('rut')
            if validar_rut(rut):
                formulario.save()
                messages.success(request, "Rut válido")
            else:
                messages.error(request, "Rut inválido")
            
    else:
        datos["form"] = ReclamosForm()

    return render(request, 'app/reclamos.html', datos)
