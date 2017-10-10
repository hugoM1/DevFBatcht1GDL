#Encoding
# -*- coding: utf-8 -*-
# NOTA
# El encoding no es más que una directiva que se coloca al inicio de un archivo Python,
# a fin de indicar al sistema, la codificación de caracteres utilizada en el archivo.

# Funciones
def saludar(nombre, mensaje='Hola'):
    print mensaje, nombre

# saludar("hugo")
# saludar("hugo", "sup")
# saludar(mensaje="Buen día", nombre="hugol")



#Funciones Recurcivas
def play(intento=1):
    respuesta = raw_input("¿De qué color es una naranja? ")
    if respuesta != "naranja":
        if intento < 3:
            print "\nFallaste! Inténtalo de nuevo"
            intento += 1
            play(intento) # Llamada recursiva
        else:
            print "\nPerdiste!"
    else:
        print "\nGanaste!"

# play()

#Asignación múltiple
def printing():
    a, b, c = 'string', 15, True
    mi_tupla = ('hola mundo', 2014)
    texto, anio = mi_tupla
    print str(a)
    print str(b)
    print str(c)
    print str(texto)
    print str(anio)


# printing()

# while
def the_while():
    while True:
        nombre = raw_input("Indique su nombre: ")
        if nombre:
            print nombre
            break

# the_while()

# sentencia for
def the_for():
    mi_lista = ['Juan', 'Antonio', 'Pedro', 'Herminio']
    for nombre in mi_lista:
        print nombre
    mi_tupla = ('rosa', 'verde', 'celeste', 'amarillo')
    for color in mi_tupla:
        print color
    for anio in range(2001, 2013):
        print "Informes del Año", str(anio)

# the_for()

# ################### Ejercicio 1 #################################
def iniciar():
    dulce = raw_input("Elija letra: ")
    if dulce=="a":
        precioProducto=2.5
        print "Su vuelto: ", calcularVuelto(monto,precioProducto)
    elif dulce=="b":
        precioProducto=1.4
        print "Su vuelto: ", calcularVuelto(monto,precioProducto)
    elif dulce=="c":
        precioProducto=4
        print "Su vuelto: ", calcularVuelto(monto,precioProducto)
    elif dulce=="d":
        precioProducto=1.2
        print "Su vuelto: ", calcularVuelto(monto,precioProducto)


def imprimirProductos():
    print "a) chupete : 2.5 \nb) gomas : 1.4 \nc) caramelo: 4 \nd) topline : 1.2"


def calcularVuelto(monto , precioProducto):
    return monto - precioProducto
#
# print imprimirProductos()
#
monto = input("Ingrese monto: ")
# if monto < 5:
#     print iniciar()
# else:
#     print "Monto debe ser menor a 5"
#     exit(0)
# ################### fin Ejercicio 1 #################################

# ################### Ejercicio 2 #################################
def tablas_de_multiplicar():
    for multiplicador in range(1, 11):
        print("Tabla de multiplicar del", multiplicador)
        for multiplicando in range(1, 11):
            print(multiplicando, "*", multiplicador, "=", multiplicando * multiplicador)
        print("==========================")

tablas_de_multiplicar()

# ################### fin Ejercicio 2 #################################

