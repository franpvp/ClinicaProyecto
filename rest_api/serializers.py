from rest_framework import serializers
from app.models import RegistroUsuario

class RegistroUsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = RegistroUsuario
        fields = '__all__'