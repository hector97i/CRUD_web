from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('alumnos', views.alumnos, name = 'alumnos'),
    path('profesores', views.profesores, name = 'profesores'),
    path('materias', views.materias, name = 'materias'),
    path('carreras', views.carreras, name = 'carreras'),
    path('alumnos/nuevo', views.nuevoAlumno, name = 'nuevoAlumno'),
    path('profesores/nuevo', views.nuevoProf, name = 'nuevoProf'),
    path('materias/nuevo', views.nuevaMateria, name = 'nuevaMateria'),
    path('carreras/nuevo', views.nuevaCarrera, name = 'nuevaCarrera'),
    path('alumnos/historial<int:id>',views.historial, name = 'historial'),
    path('alumnos/editar/<int:id>', views.editarAlumno, name = 'editarAlumno'),
    path('profesores/editar/<int:id>', views.editarProf, name = 'editarProf'),
    path('carreras/editar/<int:id>', views.editarCarrera, name = 'editarCarrera'),
    path('materia/editar/<int:id>', views.editarMateria, name = 'editarMateria'),
    path('<int:id>/<str:typ_e>/eliminar', views.delete_item, name = 'delete_item'),
    path('profesores/<int:id>/materias', views.materiasProf, name  = 'materiasProf'),
    
]