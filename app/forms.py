from django import forms
from .models import RegistroUsuario,LoginUser,Reclamo,ReservarHora,ConfirmarReserva,Especialidad,ModificarPerfil,RecuperarContraseña, ConsultaMed, ConsultaCovid19
from django.forms import ModelForm

# Clase del formulario de registro
class RegistroUserForm(ModelForm):

    class Meta:
        model = RegistroUsuario
        fields = ['id_user','nombres','apellidos','correo','nombre_usuario','contraseña',
                  'repetir_contraseña','direccion','fecha_nacimiento']
    
        widgets = {
            'id_user': forms.TextInput(attrs={'class':'form-control'}),
            'nombres': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.TextInput(attrs={'class':'form-control'}),
            'nombre_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'contraseña': forms.TextInput(attrs={'class':'form-control'}),
            'repetir_contraseña': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class':'form-control'}),
        }

class LoginUserForm(ModelForm):

    class Meta:
        model = LoginUser
        fields = '__all__'
    
class ReclamoForm(ModelForm):

    class Meta:
        model = Reclamo
        fields = '__all__'


class ReservaForm(ModelForm):

    class Meta:
        model = ReservarHora
        fields = ['rut','prevision']

        widgets = {
            'rut': forms.TextInput(attrs={'class':'form-control'}),
            'prevision': forms.Select(attrs={'class':'form-control'}),
        }


class ConfirmarReservaForm(ModelForm):

    class Meta:
        model = ConfirmarReserva
        fields = '__all__'

        widgets = {
            'id_res': forms.TextInput(attrs={'class': 'form-control'}),
            'rut': forms.TextInput(attrs={'class': 'form-control'}),
            'prevision': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_medico': forms.TextInput(attrs={'class': 'form-control'}),
            'id_esp': forms.TextInput(attrs={'class': 'form-control'}),
            'dia_agendado': forms.DateInput(attrs={'class': 'form-control'}),
            'hora_agendada': forms.TimeInput(attrs={'class': 'form-control'}),
            
        }


class RecuperarContraseñaForm(ModelForm):

    class Meta:
        model = RecuperarContraseña
        fields = '__all__'

        widgets = {
            'correo': forms.TextInput(attrs={'class':'form-control'}),
        }

class ModificarPerfilForm(ModelForm):

    class Meta:
        model = ModificarPerfil
        fields = '__all__'

        widgets = {
            'nombres': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'correo': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
        }

class ConsultaMedForm(ModelForm):

    class Meta:
        model = ConsultaMed
        fields = '__all__'

class ConsultaCovidForm(ModelForm):

    class Meta:
        model = ConsultaCovid19
        fields = '__all__'