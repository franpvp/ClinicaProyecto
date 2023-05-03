from django.shortcuts import render, redirect, reverse, get_object_or_404
from .forms import RegistroUserForm,ReclamoForm,ReservaForm,ConfirmarReservaForm,ModificarPerfilForm, RecuperarContraseñaForm
from django.contrib import messages
# Funciones que autentican el usuario
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from .utils import validar_rut
from .models import RegistroUsuario, TipoUsuario, Prevision, Especialidad, Medico
import requests
from googletrans import Translator


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
    tipo_prevision = Prevision.objects.all()
    context = {'tipo_prevision': tipo_prevision}
    if request.method == 'POST':
        formulario = ReservaForm(request.POST)
        if formulario.is_valid():
            rut = formulario.cleaned_data['rut_pac']
            prevision = formulario.cleaned_data['prevision']
            for prevision in tipo_prevision:
                nombre_prev = prevision.nombre_prev
            return redirect(reverse('confirmar-reserva',kwargs={'rut': rut,'prevision': nombre_prev}))
    else:
        datos["form"] = ReservaForm()
    return render(request, 'app/reservar-hora.html',context)

def confirmarReserva(request, rut, prevision):
    datos = {
        'form': ConfirmarReservaForm()
    }
    especialidades = Especialidad.objects.all()
    Medico
    
    if request.method == 'POST':
        formulario = ConfirmarReservaForm(request.POST)
        if formulario.is_valid():
            id_esp = formulario.cleaned_data['especialidad']
            especialidad = Especialidad.objects.get(pk=id_esp)
            medicos = Medico.objects.select_related('id_esp').filter(id_esp=especialidad)
            formulario.save()
            messages.success(request, "Hora agendada exitosamante")
        else:
            messages.error(request, "Error al confirmar hora")
    else:
        datos["form"] = ConfirmarReservaForm()
    
    context = {
        'rut': rut,
        'prevision': prevision,
        'especialidades': especialidades,
        'medicos': medicos,
    }

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



# Sección Modelos Api Externa
# Consulta Medicamentos
def consultasMed(request):
    context = {}
    if request.method == 'GET' and 'nombre' in request.GET:
        nombre_med = request.GET['nombre']
        if nombre_med:
            translator = Translator()
            nombre_med_en = translator.translate(nombre_med, dest='en').text

            url = f'https://api.fda.gov/drug/label.json?search=openfda.brand_name:"{nombre_med_en}"&limit=1'
            response = requests.get(url)
            if response is not None and response.status_code == 200:
                data = response.json()
                if data is not None:
                    marca = data['results'][0]['openfda']['brand_name'][0]
                    descripcion = data['results'][0]['indications_and_usage'][0]
                    ingredientes = data['results'][0]['active_ingredient'][0]

                    marca_es = translator.translate(marca, dest='es').text
                    descripcion_es = translator.translate(descripcion, dest='es').text
                    ingredientes_es = translator.translate(ingredientes, dest='es').text

                    context = {
                        'marca': marca_es,
                        'descripcion': descripcion_es,
                        'ingredientes': ingredientes_es,
                    }
                else:
                    messages.error(request, 'No se encontraron datos')
            else:
                messages.error(request, 'Ingrese un medicamento')
        else:
            messages.error(request, "Ingrese medicamento")

    return render(request, 'app/consultas-medicamentos.html', context)

# Falta arreglar la API
def consultasCovid19(request):
    context = {}
    if request.method == 'GET' and 'pais' in request.GET:
        pais_es = request.GET.get('pais')
        if pais_es:
            translator = Translator()
            pais_en = translator.translate(pais_es, dest='en').text
            url = f"https://api.covid19tracker.ca/reports?region={pais_en}"
            response = requests.get(url)

            if response is not None and response.status_code == 200:
                data = response.json()
                if 'data' in data and len(data['data']) > 0:
                    latest_data = data['data'][-1]
                    casos_totales = latest_data['total_cases']
                    total_muertes = latest_data['total_fatalities']
                    total_recuperaciones = latest_data['total_recoveries']

                    context = {
                            'pais': pais_es.capitalize(),
                            'casos_totales': casos_totales,
                            'total_muertes': total_muertes,
                            'total_recuperaciones': total_recuperaciones,
                    }
                else:
                    messages.error(request, 'No se encontraron datos para el país especificado.')
            else:
                messages.error(request, 'Hubo un error al buscar los datos para el país especificado.')
        else:
            messages.error(request, "Ingrese pais")

    return render(request, 'app/consultas-covid.html', context)
