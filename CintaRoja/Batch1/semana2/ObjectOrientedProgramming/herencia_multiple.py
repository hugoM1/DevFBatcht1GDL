class Base1(object):
    def __init__(self, atributo_base1):
        self.atributo_base1 = atributo_base1

    def metodo_base1(self):
        print "imprimiendo atributo  desde base1 atributo1", self.atributo_base1


class Base2:

    def metodo_base2(self):
        print "imprimiendo atributo  desde base2 atributo2"


class MultiDerived(Base1, Base2):
    def __init__(self, atributo1_para_base1):
        super(MultiDerived, self).__init__(atributo1_para_base1)

    def metodo_multi_derived(self):
        print "imprimiendo desde multi_derived"


objeto_multi_herencia = MultiDerived("el atributo2 para base1")
objeto_multi_herencia.metodo_base1()
objeto_multi_herencia.metodo_base2()
objeto_multi_herencia.metodo_multi_derived()
