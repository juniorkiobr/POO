#Representação c = x + yi
import numpy as np
complexos = []
class Complexos():
    def __init__(self, id, funcao):
        self.id = id
        self.igual = funcao.split('=')
        for i in self.igual[1]:
            if i == '+':
                self.funcao = self.igual[1].split('+')
            elif i == '-':
                self.funcao = self.igual[1].split('-')
                self.funcao[1] = '-' + self.funcao[1]
        self.real = None
        self.imaginario = None
        self.angulo = None
        self.modulo = None

        self.ex_real()
        self.ex_imaginario()
        self.Angulo()
        self.Z()
    def ex_real(self):
        numero = ''
        for i in self.funcao[0]:
            if i == '-':
                numero = numero+i
            elif(i == '0' or i =='1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9'):
                numero = numero+i
        self.real = int(numero)
    def ex_imaginario(self):
        numero = ''
        for i in self.funcao[1]:
            if i == '-':
                numero = numero+i
            elif(i == '0' or i =='1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9'):
                numero = numero+i
        self.imaginario = int(numero)
    def Z(self):
        resultado = (self.real**2 + self.imaginario**2)**(1/2)
        if resultado < 0:
            resultado *= -1
        return resultado
    def Angulo(self):
        self.angulo = np.arctan2(self.imaginario,self.real)
    @staticmethod
    def Criar(funcao):
        id = complexos.__len__() + 1
        comp = Complexos(id,funcao)
        complexos.append(comp)
    @staticmethod
    def soma(ID1, ID2):
        Encontrado = False
        func1 = None
        func2 = None
        for i in complexos:
            if i.id == ID1:
                func1 = [i.real,i.imaginario]
            elif i.id == ID2:
                func2 = [i.real,i.imaginario]
            elif func1 != None and func2 != None:
                Encontrado = True
        if Encontrado:
            id = complexos.__len__() + 1
            Complexos.Criar(f'c = {func1[0]+func2[0]}+{func1[1]+func2[1]}i')
            print(f"Criado no id {id}")
        else:
            print("Não Encontrado!!") 
    @staticmethod
    def sub(ID1, ID2):
        Encontrado = False
        func1 = None
        func2 = None
        for i in complexos:
            if i.id == ID1:
                func1 = [i.real,i.imaginario]
            elif i.id == ID2:
                func2 = [i.real,i.imaginario]
            elif func1 != None and func2 != None:
                Encontrado = True
        if Encontrado:
            id = complexos.__len__() + 1
            Complexos.Criar(f'c = {func1[0]-func2[0]}+{func1[1]-func2[1]}i')
            print(f"Criado no id {id}")
        else:
            print("Não Encontrado!!") 
    @staticmethod
    def mul(ID1, ID2):
        Encon1 = False
        Encon2 = False
        func1 = None
        func2 = None
        for i in complexos:
            if i.id == ID1:
                func1 = [i.real,i.imaginario]
                Encon1 = True
            elif i.id == ID2:
                func2 = [i.real,i.imaginario]
                Encon2 = True
        if Encon1 and Encon2:
            id = complexos.__len__() + 1
            rs1 = func1[0]*func2[0] - func1[1]*func2[1]
            rs2 = func1[0]*func2[1] + func1[1]*func2[0]
            if(rs2 < 0):
                Complexos.Criar(f'c = {rs1}{rs2}i')
            else:
                Complexos.Criar(f'c = {rs1}+{rs2}i')
            
            print(f"Criado no id {id}")
        else:
            print("Não Encontrado!!") 
    @staticmethod
    def dv(ID1, ID2):
        Encon1 = False
        Encon2 = False
        func1 = None
        func2 = None
        for i in complexos:
            if i.id == ID1:
                func1 = [i.real,i.imaginario]
                Encon1 = True
            elif i.id == ID2:
                func2 = [i.real,i.imaginario]
                Encon2 = True
        if Encon1 and Encon2:
            if(func2[0]*func1[1]-func1[0]*func2[1]) > 0:
                return (f'{func1[0]*func2[0] + func1[1]*func2[1]}+{(func2[0]*func1[1]-func1[0]*func2[1])}i/{func2[0]**2+func2[1]**2}')
            else:
                return (f'{func1[0]*func2[0] + func1[1]*func2[1]}{(func2[0]*func1[1]-func1[0]*func2[1])}i/{func2[0]**2+func2[1]**2}')
        else:
            print("Não Encontrado!!") 
    @staticmethod
    def inverso(id):
        Encon1 = False
        for i in complexos:
            if i.id == id:
                func1 = [i.real,i.imaginario]
                Encon1 = True
        if Encon1:
            if (int(func1[1]) > 0):
                Cinv = f'{func1[0]}{int(func1[1])*-1}i/{int(func1[0])**2 + int(func1[1])**2}'
            else:
                Cinv = f'{func1[0]}+{int(func1[1])*-1}i/{int(func1[0])**2 + int(func1[1])**2}'
            return(Cinv)
        else:
            print("Não Encontrado!!") 

    def __repr__(self):
        return(f'{self.id} {self.igual[0]}={self.igual[1]}')
    @staticmethod
    def relacionais(ID1, ID2):
        Encon1 = False
        Encon2 = False
        func1 = None
        func2 = None
        for i in complexos:
            if i.id == ID1:
                func1 = [i.real,i.imaginario]
                Encon1 = True
            elif i.id == ID2:
                func2 = [i.real,i.imaginario]
                Encon2 = True
        if Encon1 and Encon2:
            if(func1 == func2):
                return('Iguais')
            else:
                return('Diferentes')
          
Complexos.Criar('c = 5 + 1i')
Complexos.Criar('c = 2 - 1i')
Complexos.Criar('c = 4 + 2i')
Complexos.Criar('c = 5 + 1i')
Complexos.Criar('c = 1 + 3i')
Complexos.Criar('c = 1 - 1i')
Complexos.mul(1,2)
Complexos.soma(1,3)
Complexos.sub(3,4)
print(Complexos.dv(5,6))
print(Complexos.inverso(3))
print(Complexos.relacionais(1,4))
print(Complexos.relacionais(1,2))
for i in complexos:
    print(i)

        