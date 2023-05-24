import re
import json
import csv


def leer_archivo_json(nombre_archivo:str) -> list:

    """
    lee un archivo json desde la ruta,
    para luego cargarla en una variable 
    iterable

    nombre_archivo: es la ruta que se
    lee para ser cargada en una variable

    retorno:
    la funcion devolvera un lista de
    diccionarios que contiene lo mismo
    que la ruta pasada
    """

    lista_json = []
    
    with open(nombre_archivo,"r") as archivo: 

        diccionario = json.load(archivo)

        lista_json = diccionario["jugadores"]

    return lista_json
#1
def mostar_nombre_y_posicion_dream_team(lista_jugadore:list) -> None:

    """
    imprime los datos nombre, y posiciion 
    en la lista que se pasa por parametro

    lista_jugadore: es la lista de diccionarios
    que se va a mostrar

    retorno:
    no tiene
    """

    for juegar in lista_jugadore:

        print("{0} - {1}".format(juegar["nombre"],juegar["posicion"]))





















































































































