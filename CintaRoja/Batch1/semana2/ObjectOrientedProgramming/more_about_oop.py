# coding=utf-8
# class Vehicle:
#     def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
#         self.number_of_wheels = number_of_wheels
#         self.type_of_tank = type_of_tank
#         self.seating_capacity = seating_capacity
#         self.maximum_velocity = maximum_velocity
#
#     @property
#     def number_ofwheels(self):
#         return self.number_of_wheels
#
#     @number_ofwheels.setter
#     def number_of_wheels(self, number):
#         self.number_of_wheels = number
#
#     def make_noise(self):
#         print('VRUUUUUUUM')
#
#
# tesla_model_s = Vehicle(4, 'electric', 5, 250)
# print(tesla_model_s.number_of_wheels) # 4
# tesla_model_s.number_of_wheels = 2 # setting number of wheels to 2
# print(tesla_model_s.number_of_wheels) # 2
#
# tesla_model_s.make_noise()

"""Encapsulation: Ocultando Información"""

# Encapsulation is a mechanism that restricts direct access to objects’ data and methods.
# But at the same time, it facilitates operation on that data (objects’ methods).
# All internal representation of an object is hidden from the outside.
# Only the object can interact with its internal data.

""" El encapsulamiento se consigue a menudo mediante la ocultación de 
información, que es el proceso de ocultar todos secretos de un objeto que no 
contribuyen a sus caracteristicas esenciales; típicamente, la estructura de un 
objeto esta oculta, así como la implementación de sus metodos.”[Análisis y 
diseño orientado a objetos con aplicaciones *]

En otras palabras es impedir el acceso a los métodos o variables del objeto, 
para que solo se puedan usar dentro de la instancia del objeto. Esto en los 
lenguajes como Java o C# lo logran con unos modificadores de 
acceso (anteponen a la definición del método o propiedad public, private, protected, etc.).

Los modificadores de acceso permiten al diseñador de clases delimitar la frontera entre lo
que es accesible para los usuarios de la clase, lo que es estrictamente privado y ‘no importa’ 
a nadie más que al diseñador de la clase e incluso lo que podría llegar a importar a otros 
diseñadores de clases que quisieran alterar, completar o especializar el comportamiento de la clase.
"""

""" ‘Private’ instance variables that cannot be accessed except from inside an object don’t exist in 
Python. However, there is a convention that is followed by most Python code: a name prefixed 
with an underscore (e.g. __spam) should be treated as a non-public 
part of the API (whether it is a function, a method or a data member)"""


class Persona(object):

    def __init__(self, nombre, email, age):
        self.nombre = nombre
        self.__email = email
        self.__age = age

    def get_name(self):
        return self.nombre

    def update_email(self, new_email):
        self.__email = new_email

    def return_email(self):
        return self.__email

    def __show_age(self):
        return self.__age

    def show_age(self):
        return self.__get_age()

    def __get_age(self):
        return self.__age

    """sobrecarga de metodos"""

    def update_email(self, new_email, algo_mas):
        self.__email = new_email + algo_mas


# """
# We just can’t do it. Non-public methods are only
# allowed to be used inside our class definition.
# """
#
# tk = Persona('TK', 'tk@mail.com', 25)
# print tk.email()

# print(tk.__show_age())
# tk = Persona('TK', 'tk@mail.com')
# print(tk.email())  # => tk@mail.com
# tk._email = 'new_tk@mail.com'
# print(tk.email())  # => tk@mail.com
# tk.update_email('new_tk@mail.com')
# print(tk.email())  # => new_tk@mail.com

"""Polimormisfo"""

class Animal(object):
    def __init__(self, name):  # Constructor of the class
        self.name = name

    def talk(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")


class Cat(Animal):
    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        return 'Woof! Woof!'


animals = [Cat('Missy'), Cat('Mr. Mistoffelees'), Dog('Lassie')]

# print animals

for animal in animals:
    print animal.name + ': ' + animal.talk()

# prints the following:
#
# Missy: Meow!
# Mr. Mistoffelees: Meow!
# Lassie: Woof! Woof!
