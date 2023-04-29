from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import RegistroUserForm,ReclamoForm,ReservaForm,ConfirmarReservaForm,ModificarPerfilForm, RecuperarContraseñaForm
from django.contrib import messages
# Funciones que autentican el usuario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from .utils import validar_rut, getPrev
from .models import RegistroUsuario, TipoUsuario

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
            nombres = formulario.cleaned_data['nombres']
            apellidos = formulario.cleaned_data['apellidos']
            correo = formulario.cleaned_data['correo']
            nombre_usuario = formulario.cleaned_data['nombre_usuario']
            contraseña = formulario.cleaned_data['contraseña']
            repetir_contraseña = formulario.cleaned_data['repetir_contraseña']
            direccion = formulario.cleaned_data['direccion']
            fecha_nacimiento = formulario.cleaned_data['fecha_nacimiento']
            
            if len(contraseña) > 8 and len(contraseña) < 15:
                if contraseña != repetir_contraseña:
                    messages.error(request, 'Las contraseñas no coinciden')
                    if nombres == '' and apellidos == '' and correo == '' and nombre_usuario == '' and direccion == '' and fecha_nacimiento == '':
                        messages.error(request, 'Debe llenar todos los campos')
                else:
                    formulario.save()
                    messages.success(request, 'Usuario registrado exitosamente')
            else:
                messages.error(request, 'La contraseña debe tener al menos 8 carácteres y un máximo de 15 carácteres')
            
            # Crear nuevo usuario
            user = User.objects.create_user(
                username = formulario.cleaned_data.get("nombre_usuario"),
                password = formulario.cleaned_data.get("contraseña")
            )
            user.save()
            # Mensaje usuario creado correctamente

            usuario = authenticate(
                username = user.username,
                password = user.password
            )

            # Logeamos al usuario creado
            if usuario is not None:
                login(request, usuario)
                return redirect(to='home')
            
    else:
        datos["form"] = RegistroUserForm()

    return render(request, 'app/registro.html', datos)


def modPerfil(request):
    usuario = request.user.username
    registro = get_object_or_404(RegistroUsuario,nombre_usuario = usuario)
    print('registro: ', registro)
    if request.method == 'POST':
        formulario = RegistroUserForm(request.POST, instance=registro)
        nombres_input = request.POST.get('nombres')
        apellidos_input = request.POST.get('apellidos')
        correo_input = request.POST.get('correo')
        direccion_input = request.POST.get('direccion')
        # Actualizar la base de datos con los nuevos valores
        registro.nombres = nombres_input
        registro.apellidos = apellidos_input
        registro.correo = correo_input
        registro.direccion = direccion_input
        registro.save()
        messages.success(request, "Los cambios se han guardado exitosamente.")
    else:
        formulario = RegistroUserForm(instance=registro)

    return render(request, 'app/mod-perfil.html', {'form': formulario, 'registro': registro})

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
    if request.method == 'POST':
        formulario = RecuperarContraseñaForm(request.POST)
        if formulario.is_valid():
            # Variables
            correo = formulario.cleaned_data['correo']
            datos = RegistroUsuario.objects.get(correo=correo)
            contraseña_nueva = formulario.cleaned_data['contraseña_nueva']
            confirmar_contraseña = formulario.cleaned_data['confirmar_contraseña']
            if contraseña_nueva == confirmar_contraseña:
                usuario = User.objects.get(username = datos.nombre_usuario)
                datos.contraseña = contraseña_nueva
                usuario.set_password(contraseña_nueva)
                # Se guarda usuario con la nueva contraseña
                usuario.save()
                # También se guardan cambios en RegistroUsuario
                datos.save()
                messages.success(request,'Contraseña Actualizada')
            else:
                messages.error(request,'Las contraseñas no coinciden')
    return render(request, 'app/rec-contraseña.html')

def reclamos(request):
    datos = {
        'form': ReclamoForm()
    }
    tipo_usuarios = TipoUsuario.objects.all()
    context = {'tipo_usuarios': tipo_usuarios}
    if request.method == 'POST':
        formulario = ReclamoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Se ha enviado el reclamo exitosamente')
        else:
            messages.error(request, 'Error al enviar el reclamo')
            
    else:
        datos["form"] = ReclamoForm()
    return render(request, 'app/reclamos.html', context)
