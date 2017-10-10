
# Tipos de variables y asignacion
bool = True
name = "Craig"
age = 26
pi = 3.14159

# print(name + ' is ' + str(age) + ' years old.')
#
# print()

# print("Hola nombre")


"""Funciones"""

# retorno de una funcion
def get_message():
    return "hola hugo"


def happy_birthday_emily():
    print(get_message())
    print("Happy Birthday, dear Emily.")
    print("Happy Birthday to you!")

# happy_birthday_emily(msg1, msg2)

the_string = " "
the_string.format()
def get_sentence():
    return 'The sum of {} and {} is {}.'

def sumProblem(x, y):
    sum = x + y
    sentence = get_sentence().format(x, y, sum)
    print(sentence)

def hola():
    sumProblem(2, 3)
    sumProblem(1234567890123, 535790269358)
    a = int(input("Enter an integer: "))
    b = int(input("Enter another integer: "))
    sumProblem(a, b)

# hola()

"""Sentencias de control"""

def if_else_control():
    numero1 = 4
    numero2 = 5.0

    if (numero1 > numero2):
        print "{} mayor a {}".format(numero1, numero2)
    elif numero2 <= numero1:
        print "{} igual {}".format(numero1, numero2)
    else:
        print "error"



# tamano_de_string(len(un_string))

"""Bucles (ciclos)"""

# sentencia while
count = 0
while count <= 5:
   print count, " is  less than 5"
   count+=1
else:
   print count, " is not less than 5"


# sentencia for
for x in range(1, 10):
    print x


