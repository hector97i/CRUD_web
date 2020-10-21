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


def nuevaCarrera(request):

    if request.method == 'POST':
        form = CarreraForm(request.POST)
        if form.is_valid():
            if Carrera.objects.filter(name=form.cleaned_data.get("abv")).exists():
                form = CarreraForm()
                return render(request, 'schoolCRUD/nuevaCarrera.html', {'form': form, 'text': "Carrera ya existe."})
            else:
                form.save()
                return HttpResponseRedirect(reverse(carreras))
    else:
        form = CarreraForm()
    return render(request, 'schoolCRUD/nuevaCarrera.html', {'form':form, 'text': "", 'title': "Nueva carrera", 'button': "Crear", 'value': "new" })


def nuevaMateria(request):

    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            if Materia.objects.filter(name=form.cleaned_data.get("nombre")).exists():
                form = MateriaForm()
                return render(request, 'schoolCRUD/nuevaMateria.html', {'form': form, 'text': "Materia ya existe."})
            else:
                form.save()
                return HttpResponseRedirect(reverse(materias))
    else:
        form = MateriaForm()
    return render(request, 'schoolCRUD/nuevaMateria.html', {'form':form, 'text': "", 'title': "Nueva materia", 'button': "Crear", 'value': "new" })

def nuevoProf(request):

    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            if Profesor.objects.filter(name=form.cleaned_data.get("nombre")).exists():
                form = ProfesorForm()
                return render(request, 'schoolCRUD/nuevoProf.html', {'form': form, 'text': "Profesor ya existe."})
            else:
                form.save()
                return HttpResponseRedirect(reverse(profesores))
    else:
        form = ProfesorForm()
    return render(request, 'schoolCRUD/nuevoProf.html', {'form':form, 'text': "", 'title': "Nuevo profesor", 'button': "Crear", 'value': "new" })

def nuevoAlumno(request):

    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            if Alumno.objects.filter(name=form.cleaned_data.get("nombre")).exists():
                form = AlumnoForm()
                return render(request, 'schoolCRUD/nuevoAlumno.html', {'form': form, 'text': "Alumno ya existe."})
            else:
                form.save()
                return HttpResponseRedirect(reverse(alumnos))
    else:
        form = AlumnoForm()
    return render(request, 'schoolCRUD/nuevoAlumno.html', {'form':form, 'text': "", 'title': "Nuevo Alumno", 'button': "Crear", 'value': "new" })

def historial(request, id):
    alumno = Alumno.objects.get(pk=id)
    context = {
        "aprobadas": alumno.historial_aprobadas,
        "reprobadas": alumno.historial_reprobadas
    }
    return render(request, 'schoolCRUD/historial.html', context)


def editarAlumno(request, id):

    if request.method == 'POST':
        alumno = Alumno.objects.get(pk=id)
        form = AlumnoForm(request.POST,request.FILES, instance = alumno)
        #form.date = form.date.strftime("%d/%m/%Y")
        try:
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse(alumnos))
            else: 
                print(f"{form.errors}")

        except:
            print("Form is not valid") 

    elif request.method == 'GET':
        alumno = Alumno.objects.get(pk=id)
        form = AlumnoForm(instance = alumno)

    return render(request, "schoolCRUD/nuevoAlumno.html", {'form':form, 'text': "", 'title': "Editar alumno", 'button' : "Aceptar", 'alumno': alumno, 'value': "edit"})


def editarProf(request, id):

    if request.method == 'POST':
        prof = Profesor.objects.get(pk=id)
        form = ProfesorForm(request.POST,request.FILES, instance = prof)
        #form.date = form.date.strftime("%d/%m/%Y")
        try:
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse(profesores))
            else: 
                print(f"{form.errors}")

        except:
            print("Form is not valid") 

    elif request.method == 'GET':
        prof = Profesor.objects.get(pk=id)
        form = ProfesorForm(instance = prof)

    return render(request, "schoolCRUD/nuevoProf.html", {'form':form, 'text': "", 'title': "Editar profesor", 'button' : "Aceptar", 'prof': prof, 'value': "edit"})

def editarMateria(request, id):

    if request.method == 'POST':
        materia = Materia.objects.get(pk=id)
        form = MateriaForm(request.POST,request.FILES, instance = materia)
        #form.date = form.date.strftime("%d/%m/%Y")
        try:
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse(materias))
            else: 
                print(f"{form.errors}")

        except:
            print("Form is not valid") 

    elif request.method == 'GET':
        materia = Materia.objects.get(pk=id)
        form = MateriaForm(instance = materia)

    return render(request, "schoolCRUD/nuevaMateria.html", {'form':form, 'text': "", 'title': "Editar materia", 'button' : "Aceptar", 'materia': materia, 'value': "edit"})

def editarCarrera(request, id):

    if request.method == 'POST':
        carrera = Carrera.objects.get(pk=id)
        form = CarreraForm(request.POST,request.FILES, instance = carrera)
        #form.date = form.date.strftime("%d/%m/%Y")
        try:
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse(carreras))
            else: 
                print(f"{form.errors}")

        except:
            print("Form is not valid") 

    elif request.method == 'GET':
        carrera = Carrera.objects.get(pk=id)
        form = MateriaForm(instance = carrera)

    return render(request, "schoolCRUD/nuevaCarrera.html", {'form':form, 'text': "", 'title': "Editar carrera", 'button' : "Aceptar", 'carrera': carrera, 'value': "edit"})

def materiasProf(request, id):

    prof = Profesor.objects.get(pk=id)
    context = {
        "materias": prof.materias
    }

    return render(request, 'schoolCRUD/materiasProf.html', context)

def delete_item(request, id, typ_e):

    if typ_e == 'almno':
        item = ALumno.objects.get(pk=id)
        item.delete()
        return HttpResponseRedirect(reverse('alumnos'))
    elif typ_e == 'profesor':
        item = Profesor.objects.get(pk=id)
        item.delete()
        return HttpResponseRedirect(reverse('profesores'))
    elif typ_e == 'materia':
        item = Materia.objects.get(pk=id)
        item.delete()
        return HttpResponseRedirect(reverse('materias'))
    elif typ_e == 'carrera':
        item = Carrera.objects.get(pk=id)
        item.delete()
        return HttpResponseRedirect(reverse('carreras'))
    