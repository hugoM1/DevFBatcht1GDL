def creando_tuplas():
    # empty tuple
    my_tuple = ()
    print(my_tuple)

    # tuple having integers
    my_tuple = (1, 2, 3)
    print(my_tuple)

    # tuple with mixed datatypes
    my_tuple = (1, "Hello", 3.4)
    print(my_tuple)

    # nested tuple
    my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
    print(my_tuple)

    # tuple can be created without parentheses
    # also called tuple packing

    my_tuple = 3, 4.6, "dog"
    print(my_tuple)

    # tuple unpacking is also possible
    a, b, c = my_tuple
    print(a)
    print(b)
    print(c)

# creando_tuplas()

def indexing_tuplas():
    my_tuple = ('p', 'e', 'r', 'm', 'i', 't')

    # Output: 'p'
    print(my_tuple[0])

    # Output: 't'
    print(my_tuple[5])

    # index must be in range
    # IndexError: list index out of range

    # print(my_tuple[6])

    # index must be an integer
    # TypeError: list indices must be integers, not float

    # my_tuple[2.0]

    # nested tuple
    n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))

    # nested index
    # Output: 's'
    print(n_tuple[0][3])

    # nested index
    # Output: 4
    print(n_tuple[1][1])

# indexing_tuplas()

def cambiando_elementos():
    my_tuple = (4, 2, 3, [6, 5])

    # we cannot change an element
    # TypeError: 'tuple' object does not support item assignment

    my_tuple[1] = 9

    # # but item of mutable element can be changed
    # my_tuple[3][0] = 9
    # print(my_tuple)
    #
    # # tuples can be reassigned
    # my_tuple = ('p', 'r', 'o', 'g', 'r', 'a', 'm', 'i', 'z')
    # print(my_tuple)
cambiando_elementos()