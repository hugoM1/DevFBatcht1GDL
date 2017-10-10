lista = [1, 2 ,3]
sett = {1, 2, 3}
tup = (1, 2 ,3)
dic = {1:'value1', 2: 'value2', 3: 'value3'}



def crear_diccionario():
    # empty dictionary
    my_dict = {}

    # dictionary with integer keys
    my_dict = {1: 'apple', 2: 'ball'}

    # dictionary with mixed keys
    my_dict = {'name': 'John', 1: [2, 4, 3]}

    # using dict()
    my_dict = dict({1: 'apple', 2: 'ball'})

    # from sequence having each item as a pair
    my_dict = dict([(1, 'apple'), (2, 'ball')])

def accesar_elementos():
    my_dict = {'name': 'Jack', 'age': '26', }

    # Output: Jack
    print(my_dict['name'])

    # Output: 26
    print(my_dict.get('age'))

    print my_dict['address']

# accesar_elementos()

def cambiar_agregar_elementos():
    my_dict = {'name': 'hugo', 'age': 26}

    # update value
    my_dict['age'] = 27

    print(my_dict)

    # add item
    my_dict['address'] = 'zapopan'

    print(my_dict)

# cambiar_agregar_elementos()

def eliminar_elementos():
    # create a dictionary
    squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

    # remove a particular item
    print(squares.pop(4))
    print(squares)

    # remove an arbitrary item
    print(squares.popitem())
    print(squares)

    # delete a particular item
    del squares[5]
    print(squares)

    # remove all items
    squares.clear()
    print(squares)

    # delete the dictionary itself
    del squares

    # Throws Error
    # print(squares)
# eliminar_elementos()

def ejercicio():
    squares = {x: x * x for x in range(6)}
    print(squares)
    print range(6)
    #equivalente
    # squares = {}
    # for x in range(6):
    #     squares[x] = x * x

ejercicio()