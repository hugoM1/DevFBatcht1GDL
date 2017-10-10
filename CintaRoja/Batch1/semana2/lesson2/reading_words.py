def read_words():
    lista_palabras = []
    numero_de_palabras = input("Cuantas palabras?")
    print numero_de_palabras
    for x in range(numero_de_palabras):
        lista_palabras.append(raw_input("ingrese palabra por favor"))
    print lista_palabras

# read_words()



def f(x): return x % 3 == 0 or x % 5 == 0
print filter(f, range(2, 25))