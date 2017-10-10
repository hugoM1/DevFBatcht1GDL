# -*- coding: utf-8 -*-



# print myList[2]
# print myList[2:5]
# print myList[5:]
# print myList[:5]
# print myList[:]

myList = [1, 2, 3, 4, 5, 6]
def recorrer_lista(lista):
    m = 0
    for i in range(len(lista)):
        if m < myList[i]:
            m = myList[i]
        print i, m


# recorrer_lista(myList)

def agregar_item_a_lista():
    lista = []
    for i in range(10):
        lista.append(i + 1)
    print lista


# agregar_item_a_lista()

def array_dos_dimenciones():
    print "array dos dimenciones"
    myArray = [[1, 2], [3, 4]]
    for i in range(len(myArray)):
        for j in range(len(myArray[i])):
            print myArray[i][j]

# array_dos_dimenciones()


numero = int(input("Numero de palabras para la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        print "proporcione palabra", str(i + 1) + ": "
        palabra = raw_input()
        lista.append(palabra)
    print "La lista creada es:", lista