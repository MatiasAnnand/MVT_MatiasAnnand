from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from Family.models import Familiar

# Create your views here.
def familiar(self):

    padre = Familiar(nombre = "Andres", edad = 60, cumpleanios = "1962-10-01")
    padre.save()

    madre = Familiar(nombre = "Lucia", edad = 59, cumpleanios = "1961-05-05")
    madre.save()

    hermano = Familiar(nombre = "Juan", edad = 20, cumpleanios = "2002-09-02")
    hermano.save()

    diccionario = {
        "FamNom1":padre.nombre,
        "FamEdad1":padre.edad,
        "FamCumple1":padre.cumpleanios,
        "FamNom2":madre.nombre,
        "FamEdad2":madre.edad,
        "FamCumple2":madre.cumpleanios,
        "FamNom3":hermano.nombre,
        "FamEdad3":hermano.edad,
        "FamCumple3":hermano.cumpleanios,
        }

    Plantilla = loader.get_template('family.html')
    documento = Plantilla.render(diccionario)

    return HttpResponse(documento)