conjuntos = []
class ConjuntoInteiros():
    def __init__(self,numeros:list,limite):
        self.numeros = numeros
        self.pertencem = []
        i = 0
        while i < len(numeros):
            self.pertencem.append(False)
            i += 1
        self.limite = limite
    def verificar(self):
        cont = 0
        for i in self.numeros:
            if i >= 0 and i <= self.limite:
                self.pertencem[cont] = True
            else:
                self.pertencem[cont] = False
            cont += 1
    def add(self,num):
        self.numeros.append(num)
        self.pertencem.append(False)
    def rem(self,num):
        cont = 0
        for x in self.numeros:
            if x == num:
                self.numeros.remove(num)
                self.pertencem.pop(cont)
            cont += 1
    @staticmethod
    def criar(numeros:list,limite):
        temp = ConjuntoInteiros(numeros,limite)
        conjuntos.append(temp)
    @staticmethod
    def uniao(c1,c2):
        cU = []
        for i in c1.numeros:
            for x in c2.numeros:
                if i == x and not ConjuntoInteiros.ispresent(cU,i) and not ConjuntoInteiros.ispresent(cU,x):
                    cU.append(i)
                elif ConjuntoInteiros.ispresent(cU,i) and not ConjuntoInteiros.ispresent(cU,x):
                    cU.append(x)
                elif ConjuntoInteiros.ispresent(cU,x) and not ConjuntoInteiros.ispresent(cU,i):
                    cU.append(i)
                elif ConjuntoInteiros.ispresent(cU,i):
                    pass
                elif ConjuntoInteiros.ispresent(cU,x):
                    pass
                else:
                    cU.append(i)
                    cU.append(x)
        cU.sort()
        return(cU)
    @staticmethod
    def difer(A,B):
        cD = ConjuntoInteiros.uniao(A,B)
        print(cD)
        for i in A.numeros:
            for x in B.numeros:
                if i == x:
                    try:
                        cD.remove(i)
                    except:
                        pass
                    
        cD.sort()
        return(cD)
    @staticmethod
    def inter(A,B):
        cI = []
        for i in A.numeros:
            for x in B.numeros:
                if i == x and not ConjuntoInteiros.ispresent(cI,i):
                    cI.append(i)
        cI.sort()
        return(cI)
    @staticmethod
    def ispresent(array,num):
        ispre = False
        for i in array:
            if i == num:
                ispre = True
                break
        return(ispre)
    def __str__(self):
        r = []
        for x,i in zip(self.numeros,self.pertencem):
            t = 'Pertence' if i == True else 'Não Pertence'
            r.append(f'{x}:{t}\n')
        r = ''.join(r)
        return(r)

test = ConjuntoInteiros([10,25,14,35], 17)
print(test.__str__())
test.verificar()
print(test.__str__())
test.rem(25)
print(test.__str__())
test.add(17)
print(test.__str__())
test.verificar()
print(test.__str__())

ConjuntoInteiros.criar([1,2,3], 10)
ConjuntoInteiros.criar([4,5,6], 10)
ConjuntoInteiros.criar([1,2,3], 10)
ConjuntoInteiros.criar([3,2,0,4,5,2,3], 10)

cont = 0
for i in conjuntos:
    print(f'{cont}[{i.__str__()}]')
    cont += 1
print(ConjuntoInteiros.uniao(conjuntos[0],conjuntos[1]))
print(ConjuntoInteiros.inter(conjuntos[2],conjuntos[3]))
print(ConjuntoInteiros.difer(conjuntos[2],conjuntos[3]))

