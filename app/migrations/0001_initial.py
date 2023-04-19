# Generated by Django 4.1.7 on 2023-04-17 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmarReserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medico', models.CharField(max_length=30, verbose_name='Nombre médico')),
                ('especialidad', models.IntegerField(choices=[[0, 'Medicina General'], [1, 'Odontología'], [2, 'Psicología'], [3, 'Pediatría'], [4, 'Dermatología'], [5, 'Ginecología y Obstetricia']], verbose_name='Especialidad médico')),
                ('dia_agendado', models.DateField()),
                ('hora_agendada', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_esp', models.CharField(max_length=30, verbose_name='Nombre de la especialidad')),
            ],
        ),
        migrations.CreateModel(
            name='Reclamos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='RegistroUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=50, verbose_name='Nombres del usuario')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos del usuario')),
                ('correo', models.EmailField(max_length=50, verbose_name='Correo de usuario')),
                ('nombre_usuario', models.CharField(max_length=25, verbose_name='Nombre de usuario')),
                ('contraseña', models.CharField(max_length=30, verbose_name='Contraseña de usuario')),
                ('repetir_contraseña', models.CharField(max_length=30, verbose_name='Campo repetir contraseña')),
                ('direccion', models.CharField(max_length=60, verbose_name='Dirección de usuario')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento de usuario')),
            ],
        ),
        migrations.CreateModel(
            name='ReservarHora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut_pac', models.CharField(max_length=12, verbose_name='Rut de paciente')),
                ('prevision', models.IntegerField(choices=[[0, 'Fondo Nacional de Salud(Fonasa)'], [1, 'Isalud Isapre De Codelco'], [2, 'Isapre Banmédica'], [3, 'Isapre Colmena'], [4, 'Isapre Consalud'], [5, 'Isapre Cruz Blanca'], [6, 'Isapre Cruz Del Norte'], [7, 'Isapre Fundación Banco Estado'], [8, 'Isapre Nueva Másvida'], [9, 'Isapre Vida Tres'], [10, 'Particular']])),
            ],
        ),
        migrations.CreateModel(
            name='Medicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=30, verbose_name='Nombre médico')),
                ('rut_med', models.CharField(max_length=12, unique=True, verbose_name='Rut médico')),
                ('id_esp', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.especialidad')),
            ],
        ),
    ]
