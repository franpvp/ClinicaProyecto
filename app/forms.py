from django import forms
from .models import RegistroUsuario,Reclamo,ReservarHora,ConfirmarReserva,ModificarPerfil,RecuperarContraseña
from django.forms import ModelForm

# Clase del formulario de registro
class RegistroUserForm(ModelForm):

    class Meta:
        model = RegistroUsuario
        fields = ['nombres','apellidos','correo','nombre_usuario','contraseña',
                  'repetir_contraseña','direccion','fecha_nacimiento']
    
        widget = {
            'nombres': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'contraseña': forms.TextInput(attrs={'class':'form-control'}),
            'repetir_contraseña': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class':'form-control'}),
        }
    
class ReclamoForm(ModelForm):

    class Meta:
        model = Reclamo
        fields = '__all__'

        widget = {
            'id_rec':forms.TextInput(attrs={'class':'form-control'}),
            'nombres_rec': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos_rec': forms.TextInput(attrs={'class':'form-control'}),
            'rut_rec': forms.TextInput(attrs={'class':'form-control'}),
            'celular': forms.TextInput(attrs={'class':'form-control'}),
            'direccion_rec': forms.TextInput(attrs={'class':'form-control'}),
            'tipo_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'comentarios': forms.TextInput(attrs={'class':'form-control'}),
        }

class ReservaForm(ModelForm):

    class Meta:
        model = ReservarHora
        fields = '__all__'

        widget = {
            'rut_pac': forms.TextInput(attrs={'class':'form-control'}),
            'prevision': forms.TextInput(attrs={'class':'form-control'}),
        }

class ConfirmarReservaForm(ModelForm):

    class Meta:
        model = ConfirmarReserva
        fields = '__all__'

        widget = {
            'medico': forms.TextInput(attrs={'class':'form-control'}),
            'especialidad': forms.TextInput(attrs={'class':'form-control'}),
            'dia_agendado': forms.TextInput(attrs={'class':'form-control'}),
            'hora_agendada': forms.TextInput(attrs={'class':'form-control'}),

        }

class RecuperarContraseñaForm(ModelForm):

    class Meta:
        model = RecuperarContraseña
        fields = '__all__'

        widget = {
            'correo': forms.TextInput(attrs={'class':'form-control'}),
        }

class ModificarPerfilForm(ModelForm):

    class Meta:
        model = ModificarPerfil
        fields = '__all__'

        widget = {
            'nombres': forms.TextInput(attrs={'class':'form-control'}),
            'apelldos': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
        }
