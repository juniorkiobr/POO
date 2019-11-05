empregados = []
class Empregado():
    def __init__(self,nome,sobreN,salario):
        self._nome = nome
        self._sobreN = sobreN
        self._salario = 0 if salario < 0 else salario
    @property
    def nome(self):
        return(self._nome)
    @nome.setter
    def nome(self,nome):
        self._nome = nome
    @property
    def sobreN(self):
        return(self._sobreN)
    @sobreN.setter
    def sobreN(self,sobreN):
        self._sobreN = sobreN
    @property
    def salario(self):
        return(self._salario)
    @salario.setter
    def salario(self,valor):
        try:
            valor = int(valor)
            self._salario = 0 if valor < 0 else valor
        except:
            print("Digite um número válido!!")
    def __str__(self):
        return(f'Nome: {self._nome}\nSobrenome: {self._sobreN}\nSalario: {self._salario}')

empregado = Empregado('Marcelo','Carvalho',-450)
print(empregado.__str__())
empregado.nome = 'João'
empregado.sobreN = 'Santos'
empregado.salario = '750'
print(empregado.__str__())
empregado.salario = '-750'
print(empregado.__str__())

def cria(nome,sobrenome,salario):
    temp = Empregado(nome,sobrenome,salario)
    empregados.append(temp)

cria('Marcelo','Carvalho',998)
cria('Arlene','Gonzaga', 1996)

def aumento(porcent):
    for i in empregados:
        i.salario = i.salario+(i.salario*porcent)/100
        print(i.__str__())

aumento(10)
