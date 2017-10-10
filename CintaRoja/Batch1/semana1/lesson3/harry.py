# print "\t\t".join(map(lambda x: "".join(raw_input("Dame uno elemento\t\t")) ,range(input("Dame tamano de la lista \t"))))


def palabras(lista2=[]):
    for x in range(input('cuantas palabras?')):lista2.append(raw_input("Escribe la palabra"))
    print lista2

palabras()