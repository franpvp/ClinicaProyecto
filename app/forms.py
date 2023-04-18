from django import forms
from .models import RegistroUsuario, Reclamos, ReservarHora, ConfirmarReserva
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
    
class ReclamosForm(ModelForm):

    class Meta:
        model = Reclamos
        fields = '__all__'

        widget = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellidos': forms.TextInput(attrs={'class':'form-control'}),
            'rut_usuario': forms.TextInput(attrs={'class':'form-control'}),
            'celular': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
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