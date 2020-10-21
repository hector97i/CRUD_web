from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from schoolCRUD.models import *
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, "schoolCRUD/index.html")

def alumnos(request):

    context = {
        "alumnos": Alumno.objects.all()
    }

    return render(request, 'schoolCRUD/alumnos.html', context)

def profesores(request):
    
    context = {
        "profesores": Profesor.objects.all()
    }
    
    return render(request, 'schoolCRUD/profesores.html', context)
    
def materias(request):

    context = {
        "materias": Materia.objects.all()
    }

    return render(request, 'schoolCRUD/materias.html', context)

def carreras(request):

    context = {
        "carreras": Carrera.objects.all()
    }

    return render(request, 'schoolCRUD/carreras.html', context)


def nuevoAlumno(request):

    return render(request, 'schoolCRUD/nuevoAlumno.html')

def historial(request, id):
    alumno = Alumno.objects.get(pk=id)
    context = {
        "aprobadas": alumno.historial_aprobadas,
        "reprobadas": alumno.historial_reprobadas
    }
    return render(request, 'schoolCRUD/historial.html', context)

def editarAlumno(request, id):
