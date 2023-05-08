from django.db import models

# Modelo Registro de Usuario (Campos de Formulario de registro)
class RegistroUsuario(models.Model):
    id_user = models.AutoField(primary_key=True, unique=True,verbose_name="Id usuario")
    nombres = models.CharField(max_length=50, verbose_name="Nombres del usuario")
    apellidos = models.CharField(max_length=50, verbose_name="Apellidos del usuario")
    correo = models.EmailField(max_length=50, verbose_name="Correo de usuario")
    nombre_usuario = models.CharField(max_length=25, verbose_name="Nombre de usuario")
    contraseña = models.CharField(max_length=30, verbose_name="Contraseña de usuario")
    repetir_contraseña = models.CharField(max_length=30, verbose_name="Campo repetir contraseña")
    direccion = models.CharField(max_length=60, verbose_name="Dirección de usuario")
    fecha_nacimiento = models.DateField(null=True,verbose_name="Fecha de nacimiento de usuario")

    def __str__(self):
        return self.nombres
    
class LoginUser(models.Model):
    username = models.CharField(max_length=20,verbose_name="Nombre de Usuario")
    password = models.CharField(max_length=30, verbose_name="Contraseña Usuario")

    def __str__(self):
        return self.username

# Lista de opciones para variable "tipo_usuario"
class TipoUsuario(models.Model):
    id_tipo_usuario = models.IntegerField(primary_key=True, unique=True)
    nombre_tipo_usuario = models.CharField(max_length=20, verbose_name="Nombre tipo usuario")

    def __str__(self):
        return self.nombre_tipo_usuario
    
# Modelo Reclamo
class Reclamo(models.Model):
    id_reclamo = models.AutoField(primary_key=True, unique=True, verbose_name="Id reclamo")
    nombres_rec = models.CharField(max_length=50, verbose_name="Nombres usuario")
    apellidos_rec = models.CharField(max_length=50, verbose_name="Apellidos usuario")
    rut_rec = models.CharField(max_length=12, verbose_name="Rut usuario")
    celular = models.CharField(max_length=9,verbose_name="Nro celular usuario")
    direccion_rec = models.CharField(max_length=60, verbose_name="Direccion usuario")
    id_tipo_usuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)
    comentarios = models.TextField(max_length=150, verbose_name="Comentarios")

    def __str__(self):
        return self.nombres_rec
    
# Modelo Especialidad
class Especialidad(models.Model):
    id_esp = models.IntegerField(primary_key=True, verbose_name="Id especialidad")
    nombre_esp = models.CharField(max_length=30,null=False,verbose_name="Nombre de la especialidad")

    def __str__(self):
        return self.nombre_esp
    
# Modelo Médicos
class Medico(models.Model):
    id_med = models.IntegerField(primary_key=True, verbose_name="Id medico")
    rut_med = models.CharField(max_length=12,unique=True,verbose_name="Rut médico")
    nombre_completo = models.CharField(max_length=50, verbose_name="Nombre médico")

    def __str__(self):
        return self.nombre_completo

class Prevision(models.Model):
    id_prev = models.IntegerField(primary_key=True, verbose_name="Id previsión")
    nombre_prev = models.CharField(max_length=40, verbose_name="Nombre previsión")

    def __str__(self):
        return self.nombre_prev

# Modelo Reservar Hora
class ReservarHora(models.Model):
    rut = models.CharField(max_length=12,verbose_name="Rut de paciente")
    prevision = models.ForeignKey(Prevision,on_delete=models.CASCADE, verbose_name="Id previsión")

    def __str__(self):
        return self.rut

# Modelo Confirmar Reservar Hora
class ConfirmarReserva(models.Model):
    id_res = models.AutoField(primary_key=True, verbose_name="Id reserva")
    rut = models.CharField(max_length=12,verbose_name="Rut paciente")
    prevision = models.CharField(max_length=40,verbose_name="Id prevision de salud")
    nombre_medico = models.CharField(max_length=50, verbose_name="Nombre médico")
    id_esp = models.ForeignKey(Especialidad,on_delete=models.CASCADE,verbose_name="Especialidad médico")
    dia_agendado = models.DateField(null=False)
    hora_agendada = models.TimeField(null=False)
    

    def __str__(self):
        return self.rut
    
class RecuperarContraseña(models.Model):
    correo = models.CharField(max_length=50)
    contraseña_nueva = models.CharField(max_length=30)
    confirmar_contraseña = models.CharField(max_length=30)

    def __str__(self):
        return self.correo
    
class ModificarPerfil(models.Model):
    nombres = models.CharField(max_length=50, verbose_name="Nombres de usuario")
    apellidos = models.CharField(max_length=50, verbose_name="Apellidos de usuario")
    correo = models.EmailField(max_length=50, verbose_name="Correo de usuario")
    direccion = models.CharField(max_length=60, verbose_name="Dirección de usuario")

    def __str__(self):
        return self.nombres

class ConsultaMed(models.Model):
    busqueda = models.CharField(max_length=50, verbose_name="Busqueda medicamento")

    def __str__(self):
        return self.busqueda
    
class ConsultaCovid19(models.Model):
    pais = models.CharField(max_length=100,verbose_name="Busqueda enfermedad")

    def __str__(self):
        return self.pais
    





