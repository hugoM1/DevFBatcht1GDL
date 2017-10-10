# set de enteros
set_enteros = {1, 2, 3}
# print(set_enteros)

# set de diferentes tipos de datos
set_diferentes_tipos = {1.0, "Hello", (1, 2, 3)}
# print(set_diferentes_tipos)

# set no pueden tener elementos repetidos
set_numeros_repetidos = {1, 2, 3, 4, 3, 2}
# print(set_numeros_repetidos)

# set no pueden tener numeros mutables como listas o diccionarios como elementos
# mutable_set = {1, 2, [3, 4]}

# operaciones con sets

# initialize my_set

# print(my_set)

# you will get an error
# TypeError: 'set' object does not support indexing

# my_set[0]
my_set = {1, 3}


def add_element_to_set():
    # add an element
    # my_set.add(2)
    # print "element added", my_set

    # add multiple elements
    # my_set.update([2, 3, 4])
    # print "set updated with several elements at once", my_set
    #
    # # add list and set
    my_set.update([4, 5], {1, 6, 8})
    print "set updated using a list", my_set


# add_element_to_set()

def delete_set_element():
    # initialize my_set
    my_set = {1, 3, 4, 5, 6}
    print(my_set)

    # discard an element
    my_set.discard(4)
    print(my_set)

    # remove an element
    my_set.remove(16)
    print(my_set)

    # discard an element
    # not present in my_set
    my_set.discard(2)
    print(my_set)

    # remove an element
    # not present in my_set
    # you will get an error.
    # Output: KeyError: 2

    # my_set.remove(2)


# delete_set_element()


def pop_element_from_set():
    # initialize my_set
    # Output: set of unique elements
    my_set = set("HelloWorld")
    print(my_set)

    # pop an element
    # Output: random element
    print(my_set.pop())

    # clear my_set
    # Output: set()
    my_set.clear()
    print(my_set)


# pop_element_from_set()

# pop_element_from_set()
setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

inter = setA.intersection(setB)
print inter
