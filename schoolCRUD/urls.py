from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('alumnos', views.alumnos, name = 'alumnos'),
    path('profesores', views.profesores, name = 'profesores'),
    path('materias', views.materias, name = 'materias'),
    path('carreras', views.carreras, name = 'carreras'),
    path('alumnos/historial<int:id>',views.historial, name = 'historial'),
    path('alumnos/editar/<int:id>', views.editarAlumno, name = 'editarAlumno'),
    path('<int:id>/<str:typ_e>/eliminar', views.delete_item, name = 'delete_item'),
    path('alumnos/nuevo', views.nuevoAlumno, name = 'nuevoAlumno'),
    
]