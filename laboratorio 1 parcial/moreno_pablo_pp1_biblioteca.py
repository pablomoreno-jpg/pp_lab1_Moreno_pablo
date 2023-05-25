import re
import json


def validar_numero_ingresado(numero:str) -> bool:

    """
    lee el numero que se le pasa por 
    parametros y verifica si es 
    numero entero

    retorno:
    en caso de que sea un numero
    (negativo o positivo) devuelve true,
    en caso de no ser un numero devuelve
    False 
    """

    invalido = False

    if re.match(r'^\-?\d+$',numero): #expresion regular para validar tanto numero positivos como negativos

        invalido = True

    return invalido

def ingresar_opciones(lista_opciones:list) -> int: 

    """
    pide por consola le ingrese de una opcion
    y valida si lo ingresado es un numero.

    lista_opciones: es una lista con numeros
    que sirve para compara si el numero ingresado
    esta en la lista 

    retorno:
    en caso de que lo ingresado es un numero, 
    y pertenece a la lista pasada por parametros
    devuelve el numero en formato int.
    en caso de no cumplir ningun caso vuelve a pedir
    un ingreso valido
    """

    while True:

        opcion = input("ingrese una opcion: ")

        if validar_numero_ingresado(opcion): #si la funcion devuelve entra en la validacion
            
            opcion_int = int(opcion)

            if opcion_int in lista_opciones: #si el numero se encuentra dentro de lista, hace el return

                return opcion_int #cuando entra a esta linea, el while deja de iterar
            
            else:

                print("la opcion no existe")

        else:   # en caso de entrar en algunos de los 2 elses, vuelve a pedir un numero

            print("opcion invalida")

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
    
    with open(nombre_archivo,"r") as archivo: #modo de lectura

        diccionario = json.load(archivo)

        lista_json = diccionario["jugadores"] # carga al varible solo con el diccionario 'jugadores'

    return lista_json

def guardar_csv(nombre_guardado:str,contenido:str) -> bool:

    """
    crea y guarda un archivo .scv

    nombre_guardado: es el nombre con el que
    se va a guarda

    contenido: es lo que se va a guardar en el 
    archivo (debe ser un formato de texto)

    retorno:
    devolvera True si se guarda con exito,
    False en caso de error
    """

    exito = False

    with open(nombre_guardado,"w") as archvo:

        conteo = archvo.write(contenido)

    if conteo == len(contenido):

        exito = True

    return exito

#1
def mostrar_nombre_y_posicion_dream_team(lista_jugadores:list) -> None:

    """
    imprime los datos nombre, y posiciion 
    en la lista que se pasa por parametro

    lista_jugadore: es la lista de diccionarios
    que se va a mostrar

    retorno:
    no tiene
    """

    for jugador in lista_jugadores:
    
            print("{0} - {1}".format(jugador["nombre"],jugador["posicion"]))

#2
def imprimir_dicionario(diccionario:dict) -> None:

    """
    imprime, por consola, todas las claves y
    valores de un diccionario (indepentientemente
    si su valor es una lista o un dicionario)


    diccionario: es el diccionario que se va a
    imprimir por consola

    retrono:
    no tiene
    """


    for campo in diccionario: 

        if type(diccionario[campo]) == dict: #en caso de que el valor de la la clave sea dict
            
            print("-{}:".format(campo),end="\n")
            imprimir_dicionario(diccionario[campo]) 

        elif type(diccionario[campo]) == list:
            
            print("-{}:".format(campo))
            for elemento in diccionario[campo]:

                print("-{}".format(elemento))

        else:    
            print("-{0}: {1}".format(campo,diccionario[campo]),end="\n")

def mostrar_nombre_y_o_inidece(lista_jugadores:list,mostrar_inidce = False) -> None:

    """
    muestra los nombres (y los indices 
    correspondientes si se desea) de todos
    los jugadores de la lista

    lista_jugadores: es la lista en donde se van 
    a encontrar los nombres de los jugadores

    mostrar_inidce: es la variable que valida
    si se quiere mostrar el indice o no.
    seteada en False por defecto
    """


    cantidad_jugadores = len(lista_jugadores)

    if mostrar_inidce: 

        for indice in range(cantidad_jugadores):

            print("{0:3}    - {1}".format(indice,lista_jugadores[indice]["nombre"]),end="\n")

    else:

        for diccionario in lista_jugadores:

            print("-{}".format(diccionario["nombre"]))

def mostrar_un_jugador_por_indice(lista_jugadores:list) -> dict:

    """
    muestra, por consola, los nombres (junto
    con sus respectivos indices) de los jugadores
    de la lista, para luego pedirle al usuario
    el indice del jugdor el cual quiere que se
    muestre sus estadisticas.

    lista_jugadores: es la lista en la cual se van
    a mostrar los nombres de los jugadores, y la lista
    del jugadore que el usuario quiera

    retorno:
    en caso de el numero ingresado, se valido. devolvera
    un nuevo diccionario con el nombre, posicion 
    y las estadisticas del jugador elegido. en caso 
    de errores, mostrar cual fue el error cometido y
    devolvera un diccionario vacio
    """

    nombre_y_estaditicas = {}
    
    cantidad_jugadores = len(lista_jugadores)

    print("indice - nombre:")

    mostrar_nombre_y_o_inidece(lista_jugadores,mostrar_inidce=True)

    indice = input("ingrese el numero del indice: ")
    print("\n",end="")

    if validar_numero_ingresado(indice):

        indice = int(indice)

        if indice <= cantidad_jugadores and indice > -1:

            for indec in range(cantidad_jugadores):

                if indice == indec:

                    nombre_y_estaditicas["nombre"] = lista_jugadores[indec]["nombre"]
                    nombre_y_estaditicas["posicion"] = lista_jugadores[indec]["posicion"]
                    nombre_y_estaditicas["estadisticas"] = lista_jugadores[indec]["estadisticas"]

                    print("{0}\nestadisticas: ".format(nombre_y_estaditicas["nombre"]),end="\n")
                    imprimir_dicionario(nombre_y_estaditicas["estadisticas"])

        else:

            print("el numero igresado, excede los indices de la lista")

    else:

        print("el valor ingresado, no es un numero valid.")
           

    return nombre_y_estaditicas

#3
def guardar_estadisticas_de_un_jugador(diccionario_estadisticas:dict,nombre_guardado:str) -> bool:

    """
    recibe un diccionario para luego
    guardarlo en formato csv

    diccionario_estadisticas: es el 
    diccionario que se va a guardar en 
    formanto de texto

    nombre_guardado: es el nombre, junto
    con la direccion con la cual se va a guardar
    el archivo

    retorno:
    en caso de que la liste no este vacia, o que 
    no halla ningun error a la hora de crear el
    archivo, devolvera True. en caso contrario
    devolvera False 
    
    """

    guardado_exitoso = False

    if len(diccionario_estadisticas) > 0:

        guardar = "{}:{}\n{}:{}\n".format("nombre",diccionario_estadisticas["nombre"],"posicion",diccionario_estadisticas["posicion"])
        
        #primeras 2 lineas para posteriomente guardar el resto en una secuencia for  

        for campo in diccionario_estadisticas["estadisticas"]:

            guardar += "{}:{}\n".format(campo,diccionario_estadisticas["estadisticas"][campo])

        if guardar_csv(nombre_guardado,guardar): #si la funcion devuelve verdadero significa que guardo bien

            guardado_exitoso = True

    return guardado_exitoso

#4
def validar_nombre_ingresado(lista_jugadores:list,nombre:str) -> int : 

    """
    valida si el nombre perteneze, o se 
    asemeja a un nombre que este en la lista

    lista_jugadores: es la lista en donde se 
    van a buscar y comparar los nombres 

    nombre: es el nombre que se va a buscar
    si tiene similitud a algun nombre de la 
    lista

    retorno:
    en caso de encotrar alguna similitud, devuelve
    el indice de la lista, en donde se encontro 
    la similitud. en caso contrario devuelve 
    -1
    """

    contador = 0

    for elemento in lista_jugadores:

        if re.search(nombre,elemento["nombre"].lower()):
            
            return contador

        contador +=1 

    return -1
    
def buscar_y_mostrar_logros(lista_jugadores:list) -> None:

    mostrar_nombre_y_o_inidece(lista_jugadores)

    nombre = input("ingrse el nombre del jugador el cual quiera ver sus logros: ")

    indec = validar_nombre_ingresado(lista_jugadores,nombre)

    if indec > -1 :# si no encotro la simitud no entra
        
        print("logroes de {}:".format(lista_jugadores[indec]["nombre"]))

        for logro in lista_jugadores[indec]["logros"]:

            print(logro) 

    else:

        print("no se encontro el jugador que se ingreso")

#5

def calcular_promedio_de_lista(lista_jugadores:list,dato:str) -> float:

    prmedio = 0

    if len(lista_jugadores) > 0:

        suma = 0

        contador = 0

        for indec in range(len(lista_jugadores)):

            suma += lista_jugadores[indec]["estadisticas"][dato]

            contador += 1


        prmedio = suma/ contador

    return prmedio

def ordenar_nombres(lista_jugadores:list) -> list:

    copia_lista = lista_jugadores[:]

    if len(copia_lista) > 0:

        ordenamiento = True

        while ordenamiento:

            ordenamiento = False

            for indec in range(len(copia_lista) -1):

                if copia_lista[indec]["nombre"] > copia_lista[indec+1]["nombre"]:
                    
                    ordenamiento = True

                    copia_lista[indec],copia_lista[indec+1] = copia_lista[indec+1],copia_lista[indec]

             

    return copia_lista

def mostrar_promedio_del_equipo(lista_jugadores:list) -> None:

    if len(lista_jugadores) > 0:

        promedio = calcular_promedio_de_lista(lista_jugadores,"promedio_puntos_por_partido")
        
        print("el promedio de puntos por partido (promedio pp) de todo el equipo es: {}".format(promedio))
        
        lista_ordenada = ordenar_nombres(lista_jugadores)

        for elemento in lista_ordenada:
            
            print("-{0} |promedio.pp :{1}".format(elemento["nombre"],elemento["estadisticas"]["promedio_puntos_por_partido"]))

#6
def buscar_miembre_del_salon_de_la_fama(lista_jugadores:list):

    pertencia = False

    mostrar_nombre_y_o_inidece(lista_jugadores)

    nombre = input("ingrese el nombre del jugdor que quierea buscar en el salon de la fama del baloncesto: ")

    indec =  validar_nombre_ingresado(lista_jugadores,nombre)

    if indec > -1:

        for logro in lista_jugadores[indec]["logros"]:

            if re.search(r'(Miembro del Salon de la Fama del Baloncesto)$',logro):

                pertencia = True

        if pertencia:

            print("el jugador pertence al salon de la fama del balocesto")

        else:

            print("el jugador no petence al salon de la fama")


























































































