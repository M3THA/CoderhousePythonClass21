from django import http
from django.shortcuts import render

from AppCoder.forms import CursoFormulario, ProfeFormulario
from .models import Curso, Profesor
from django.http import HttpResponse

# Create your views here.


def curso(self):
    
    curso= Curso(nombre="Django", comision=939393)
    curso.save()
    texto= f"Curso creado: {curso.nombre} {curso.comision}"
    return HttpResponse(texto)

def inicio(request):
    return render (request, "Appcoder/inicio.html")

def cursos(request):
    return render (request, "Appcoder/cursos.html")

def profesores(request):
    return render (request, "Appcoder/profesores.html")

def estudiantes(request):
    return render (request, "Appcoder/estudiantes.html")

def entregables(request):
    return render (request, "Appcoder/entregables.html")

def cursoFormulario(request):
    if request.method == 'POST':
        miFormulario= CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            curso= Curso (nombre=informacion['curso'], comision=informacion['comision'])
            curso.save()
            return render(request, "AppCoder/inicio.html")
    else:
            miFormulario= CursoFormulario()
    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario":miFormulario})

def profeFormulario(request):
    if request.method == 'POST':
        miFormulario= ProfeFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            informacion= miFormulario.cleaned_data
            profe= Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])
            profe.save()
            return render(request, "AppCoder/inicio.html")
    else:
            miFormulario= ProfeFormulario()
    return render(request, "AppCoder/profeformulario.html", {"miFormulario":miFormulario})

def busquedaComision(request):

    return render(request, "AppCoder/busquedaComision.html")

def buscar(request):
    if request.GET['comision']:
        comision= request.GET['comision']
        cursos= Curso.objects.filter(comision__icontains=comision)
        
        return render (request, "AppCoder/resultadosBusqueda.html", {"cursos":cursos, "Camada": comision})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)