from django.shortcuts import render

from django.http.response import HttpResponseRedirect, HttpResponse
from django.conf import settings
from datetime import datetime

from main.models import Provincia, TipoEvento, Lengua, Municipio, Evento
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


path = 'data'



def populateDatabase(request):
    e = populateTipoEventos()
    l = populateLenguas()
    m = populateMunicipio()
    populateEventos(e,l,m)
    logout(request)  # se hace logout para obligar a login cada vez que se vaya a poblar la BD
    return HttpResponseRedirect('/index.html')


def populateEventos(evento_map, lenguas_map, municipio_map):
    print("Loading Tipo Eventos...")
    TipoEvento.objects.all().delete()

    dict_lenguas = {}
    list_evento = []
    fileobj=open(path+"\\dataset_A.csv", "r")
    for line in fileobj.readlines():
        rip = line.strip().split(';')
        date = None if len(rip[2]) == 0 else datetime.strptime(rip[2], '%d-%m-%Y')

        list_aux= []
        lenguas = rip[3].strip("/")
        for lengua in lenguas:
            list_aux.append(lenguas_map[lengua])

        dict_lenguas[rip[0]] = list_aux
        list_evento.append(Evento(nombre=rip[0], tipoEvento=evento_map[rip[1]], fecha=date, lenguajes=list_aux, nombreLugar=rip[4],
                                  municipio=municipio_map[rip[5]], pais=rip[6]))
    fileobj.close()
    Evento.objects.bulk_create(list_evento)

    dict = {}
    for evento in Evento.objects.all():
        evento.lenguajes.set(dict_lenguas[evento.nombre])
        dict[evento.nombre] = evento

    print("Eventos inserted: " + str(Evento.objects.count()))
    print("---------------------------------------------------------")


def populateTipoEventos():
    print("Loading Tipo Eventos...")
    TipoEvento.objects.all().delete()

    lista = []
    dict = {}
    fileobj = open(path + "\\tipoevento.csv", "r")
    i = 1
    for line in fileobj.readlines():
        ev = TipoEvento(id=i, nombre=str(line.strip()));
        lista.append(ev)
        dict[line] = i
        i = i+1
    fileobj.close()
    TipoEvento.objects.bulk_create(lista)  # bulk_create hace la carga masiva para acelerar el proceso

    print("Tipo eventos inserted: " + str(TipoEvento.objects.count()))
    print("---------------------------------------------------------")
    return dict


def populateLenguas():
    print("Loading lenguas...")
    Lengua.objects.all().delete()

    lista = []
    dict = {}
    fileobj = open(path + "\\lenguas.csv", "r")
    i = 1
    for line in fileobj.readlines():
        leng = Lengua(id=i, nombre=str(line.strip()))
        lista.append(leng)
        dict[line] = i
        i = i+1
    fileobj.close()
    Lengua.objects.bulk_create(lista)  # bulk_create hace la carga masiva para acelerar el proceso

    print("Lenguas inserted: " + str(Lengua.objects.count()))
    print("---------------------------------------------------------")
    return dict


def populateMunicipio():
    print("Loading Municipio...")
    Municipio.objects.all().delete()

    lista = []
    dict = {}
    fileobj = open(path + "\\municipio.csv", "r")
    i = 1
    for line in fileobj.readlines():
        mun = Municipio(id=i, nombre=str(line.strip()))
        lista.append(mun)
        dict[line] = i
        i = i+1
    fileobj.close()
    Municipio.objects.bulk_create(lista)  # bulk_create hace la carga masiva para acelerar el proceso

    print("Municipio inserted: " + str(Municipio.objects.count()))
    print("---------------------------------------------------------")
    return dict