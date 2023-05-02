from rest_framework import serializers
from app.models import RegistroUsuario, Medico

class RegistroUsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = RegistroUsuario
        fields = '__all__'
        
class MedicoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['id_med', 'rut_med', 'nombre_completo', 'id_esp']