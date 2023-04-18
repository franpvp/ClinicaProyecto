from django.db import models

# Modelo Registro de Usuario (Campos de Formulario de registro)
class RegistroUsuario(models.Model):
    nombres = models.CharField(max_length=50, verbose_name="Nombres del usuario")
    apellidos = models.CharField(max_length=50, verbose_name="Apellidos del usuario")
    correo = models.EmailField(max_length=50, verbose_name="Correo de usuario")
    nombre_usuario = models.CharField(max_length=25, verbose_name="Nombre de usuario")
    contraseña = models.CharField(max_length=30, verbose_name="Contraseña de usuario")
    repetir_contraseña = models.CharField(max_length=30, verbose_name="Campo repetir contraseña")
    direccion = models.CharField(max_length=60, verbose_name="Dirección de usuario")
    fecha_nacimiento = models.DateField(verbose_name="Fecha de nacimiento de usuario")

    def __str__(self):
        return self.nombres

# Lista de opciones para variable "tipo_usuario"
opciones_usuario = [
    [0, "Paciente"],
    [1, "Familiar Paciente"],
    [2, "Otro"]
]
# Modelo Reclamos
class Reclamos(models.Model):
    nombre: models.CharField(max_length=50, verbose_name="Nombres de usuario")
    apellidos: models.CharField(max_length=50, verbose_name="Apellidos de usuario")
    rut_usuario: models.CharField(max_length=12, verbose_name="Rut de usuario")
    celular: models.IntegerField(max_length=8, verbose_name="Numero de celular usuario")
    direccion: models.CharField(max_length=60, verbose_name="Direccion de usuario")
    tipo_usuario: models.IntegerField(choices=opciones_usuario)
    comentarios: models.TextField()

    def __str__(self):
        return self.nombre
    
# Modelo Especialidad
class Especialidad(models.Model):
    nombre_esp = models.CharField(max_length=30,null=False,verbose_name="Nombre de la especialidad")

    def __str__(self):
        return self.nombre_esp
    
# Modelo Médicos
class Medicos(models.Model):
    nombre_completo = models.CharField(max_length=30, verbose_name="Nombre médico")
    rut_med = models.CharField(max_length=12,unique=True,verbose_name="Rut médico")
    id_esp = models.ForeignKey(Especialidad, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_completo

opciones_prev = [
    [0, "Fondo Nacional de Salud(Fonasa)"],
    [1, "Isalud Isapre De Codelco"],
    [2, "Isapre Banmédica"],
    [3, "Isapre Colmena"],
    [4, "Isapre Consalud"],
    [5, "Isapre Cruz Blanca"],
    [6, "Isapre Cruz Del Norte"],
    [7, "Isapre Fundación Banco Estado"],
    [8, "Isapre Nueva Másvida"],
    [9, "Isapre Vida Tres"],
    [10, "Particular"]
]

# Modelo Reservar Hora
class ReservarHora(models.Model):
    rut_pac = models.CharField(max_length=12,verbose_name="Rut de paciente")
    prevision = models.IntegerField(choices=opciones_prev)

    def __str__(self):
        return self.rut_pac

opcion_especilidad = [
    [0,"Medicina General"],
    [1,"Odontología"],
    [2,"Psicología"],
    [3,"Pediatría"],
    [4,"Dermatología"],
    [5,"Ginecología y Obstetricia"]
]

# Modelo Confirmar Reservar Hora
class ConfirmarReserva(models.Model):
    nombre_pac = models.CharField(max_length=40, verbose_name="Nombre Paciente")
    apellidos_pac = models.CharField(max_length=50, verbose_name="Apelldos Paciente")
    medico = models.CharField(max_length=30, verbose_name="Nombre médico")
    especialidad = models.IntegerField(choices=opcion_especilidad,verbose_name="Especialidad médico",null=False)
    dia_agendado = models.DateField(null=False)
    hora_agendada = models.TimeField(null=False)

    def __str__(self):
        return self.nombre_pac

    
    





