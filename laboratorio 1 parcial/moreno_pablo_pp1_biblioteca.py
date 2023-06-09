import re
import json


def validar_numero_ingresado(numero:str) -> bool:

    """
    lee el numero que se le pasa por 
    parametros y verifica si es 
    numero entero 

    numero: es el texto que se va a
    validar si es un entero

    retorno:
    en caso de que sea un entero devuelve true,
    en caso contrario False 
    """

    validad = False

    if re.match(r'^\-?\d+$',numero):
         #valida si es un numero entro  (negativo o postivo)

        validad = True

    return validad

def validar_flotante_ingresado(numero:str) -> bool:

    """
    lee el numero que se le pasa por 
    parametros y verifica si es 
    un numero floatante aceptable

    numero: es el texto que se va a
    validar si es un flotante

    retorno:
    en caso de que sea un flotante devuelve true,
    en caso contrario False 
    """

    validad = False

    if re.match(r'^\-?\d+$|^\-?\d+\.\d+$',numero):
    #valida si es un numero flotante aceptable(negativo o postivo)

        validad = True

    return validad
   

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

        if validar_numero_ingresado(opcion):
             #si la funcion devuelve entra en la validacion
            
            opcion_int = int(opcion)

            if opcion_int in lista_opciones: 
                #si el numero se encuentra dentro de lista, hace el return

                return opcion_int 
                #cuando entra a esta linea, el while deja de iterar
            
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

    lista_leida = []
    
    with open(nombre_archivo,"r") as archivo: 
        #modo de lectura

        diccionario = json.load(archivo)

        lista_leida = diccionario["jugadores"] 
        # carga al varible solo con el diccionario 'jugadores'

    return lista_leida

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
def mostrar_nombre_y_posicion_dream_team(lista_jugadores:list,dato:str) -> None:

    """
    imprime los datos nombre, y el
    dato que se quiera ver junto

    lista_jugadore: es la lista de diccionarios
    que se va a mostrar

    dato: es el dato cuyo valor se va a mostrar
    junto al nombre

    retorno:
    no tiene
    """

    for jugador in lista_jugadores:
        
        print("{0} - {1}: {2}".format(jugador["nombre"],dato,jugador[dato]))

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


    for key in diccionario: 

        if type(diccionario[key]) == dict: 
            #en caso de que el valor de la key sea diccionario
            
            print("-{}:".format(key),end="\n")
            imprimir_dicionario(diccionario[key]) 

        elif type(diccionario[key]) == list: 
            #en caso de que el valor de la key sea una lista
            
            print("-{}:".format(key))
            for elemento in diccionario[key]:

                print("-{}".format(elemento))

        else:    
            print("-{0}: {1}".format(key,diccionario[key]),end="\n")

def mostrar_nombre_y_o_inidece(lista_valores:list,mostrar_inidce = False) -> None:

    """
    muestra los nombres (y los indices 
    correspondientes si se desea) de todos
    los jugadores de la lista

    lista_valores: es la lista en donde se van 
    a encontrar los nombres de los jugadores

    mostrar_inidce: es la variable que valida
    si se quiere mostrar el indice o no.
    seteada en False por defecto

    retorno: 
    no tiene
    """


    cantidad_jugadores = len(lista_valores)

    if mostrar_inidce: 
        #caso True, muestra el indice en el que el valor esta parado junto al nombre

        for indice in range(cantidad_jugadores):

            print("{0:3}    - {1}".format(indice,lista_valores[indice]["nombre"]),end="\n")

    else:

        for diccionario in lista_valores: 
            #caso False, solo muestra los nombres

            print("-{}".format(diccionario["nombre"]))

def buscar_jugador_por_indice(lista_buscar_jugador:list) -> dict: 

    """
    muestra por consola los nombres (junto
    con sus respectivos indices) de los jugadores
    de la lista, para luego pedirle al usuario
    el indice del jugdor el cual quiere que se
    muestre sus estadisticas.

    lista_buscar_jugador:es la lista en donde
    se va a relizar la busqueda. a partir de
    un indice de la misma

    retorno:
    en caso de el numero ingresado, sea valido. devolvera
    un nuevo diccionario con el nombre, posicion 
    y las estadisticas del jugador elegido. en caso 
    de errores, mostrar cual fue el error cometido y
    devolvera un diccionario vacio
    """

    nombre_y_estaditicas = {}
    
    indices_de_jugadores = len(lista_buscar_jugador)

    print("indice - nombre:")

    mostrar_nombre_y_o_inidece(lista_buscar_jugador,mostrar_inidce=True) 
    #mustra nombres junto a sus indices

    indice = input("ingrese el indice del jugador cuyas estadisticas quiera ver: ")

    if validar_numero_ingresado(indice):

        indice = int(indice)

        if indice < indices_de_jugadores and indice > -1: 
            #validacion para que no se ingrese 12 o mas, o menos de 0

            nombre_y_estaditicas["nombre"] = lista_buscar_jugador[indice]["nombre"]
            nombre_y_estaditicas["posicion"] = lista_buscar_jugador[indice]["posicion"]
            nombre_y_estaditicas["estadisticas"] = lista_buscar_jugador[indice]["estadisticas"]
            
            print("{0}\nestadisticas: ".format(nombre_y_estaditicas["nombre"]))
            imprimir_dicionario(nombre_y_estaditicas["estadisticas"])
            print("\n",end="")
        else:

            print("el numero igresado, excede los indices de la lista")

    else:

        print("el valor ingresado, no es un numero valid.")
           

    return nombre_y_estaditicas

#3
def guardar_un_jugador(diccionario_jugador:dict,nombre_guardado:str) -> bool:

    """
    recibe un diccionario para luego
    guardarlo en formato csv

    diccionario_jugador: es el 
    diccionario que se va a guardar en 
    formanto de texto

    nombre_guardado: es el nombre, junto
    con la direccion en la cual se va a guardar
    el archivo

    retorno:
    en caso de que la liste no este vacia, o que 
    no halla ningun error a la hora de crear el
    archivo, devolvera True. en caso contrario
    devolvera False 
    
    """

    guardado_exitoso = False

    if len(diccionario_jugador) > 0:

        guardar = "{}:{}\n{}:{}\n".format("nombre",diccionario_jugador["nombre"],"posicion",diccionario_jugador["posicion"])
        
        #primeras 2 lineas para posteriomente guardar el resto en una secuencia for  

        for campo in diccionario_jugador["estadisticas"]:

            guardar += "{}:{}\n".format(campo,diccionario_jugador["estadisticas"][campo])

        if guardar_csv(nombre_guardado,guardar): 
            #si la funcion devuelve verdadero significa que guardo bien

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

    """
    pide por consola que ingrese el nombre
    del jugador, el cual quiera ver sus
    logros

    lista_jugadores: es la lista de donde
    se van a sacar los valores de jugador 
    que se ingrese

    retorno:
    no tiene
    """


    mostrar_nombre_y_o_inidece(lista_jugadores)
    # muestra los nombres de los jugadores para su ingreso

    nombre = input("ingrse el nombre del jugador el cual quiera ver sus logros: ")

    indec = validar_nombre_ingresado(lista_jugadores,nombre) 
    #valida si lo que se ingrese se parece a algun nombre de la lista

    if indec > -1 :# si no encuetra la similitud no entra
        
        print("logroes de {}:".format(lista_jugadores[indec]["nombre"]))

        for logro in lista_jugadores[indec]["logros"]:

            print(logro) 

    else:

        print("no se encontro el jugador que se ingreso")


#5
def calcular_promedio_de_lista(lista_jugadores:list,dato:str) -> float:

    """
    calcula el promedio de cualquier dato 
    que se le pease por paramtro, de la 
    lista

    lista_jugadores: es la lista de donde 
    se van a sacar los valores a buscar

    dato: es el valor que se va a buscar 
    dentro de la lista

    retorno:
    devolvera el calculo del 
    promedio de dato que se le paso 
    por parametros
    """


    prmedio = 0

    if len(lista_jugadores) > 0: #valida que la lista no este vacia

        suma = 0

        contador = 0

        for indec in range(len(lista_jugadores)):

            suma += lista_jugadores[indec]["estadisticas"][dato]

            contador += 1


        prmedio = suma/ contador

    return prmedio

def ordenar_lista(lista_ordenar:list,nombre_posicion:str) -> list:

    """
    ordena una lista por los
    nombres (o posiciones ),
    en orden alfabetico

    lista_ordenar: es la lista que
    se va a odenar.

    nombre_posicion: es el tipo
    de dato que se va a utilizar
    como filtro para ordenar
    (la lista solo ordena por 
    los datos nombre o posicion)

    retorno:
    devuelve la misma lista
    pero en ordene alfabetico
    """

    copia_lista = lista_ordenar[:]

    if re.match(r'^nombre$|^posicion$',nombre_posicion):
    
        #expresion para que solo acepte los datos nombre y posicion

        ordenamiento = True

        while ordenamiento:

            ordenamiento = False

            for indec in range(len(copia_lista) -1):

                if copia_lista[indec][nombre_posicion] > copia_lista[indec+1][nombre_posicion]:
                    
                    ordenamiento = True

                    copia_lista[indec],copia_lista[indec+1] = copia_lista[indec+1],copia_lista[indec]

    else:

        print("error, no se pude ordenar por este dato")


    return copia_lista

def mostrar_promedio_del_equipo(lista_jugadores:list) -> None:

    """
    calcula el promedio de 
    puntos por partido de 
    todos los jugadores
    para luego mostrar cada
    uno de los putos por partido
    de todos los jugadoes
    (ordenado por nombre)

    lista_jugadores: es la lista 
    de donde se van a obtener los datos 
    para calcular el promedio y para
    mostrar los nombres de los jugadores

    retorno:
    no tiene
    """

    if len(lista_jugadores) > 0:

        promedio = calcular_promedio_de_lista(lista_jugadores,"promedio_puntos_por_partido")
        
        print("el promedio de puntos por partido (promedio pp) de todo el equipo es: {}".format(promedio))
        
        lista_ordenada = ordenar_lista(lista_jugadores,"nombre")

        for elemento in lista_ordenada:
            
            print("-{0} |promedio.pp :{1}".format(elemento["nombre"],
                                                  elemento["estadisticas"]
                                                  ["promedio_puntos_por_partido"]))
    
#6
def buscar_miembro_del_salon_de_la_fama(lista_jugadores:list) -> None:

    """ 
    pide el ingres del nombre de 
    un jugador para luego buscar
    si pertence al salon de la fama
    del baloncesto

    lista_jugadores: es la lista de donde
    se van a buscar los jugadores
    
    retorno:
    no tiene
    """

    pertencia = False

    mostrar_nombre_y_o_inidece(lista_jugadores)

    nombre = input("nombre del jugador que quiera saber si es parte del salon de la fama: ")

    indec =  validar_nombre_ingresado(lista_jugadores,nombre)

    if indec > -1:

        for logro in lista_jugadores[indec]["logros"]:

            nombre = lista_jugadores[indec]["nombre"]

            if re.search(r'(Miembro del Salon de la Fama del Baloncesto)$',logro):

                pertencia = True

        if pertencia:

            print("el jugador {} pertence al salon de la fama del balocesto".format(nombre))

        else:

            print("el jugador {} no petence al salon de la fama".format(nombre))

    else:

        print("no se encontro el jugador que esta buscando")

#7-8-9-13-14-19
def buscar_el_mayor_dato_de_la_lista(lista_jugadores:list,dato_buscar:str) -> None:
    
    """
    busca y muestra cual es el
    mayor valor estadistico que 
    se puede encontrar en la lista
    
    lista_jugadores: es de donde se 
    van a optener los datos para la 
    busqueda

    dato_buscar: es el valor estadistico
    que se va a buscar dentro de la lista

    retorno:
    no tiene
    """

    jugador_encontrado = {}

    if len(lista_jugadores) > 0:

        flag_primera_vez = True

        for indec in range(len(lista_jugadores)):

            if flag_primera_vez:

                jugador_encontrado = lista_jugadores[indec]

                flag_primera_vez = False

            else:

                if lista_jugadores[indec]["estadisticas"][dato_buscar] > jugador_encontrado["estadisticas"][dato_buscar]:

                        jugador_encontrado = lista_jugadores[indec]

        dato_buscar = dato_buscar.replace("_"," ") # modificacion para una lectura mas limpia
        print("el jugador con mas {0} es: {1}".format(dato_buscar,jugador_encontrado["nombre"]))

#10-11-12-15-18
def mostrar_datos_estaditico_de_un_jugador(jugador:dict,dato:str) -> None:

    """
    mustra el nombre y el dato que 
    se desee (que este en dentro de
    las estaditicas) del jugador

    jugador: es el diccioanrion donde
    se van a buscar los datos de un jugador

    dato: es el dato que se va a buscar
    dentro del diccionario 'estadisticas'
    que tiene el jugador

    retorno:
    no tiene 
    """
    if len(jugador) > 0: #valida que no se le pase un diccionario vacio

        dato_impreso = dato.replace("_"," ") #para que la impresion por consola sea mas limpia

        print("{} - {}: {}".format(jugador["nombre"],dato_impreso,jugador["estadisticas"][dato]))

def jugador_con_mayor_promedio(lista_jugadores:list,dato_comparar:str) -> None:

    """
    pide el ingrese de un numero y busca
    los jugadores que tenga el dato
    que supere ese numero

    lista_jugadores: es la lista de
    donde se van a obtener el dato


    dato_comparar: es el dato que se
    va a buscar y comparar con el
    numero ingresado

    retorno:
    no tiene
    """

    dato_impreso = dato_comparar.replace("_"," ")

    mensaje_input = "ingrese un valor para buscar jugador con mayor {}:".format(dato_impreso)

    ingreso = input(mensaje_input)

    encontrado = False 
    #bool que valida si se muestra un mensaje en caso de que no se ecuentre un jugador que supere
    #el valor ingresado.

    if validar_flotante_ingresado(ingreso):

        busqueda = float(ingreso) 

        for jugador in lista_jugadores:

            if jugador["estadisticas"][dato_comparar] > busqueda:

                encontrado = True #si se encuentra, el mensaje no se mostrara.

                mostrar_datos_estaditico_de_un_jugador(jugador,dato_comparar)


        if not encontrado: #en no se encuentre valor que supere lo ingresado muenstra el mensaje.

            print("lo siento, no se encontro jugador que supere ese numero")
            

    else:

        print("error, lo que se ingreso no es un numero valido")

#16
def buscar_minimo(lista_jugadores:list,dato:str,promedio_a_comparar:float) -> int:

    """
    busca de entre toda la lista,
    cual es el menor valor del 
    dato a buscar

    lista_jugadores: es la lista
    en donde se va a buscar y
    compara los valores

    dato: es el dato que se va 
    a buscar en la lista

    promedio_a_comparar: es un 
    valor por el cual se va a
    comparar para hayar el
    menor valor en la lista  

    retono:
    retorno el indice en donde
    se encontro el menor 
    valor del dato
    """

    flag_primera_vez = True #se cambia cuando es la primer iteracion

    for indec in range(len(lista_jugadores)):
    
        if flag_primera_vez:

            flag_primera_vez = False

            indec_minimo = indec

        else:

            if lista_jugadores [indec]["estadisticas"][dato] < promedio_a_comparar:

                indec_minimo = indec
        

    return indec_minimo

def calcular_promedio_y_excluir_al_mas_bajo(lista_jugadores:list) -> None:

    if len(lista_jugadores) > 0:
        
        promedio_puntos_partido =  calcular_promedio_de_lista(lista_jugadores,"promedio_puntos_por_partido")

        posicion_minima = buscar_minimo(lista_jugadores,"promedio_puntos_por_partido",promedio_puntos_partido)

        for indec in range(len(lista_jugadores)):

            if indec != posicion_minima:

                mostrar_datos_estaditico_de_un_jugador(lista_jugadores[indec],"promedio_puntos_por_partido")

#17
def buscar_jugador_con_mas_logros(lista_jugadores:list) -> None:
    
    """
    busca y muestra cual es el jugador
    que tiene la mayor cantidad de 
    logros 

    lista_jugadores: es la lista
    de donde se obtienen los datos
    para calcular los logros

    retorno:
    no tiene
    """

    if len(lista_jugadores) > 0:

        cantidad_logros = 0 #valor inicial para la busqueda de maximo

        for jugador in lista_jugadores:

            if len(jugador["logros"]) > cantidad_logros:

                    cantidad_logros = len(jugador["logros"])#la mayor cantidad de logros lo mido con un len

                    jugadore_con_mas_logros = jugador 

        print("el jugador con mas logros es: {}",jugadore_con_mas_logros["nombre"])

#20
def jugadores_con_mayor_porcentaje_de_tiro(lista_jugadores:list) -> None:

    if len(lista_jugadores) > 0:

        lista_auxiliar = [] 

        flag_encuentro = False #variable que cambia si encuentra, al menos, un valor mayor al numero ingresado

        porcentaje_ingresado = input("ingrese un numero: ")

        if validar_numero_ingresado(porcentaje_ingresado):

            porcenaje = float(porcentaje_ingresado)
            
            for jugador in lista_jugadores:

                if jugador["estadisticas"]["porcentaje_tiros_de_campo"] > porcenaje:

                    flag_encuentro = True

                    lista_auxiliar.append(jugador)  

            if flag_encuentro:

                lista_ordenada = ordenar_lista(lista_auxiliar,"posicion")
                
                for jugador in lista_ordenada:

                    #mostrar_datos_estaditico_de_un_jugador(jugador,"porcentaje_tiros_de_campo")
                    print("{0}| posicion: {1}|porcenjtae de tiros de campo: {2}".format(jugador["nombre"],
                                                                                        jugador["posicion"],
                                                                                        jugador["estadisticas"]
                                                                                                ["porcentaje_tiros_de_campo"]))
                    
            else:

                print("no se encontro un jugador que supere el numero ingresado")

        else:

            print("error, el dato no es un numero valido")

#23
def ordenar_lista_por_dato(lista_ordenar:list,dato:str) -> list:

    """
    ordenar de mayor a menor 
    a partir del valor (de la biblioteca
    estadistica)de un dato

    lista_ordenar: es la lista 
    que se va a ordenar

    dato: es el dato que se va
    a usar como comparacion principal
    para ordenar la lista

    retorno:
    devuelve la lisa ordena desde
    el mayor valor de un dato 
    """

    ordenar = True

    lista_ordenada = lista_ordenar[:]

    while ordenar:

        ordenar = False

        flag_primera_vez = True

        for indec in range(len(lista_ordenada)-1):

            if lista_ordenada[indec]["estadisticas"][dato] < lista_ordenada[indec+1]["estadisticas"][dato]:
                
                ordenar = True

                lista_ordenada[indec], lista_ordenada[indec+1] = lista_ordenada[indec+1],lista_ordenada[indec]


    return lista_ordenada

def rankear_listas(lista_rankear:list,dato:str) -> list[dict]:

    """
    ordena la lista y le da una
    posicion numerica (1 para el
    mayor, 12 para el menor) de 
    dependiendo de que tal 
    alto este en la lista

    lista_rankear: es la 
    lista que se va a ordenar
    para luego generar una posicion

    dato: es el dato que se va
    a usar como filtro
    para ordenar yu rankear 
    la lista

    retono:
    devolvera una lista de 
    diccionarios, que contentra
    el nombre del jugador y 
    la posicion en la que se encuentra
    en dicho dato
    """


    lista_diccionarios = []

    lista_ordenada = ordenar_lista_por_dato(lista_rankear,dato)

    contador = 0

    for elemento in lista_ordenada:

        contador += 1

        jugador = {}

        jugador["nombre"] = elemento["nombre"]

        jugador[dato] = contador

        lista_diccionarios.append(jugador)

    return lista_diccionarios

def juntar_listas_por_nombres(lista_1:list[dict],lista_2:list[dict],
                              calve_unica_1:str,clave_unica_2:str) -> list:

    """
    junta dos listas de diccionarios,
    cuyos elementos en comun 
    es que cada diccioanrio de cada
    lista, tiene el mismo nombre

    lista_1: es la primera lista
    que se va a iterar para la busqueda de un
    nombre en comun

    calve_unica_1: es la clave de la primera
    lista que la diferencia de la segunda

    lista_2: es la segunda lista en donde
    se va a buscar el nombre en comun

    clave_unica_2: es la clave de la segunda
    lista que la diferencia de la primera

    retorno:
    devolvera una lista de diccioanrios
    que tendra el nombre de un jugador
    y los valores de las claves unicas
    que se le paso por parametros
    """

    lista_3 = []

    for elemento_1 in lista_1:

        nombre = elemento_1["nombre"] #guarda el nombre para la busqueda

        for elemento_2 in lista_2:
            
            if elemento_2["nombre"] == nombre:

                nuevo_diccionario = {} #por cada iteracion, el diccioanrio se reescribe
                nuevo_diccionario["nombre"] = nombre
                nuevo_diccionario[calve_unica_1] = elemento_1[calve_unica_1]
                nuevo_diccionario[clave_unica_2] = elemento_2[clave_unica_2]

                lista_3.append(nuevo_diccionario) #el diccioanrio generado, se guarda en la lista



    return lista_3

def crear_nuevo_diccioanrio(diccioanrio_1:dict,claves_1:list,
                            diccioanrio_2:dict,claves_2:list,nombre:str) -> dict:

    """
    crea un nuevo diccioarnio
    a patir de 2 diccioanrio
    que comparten nombre

    diccioanrio_1: es un diccioanrio
    al cual se le van a tomar sus 
    valores, excetuando nombre
    
    claves_1: es una lista 
    de claves para acceder
    a los valores del diccionario_1

    diccioanrio_2: es un diccioanrio
    al cual se le van a tomar sus 
    valores, excetuando nombre

    claves_2:es una lista 
    de claves para acceder
    a los valores del diccionario_2

    nombre: es el nombre que va al
    principio de ambas listas

    retorno:
    devolvera un diccionario que tiene
    un nombre, y todos los valores de los
    diccioanrios que se le pasaron como para
    metros
    """


    diccioanrio_nuevo = {}

    diccioanrio_nuevo["nombre"] = nombre

    for key_1 in claves_1:

        diccioanrio_nuevo[key_1] = diccioanrio_1[key_1]

    for key_2 in claves_2:

        diccioanrio_nuevo[key_2] = diccioanrio_2[key_2]

    return diccioanrio_nuevo

def juntar_todos_los_rankings(rankin_1:list[dict],clave_1:str,rankin_2:list[dict],
                              clave_2:str,rankin_3:list[dict],clave_3:str,rankin_4:list[dict],
                              clave_4:str) -> list:

    """
    junta 4 listas de diccionarois
    que tiene como caracteristcas 
    que tienen nombres iguales en cada
    lista, y un dato unico

    rankin_1, rankin_2, rankin_3, rankin_4: 
    son listas de diccioanrios que solo comparten
    nombres.

    clave_1: es la clave unica de la lista
    rankin_1

    clave_2: es la clave unica de la lista
    rankin_2

    clave_3: es la clave unica de la lista
    rankin_3

    clave_4: es la clave unica de la lista
    rankin_4

    retorno:
    devuelve una lista de diccioanrios
    que en cada diccioarnio, tiene 
    un nombre y todos los valores de elemento
    de las listas pasadas
    
    """


    lista_junatada_1 = juntar_listas_por_nombres(rankin_1,rankin_2,clave_1,clave_2) 
    #se crea la primera parte del ranking

    claves_ranking_1 = []
    claves_ranking_1.append(clave_1)
    claves_ranking_1.append(clave_2)
    #se crea una lista que contiene las claves de la primera lista de rankig creada

    lista_junatada_2 = juntar_listas_por_nombres(rankin_3,rankin_4,clave_3,clave_4) 
    #se crea la segunda parte del ranking

    claves_ranking_2 = []
    claves_ranking_2.append(clave_3)
    claves_ranking_2.append(clave_4)
     #se crea una lista que contiene las claves de la segunda lista de rankig creada

    lista_completa = []

    for elemento_1 in lista_junatada_1:

        nombre = elemento_1["nombre"]

        for elemento_2 in lista_junatada_2:

            if elemento_2["nombre"] == nombre:

                diccioanario = {}

                diccioanario = crear_nuevo_diccioanrio(elemento_1,claves_ranking_1,
                                                       elemento_2,claves_ranking_2,nombre)

                lista_completa.append(diccioanario)

    return lista_completa

def crear_posicines_de_jugadores(lista_jugadores:list) -> list[dict]:

    """
    crea una lista de posiciones
    en las que se encuentran 
    cada uno de los jugadores
    con las siguentes estadisticas tomas:
    Puntos, Rebotes, Asistencias y robos

    lista_jugadores:
    es la lista de donde se van a 
    sacar los datos para crear el ranking

    retorno:
    devolvera una lista con los nombres 
    del jugadores, y sus respectivas posiciones
    en cada una de las estadisticas mencionadas
    """

    copia_lista = lista_jugadores[:]

    ranking_puntos = rankear_listas(copia_lista,"puntos_totales")

    ranking_rebotes = rankear_listas(copia_lista,"rebotes_totales")

    ranking_asistencias = rankear_listas(copia_lista,"asistencias_totales")

    ranking_robos = rankear_listas(copia_lista,"robos_totales")

    lista_rankeada = juntar_todos_los_rankings(ranking_puntos,"puntos_totales",ranking_rebotes,
                                               "rebotes_totales",ranking_asistencias,"asistencias_totales",
                                               ranking_robos,"robos_totales")

    return lista_rankeada

def capitalizar_palabras(palabra_texto:str) -> str:

    """
    capitaliza la palabra, o texto, que se le pase por 
    paramatro.

    palabra_texto: sting que se va a capilizar

    retorno:
    devuelve la palabra que se va a capitalizar

    """

    palabra_texto = palabra_texto.strip()

    if re.match(r'\b\w*,\w*\b',palabra_texto):

        lista_palabra = palabra_texto.split(",")

        palabras_capitalizadas = []

        for palabra in lista_palabra:

            palabras_capitalizadas.append(palabra.capitalize())

        nueva_palabra = ",".join(palabras_capitalizadas)

    else:

        nueva_palabra = palabra_texto.capitalize()

    return nueva_palabra

def guardar_posiciones(lista_posiciones:list[dict]) -> None:

    """
    guarda una lista 
    con todos los ranking de los
    jugadores en formato .csv

    lista_posiciones: es la
    lista que contiene los
    nombres y los rankings
    de todos los jugadores

    retorno:
    no tiene
    """


    contenido = ""

    claves = list(lista_posiciones[0].keys())

    cabezara = ",".join(claves)
    cabezara = cabezara.replace("nombre","Jugador")
    cabezara = cabezara.replace("_totales","")
    cabezara = capitalizar_palabras(cabezara)

    for elemento in lista_posiciones:
        
        contador = 0

        for key in claves:

            contador +=1

            if contador < len(claves):

                contenido += "{},".format(elemento[key])

            else:

                contenido += "{}\n".format(elemento[key])

        guardar = "{0}\n{1}".format(cabezara,contenido)

        if guardar_csv(r'laboratorio 1 parcial\ranking_dt.csv',guardar):

            print("el archivo, se guardo de forma exitosa")

        else:

            print("no se pudo guardar")


#extras:
#1
def buscar_cantidad_de_posiciones_de_jugadores(lista_jugadores:list) -> dict:

    """
    busca la cantidades de 
    jugadores que hay en cada
    jugador de la lista

    lista_jugadores: es la 
    lista en donde se van
    a buscar las posiciones

    retorno:
    devuelve un diccionario
    que tinene la posicion como
    clave y la cantidad de jugadores
    que se encontro en la posicion

    """

    dict_posiciones = {}

    if len(lista_jugadores):

        for elemento in lista_jugadores:

            if elemento["posicion"] in dict_posiciones:

                dict_posiciones[elemento["posicion"]] += 1

            else:

                dict_posiciones[elemento["posicion"]] = 1

    return dict_posiciones

def imprimir_diccioanrio(diccionario:dict) -> None:

    """
    imprime el diccioanrio
    que se le pasa por parametros

    diccionario: es el diccionario
    cuyas claves y valores 
    por consola

    retorno:
    no tiene
    """


    for key in diccionario:

        print("{0}: {1}".format(key,diccionario[key]))

#2

def obtener_numero_de_All_star(jugador:dict) -> int:

    """
    buscar la cantidad
    de veces fue que el jugador fue
    All-star 

    jugador: es el que se va a
    buscar la cantidad, de veces
    que fue All-star

    retorno:
    retornada un el numero de veces
    que el jugador fue All-star
    """


    if len(jugador) > 0:

        for indec in range(len(jugador["logros"])):
            #empieza iterando los indices de la lista logros

            if re.search("All-Star",jugador["logros"][indec]):
                #buscar en el elemento si dice all-star

                numero = re.findall(r'^\d++',jugador["logros"][indec])
                #busca y almacena el numero

                numero = int(numero[0])
                #lo castea

                return numero

        return 0
        #si no encuentra all-star devuelve 0

def ordenar_por_catidad_All_star(lista_jugadores:list) -> list:
    
    """
    ordena la lista en base
    a cuantes veces
    fue all-star, cada jugador
    
    lista_jugadores: es la lista
    que se va a ordenar

    retorno:
    devolvera la misma lista,
    pero ordenad desde el jugador
    que fue mas veces Allstar
    hasta el que menos
    """


    copia_lista = lista_jugadores[:]

    if len(lista_jugadores) > 0:

        ordenar = True

        while ordenar:

            ordenar = False

            for indec in range(len(copia_lista)-1):
                
                All_star_indec_actual = obtener_numero_de_All_star(copia_lista[indec])
                #busca el numero de veces All-star en el indice alctual

                All_star_indec_siguente = obtener_numero_de_All_star(copia_lista[indec+1])
                #busca el numero de veces All-star en el siguiente indice

                if All_star_indec_actual < All_star_indec_siguente:
                    
                    ordenar = True

                    copia_lista[indec],copia_lista[indec+1] = copia_lista[indec+1],copia_lista[indec]


    return copia_lista

def mostrar_lista_ordenada_por_Mayor_all_star(lista_jugadores:list) -> None:

    """
    muestra cuantas veces el jugador fue
    All-star, y los muesta de mayor a menor

    lista_jugadores: es la lista donde
    se va a buscar, cuantas veces el jugador
    fue All-star

    retorno:
    no tiene    
    """


    if len(lista_jugadores) > 0:

        lista_ordenada = ordenar_por_catidad_All_star(lista_jugadores)

        for elemento in  lista_ordenada:

            numero_all_star = obtener_numero_de_All_star(elemento) 

            print("{0} ({1} veces All-star)".format(elemento["nombre"],numero_all_star))


#3

def buscar_jugador_con_la_mejor_stadistica(lista_jugadores:list,valor_stadistico:str) -> str:
    
    """
    busca el mayor valor de la estaditicas
    de cada jugador en la lista 
    
    lista_jugadores: es la lista
    donde se buscan y comparan 
    los datos de los jugadores

    valor_stadistico: es el valor 
    que se va a compara y buscar
    en la lista

    retorno:
    devuelve un texto con el nombre del
    jugador que tiene el mayor valor 
    espesificado en la lista 
    """


    flag_primer_vez = True

    for jugador in lista_jugadores:

        if flag_primer_vez:

            flag_primer_vez= False

            mayor_estaditica = jugador

        elif jugador["estadisticas"][valor_stadistico] > mayor_estaditica["estadisticas"][valor_stadistico]:

            mayor_estaditica = jugador

        estaditica = valor_stadistico.replace("_"," ")

        jugador_con_mejor_estadistica = "mayor canitdad de {0}: {1}({2})".format(estaditica,mayor_estaditica["nombre"],
                                                                                 mayor_estaditica["estadisticas"][valor_stadistico])

    return jugador_con_mejor_estadistica

def los_mejores_jugadores_de_cada_estadistica(lista_jugadores:list) -> list:

    """
    muestra por consola 
    el nombre con el mayor
    valor esataditico de
    cada una de las estaditicas

    lista_jugadores: es la lista    
    donde se van a buscar y mostrar
    las mayores estaditicas

    retorno:
    devuelve una lista la mayor 
    estadistica y el nombre
    del jugador que tiene el
    valor mas grande en esa
    estaditica 
    """

    lista_estaditica = []
    
    lista_de_cada_staditica = []

    for key in lista_jugadores[0]["estadisticas"]:

        lista_estaditica.append(key)

    #obtengo todas las claves de la bibliotcea estadisticas en una lista

    for estadistica in lista_estaditica:

       lista_de_cada_staditica.append(buscar_jugador_con_la_mejor_stadistica(lista_jugadores,estadistica))

    return lista_de_cada_staditica

def mostrar_el_mejor_de_cada_estaditica(lista_mejores)-> None:

    """
    muestra por consola,
    una el mejor jugador de cada, estadictica

    lista_mejores: es la lista que
    se va a mostrar

    retono:
    no tiene
    """

    for elemento in lista_mejores:

        print("-{}".format(elemento))

#4

def cantidad_de_veces_que_se_repite_un_nombre(lista_estadisticas:list) -> dict:

    """
    buscar en una lista con textos
    cuantas veces se repite un nombre

    lista_estadisticas: es una lista
    el la que se va a buscar si se
    encuentra un nombre y cuantas veces
    se repite

    retorno:
    devolvera un diccioanrio en donde
    tiene como clave el nombre encotrado
    y como valor la cantidad de veces que
    se repitio
    """

    dict_cantidad_repeticiones = {}

    if len(lista_estadisticas)> 0:
        
        for elemento in lista_estadisticas: 

            nombre = re.findall(r'[A-Z]{1}[a-z]+',elemento)
            
            nombre = " ".join(nombre)

            if nombre in dict_cantidad_repeticiones:

                dict_cantidad_repeticiones[nombre] += 1

            else:

                dict_cantidad_repeticiones[nombre] = 1

    return dict_cantidad_repeticiones

def mostrar_el_jugador_con_las_mejores_estadicticas(lista_jugadores:list) -> None:

    """
    busca y muestra, cual es
    el jugador con las mejores
    estadisticas

    lista_jugadores: es la lista
    en donde se va a realizar la busqueda

    retono: 
    no tine
    """

    mayores_estaditicas = los_mejores_jugadores_de_cada_estadistica(lista_jugadores)
    #realiza denuevo lo solicitado en el punto antierior a este

    jugadores_encontrados = cantidad_de_veces_que_se_repite_un_nombre(mayores_estaditicas)
    #busca en la lista mayores_estaditicas, cuantas veces se repite un nombre

    flag_primera_vez = True

    for key in jugadores_encontrados:

        if flag_primera_vez:
            
            flag_primera_vez = False
            mayor_cantida = jugadores_encontrados[key]
            nombre_del_mejor = key


        elif jugadores_encontrados[key] > mayor_cantida:
            
            mayor_cantida = jugadores_encontrados[key]
            nombre_del_mejor = key


    print("el jugadores con las mejores estadisticas es {}".format(nombre_del_mejor))



#menu
def imprimir_opcines() -> None:

    """
    imprime las opciones que
    tiene el menu del 

    retorno:
    no tiene
    """

    print("\n"
          "1) Mostrar la lista de todos los jugadores del Dream Team.\n"
          "2) Ingresar el indice del jugador que quiera ver sus estadisticas.\n"
          "3) Guardar jugador elegido en la opcione 2.\n"
          "4) Buscar los logros de un jugador.\n"
          "5) Calcular y mostrar el promedio de puntos por partido de todo el equipo del Dream Team.\n"
          "6) Buscar jugador en el Salón de la Fama del Baloncesto.\n"
          "7) Calcular y mostrar el jugador con la mayor cantidad de rebotes totales.\n"
          "8) Calcular y mostrar el jugador con el mayor porcentaje de tiros de campo.\n"
          "9) Calcular y mostrar el jugador con la mayor cantidad de asistencias totales.\n"
          "10) Ingresar un valor y mostrar los jugadores que han promediado más puntos por partido que ese valor.\n"
          "11) Ingresar un valor y mostrar los jugadores que han promediado más rebotes por partido que ese valor.\n"
          "12) Ingresar un valor y mostrar los jugadores que han promediado más asistencias por partido que ese valor.\n"
          "13) Calcular y mostrar el jugador con la mayor cantidad de robos totales.\n"
          "14) Calcular y mostrar el jugador con la mayor cantidad de bloqueos totales.\n"
          "15) Ingresar un valor y mostrar los jugadores que tengan un porcentaje de tiros libres mayor.\n"
          "16) Calcular y mostrar el promedio de puntos por partido del equipo excluyendo al jugador con" 
               "la menor cantidad de puntos por partido.\n"
          "17) Calcular y mostrar el jugador con la mayor cantidad de logros obtenidos.\n"
          "18) Ingresar un valor y mostrar los jugadores que tengan un porcentaje de tiros triples mayor.\n"
          "19) Calcular y mostrar el jugador con la mayor cantidad de temporadas jugadas.\n"
          "20) Ingresar un valor y mostrar los jugadores , ordenados por posición en la cancha, que hayan tenido"
               "un porcentaje de tiros de campo superior a ese valor.\n"
          "21) Generar un archivo .csv con los rankings de los jugadores en puntos,rebotes,asistencias,y robos.\n"
          "\nextras:\n"
          "22.Determinar la cantidad de jugadores que hay por cada posición\n"
          "23.Mostrar la lista de jugadores ordenadas por la cantidad de All-Star de forma descendente\n"
          "24.Determinar qué jugador tiene las mejores estadísticas en cada valor\n"
          "25.Determinar qué jugador tiene las mejores estadísticas de todos.\n\n"

          "26) salir.\n",end= "\n")

def dream_team_app() -> None:

    """
    ejecuta un menu de opcines
    en el que se puede ejecutar diferentes
    funciones dependidiendo
    de la opcion que se elija 
    
    retorno:
    no tiene
    """

    flag_guardar = False

    ruta_lectura = r"C:\Users\pablo\OneDrive\Escritorio\python - ejercicios\laboratorio 1 parcial\dt.json"

    lista_nba = leer_archivo_json(ruta_lectura)

    numero_opcines = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]

    while True:
        


        imprimir_opcines()

        opcion = ingresar_opciones(numero_opcines)

        match opcion:

            case 1:
                mostrar_nombre_y_posicion_dream_team(lista_nba,"posicion")

            case 2:
                jugador_encontrado = buscar_jugador_por_indice(lista_nba)
                
                if len(jugador_encontrado) > 0:

                    flag_guardar = True

            case 3:
                if flag_guardar:

                    ruta_guardado = r"laboratorio 1 parcial\jugador_encontrado.csv"

                    if guardar_un_jugador(jugador_encontrado,ruta_guardado):

                        print("el jugador se guardo correctamente")

                    else:

                        print("error, al guardar un jugador")

                else:

                    print("por favor, ingrese a la opcion 2 primero")

            case 4:
                buscar_y_mostrar_logros(lista_nba)

            case 5:
                mostrar_promedio_del_equipo(lista_nba)

            case 6:
                buscar_miembro_del_salon_de_la_fama(lista_nba)

            case 7:
                buscar_el_mayor_dato_de_la_lista(lista_nba,"rebotes_totales")

            case 8:
                buscar_el_mayor_dato_de_la_lista(lista_nba,"porcentaje_tiros_de_campo")
                
            case 9:
                buscar_el_mayor_dato_de_la_lista(lista_nba,"asistencias_totales")
                
            case 10:
                jugador_con_mayor_promedio(lista_nba,"promedio_puntos_por_partido")

            case 11:
                jugador_con_mayor_promedio(lista_nba,"promedio_rebotes_por_partido")

            case 12:
                jugador_con_mayor_promedio(lista_nba,"promedio_asistencias_por_partido")

            case 13:
                buscar_el_mayor_dato_de_la_lista(lista_nba,"robos_totales")

            case 14:
                buscar_el_mayor_dato_de_la_lista(lista_nba,"bloqueos_totales")
            
            case 15:
                jugador_con_mayor_promedio(lista_nba,"porcentaje_tiros_libres")

            case 16:
                calcular_promedio_y_excluir_al_mas_bajo(lista_nba)

            case 17:
                buscar_jugador_con_mas_logros(lista_nba)

            case 18:
                jugador_con_mayor_promedio(lista_nba,"porcentaje_tiros_triples")

            case 19:
                buscar_el_mayor_dato_de_la_lista(lista_nba,"temporadas")

            case 20:
                jugadores_con_mayor_porcentaje_de_tiro(lista_nba)

            case 21:
                lista_posiciones = crear_posicines_de_jugadores(lista_nba)

                guardar_posiciones(lista_posiciones)

            case 22:
                lista_All_star = ordenar_por_catidad_All_star(lista_nba)

                mostrar_lista_ordenada_por_Mayor_all_star(lista_All_star)

            case 23:
                posiciones = buscar_cantidad_de_posiciones_de_jugadores(lista_nba)

                if len(posiciones):

                    imprimir_diccioanrio(posiciones)
            
            case 24:
                lista_estadisticas = buscar_jugador_con_la_mejor_stadistica(lista_nba)

                if len(lista_estadisticas) > 0:

                    mostrar_el_mejor_de_cada_estaditica(lista_estadisticas)

            case 25:
                mostrar_el_jugador_con_las_mejores_estadicticas(lista_nba)

            case 26:
                print("cerrando aplicacion....")
                break

lista_nba = leer_archivo_json(r"C:\Users\pablo\OneDrive\Escritorio\python - ejercicios\laboratorio 1 parcial\dt.json")


mostrar_el_jugador_con_las_mejores_estadicticas(lista_nba)