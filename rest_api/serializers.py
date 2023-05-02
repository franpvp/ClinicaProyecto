from rest_framework import serializers
from app.models import RegistroUsuario, Medico, Reclamo

class RegistroUsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = RegistroUsuario
        fields = '__all__'
        
class MedicoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['id_med', 'rut_med', 'nombre_completo', 'id_esp']

class ReclamoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Reclamo
        fields = '__all__'