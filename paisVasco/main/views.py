from django.shortcuts import render

from django.http.response import HttpResponseRedirect, HttpResponse
from django.conf import settings
from datetime import datetime

from main.models import Provincia, TipoEvento, Lenguas, Municipio, Evento
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


path = 'data'


#Funcion de acceso restringido que carga los datos en la BD
@login_required(login_url='/ingresar')
def populateDatabase(request):
    populateTipoEventos()
    populateLenguas()
    populateMunicipio()
    populateEventos()
    logout(request)  # se hace logout para obligar a login cada vez que se vaya a poblar la BD
    return HttpResponseRedirect('/index.html')




def populateEventos()
    print("Loading Tipo Eventos...")
    TipoEvento.objects.all().delete()


def populateTipoEventos():

    print("Loading Tipo Eventos...")
    TipoEvento.objects.all().delete()

    lista = []
    fileobj = open(path + "\\tipoevento.csv", "r")
    for line in fileobj.readlines():
        lista.append(TipoEvento(nombre=str(line.strip())))
    fileobj.close()
    TipoEvento.objects.bulk_create(lista)  # bulk_create hace la carga masiva para acelerar el proceso

    print("Tipo eventos inserted: " + str(TipoEvento.objects.count()))
    print("---------------------------------------------------------")


def populateLenguas():
    print("Loading lenguas...")
    Lenguas.objects.all().delete()

    lista = []
    fileobj = open(path + "\\lenguas.csv", "r")
    for line in fileobj.readlines():
        lista.append(Lenguas(nombre=str(line.strip())))
    fileobj.close()
    Lenguas.objects.bulk_create(lista)  # bulk_create hace la carga masiva para acelerar el proceso

    print("Lenguas inserted: " + str(Lenguas.objects.count()))
    print("---------------------------------------------------------")


def populateMunicipio():
    print("Loading Municipio...")
    Municipio.objects.all().delete()

    lista = []
    fileobj = open(path + "\\municipio.csv", "r")
    for line in fileobj.readlines():
        lista.append(Municipio(nombre=str(line.strip())))
    fileobj.close()
    Municipio.objects.bulk_create(lista)  # bulk_create hace la carga masiva para acelerar el proceso

    print("Municipio inserted: " + str(Municipio.objects.count()))
    print("---------------------------------------------------------")