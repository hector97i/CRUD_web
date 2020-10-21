from django.db import models
from django.forms import ModelForm
from django.db.models import Q
from django.db.models import DateField
from django import forms
# Create your models here.
#y los profesores que la imparten.

class Area(models.Model):
    AREAS = [
        ('ING', 'Ingenieria'),
        ('SCI', 'Ciencias'),
        ('HUM', 'Humanidades'),
        ('SOC', 'Ciencias Sociales')
    ]
    area = models.CharField(choices=AREAS,default='ING', max_length=32)

    def __str__(self):
        return f"{self.area}"


class Grado(models.Model):
    GRADOS = [
        ('BACH', 'Bachillerato'),
        ('LIC', 'Licenciatura'),
        ('MAS', 'Maestría'),
        ('DOC', 'Doctorado'),
        ('POSD', 'Post-doctorado')
    ]
    grado = models.CharField(choices=GRADOS,default='MAS', max_length=32)

    def __str__(self):
        return f"{self.grado}"

class Estado(models.Model):
    CHOICES = [
        ('ACT', 'Activo'),
        ('SUS', 'Suspendido'),
        ('BAJA', 'Dado de baja')
    ]
    estado = models.CharField(choices=CHOICES,default='ACT', max_length=32)

    def __str__(self):
        return f"{self.estado}"

class Campus(models.Model):
    nombre = models.CharField(max_length=64)
    ciudad = models.CharField(max_length=64)
    abv = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.abv} - {self.nombre}"

class Profesor(models.Model):
    nomina = models.CharField(max_length=9)
    nss = models.CharField(max_length=16)
    nombre = models.CharField(max_length=64)
    rfc = models.CharField(max_length=16)
    curp = models.CharField(max_length=64)
    direccion = models.CharField(max_length=128)
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateField()
    lugar_nacimiento = models.CharField(max_length=64)
    email_personal = models.CharField(max_length=64)
    email_institucional = models.CharField(max_length=64)
    ultimo_grado = models.ForeignKey(Grado, on_delete=models.CASCADE, null=False)
    major = models.CharField(max_length=32)
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING)
    materias = models.ManyToManyField('Materia')
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    tipo = "profesor"

    def __str__(self):
        return f"{self.nombre} - {self.nomina} - {self.area}"
    

class Materia(models.Model):
    nombre = models.CharField(max_length=64)
    clave = models.CharField(max_length=8)
    creditos = models.IntegerField()
    horas_semanales = models.IntegerField()
    ofertada_antes = models.BooleanField()
    area = models.ForeignKey(Area, on_delete=models.DO_NOTHING)
    alumnos_previo = models.IntegerField()
    abierta = models.BooleanField()
    no_estudiantes = models.IntegerField()
    grupos = models.IntegerField()
    profesores = models.ManyToManyField(Profesor)
    tipo = "materia"

    def __str__(self):
        return f"{self.clave} - {self.nombre}" 
    

class Carrera(models.Model):
    nombre = models.CharField(max_length=64)
    abv = models.CharField(max_length=4)
    semestres = models.IntegerField()
    campus = models.ManyToManyField(Campus)
    alumnos_inscritos = models.IntegerField()
    fecha_plan = models.DateField()
    materias = models.ManyToManyField(Materia)
    creditos_min = models.IntegerField()
    creditos_max = models.IntegerField()
    profesores = models.ManyToManyField(Profesor)
    tipo = "carrera"

    def __str__(self):
        return f"{self.abv} - {self.nombre}" 

class Alumno(models.Model):
    matricula = models.CharField(max_length=9)
    nombre = models.CharField(max_length=128)
    direccion = models.CharField(max_length=128)
    telefono = models.IntegerField()
    fecha_nacimiento = models.DateField()
    email = models.CharField(max_length=64)
    curp = models.CharField(max_length=64)
    lugar_nacimiento = models.CharField(max_length=64)
    tutor = models.CharField(max_length=64)
    carrera = models.ForeignKey(Carrera, on_delete = models.CASCADE, null = False)
    semestre = models.IntegerField()
    historial_aprobadas = models.ManyToManyField(Materia, related_name='aprobadas')
    historial_reprobadas = models.ManyToManyField(Materia, related_name='repsrobadas')
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    tipo = "alumno"

    def __str__(self):
        return f"{self.matricula} - {self.nombre}"         

class CampusForm(ModelForm):

    class Meta:
        model = Campus
        fields = '__all__'

class ProfesorForm(ModelForm):

    class Meta:
        model = Profesor
        fields = '__all__'

class MateriaForm(ModelForm):

    class Meta:
        model = Materia
        fields = '__all__'

class CarreraForm(ModelForm):

    class Meta:
        model = Carrera
        fields = '__all__'

class AlumnoForm(ModelForm):

    class Meta:
        model = Alumno
        fields = '__all__'
