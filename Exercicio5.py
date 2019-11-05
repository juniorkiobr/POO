from datetime import date as dt
class Data():
    
    def __init__(self,dia = None,mes = None,ano = None,diaA = None, mesA = None, anoA = None):
        self.dia = None
        self.mes = None
        self.ano = None
        self.diaA = None
        self.mesA = None
        self.anoA = None
        
        if dia != None and mes != None and ano != None:
            self.dia = dia if ((dia > 0 and dia <=31 and (mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12)) or (dia > 0 and dia <= 30 and(mes == 4 or mes == 6 or mes == 9 or mes == 11)) or (dia > 0 and dia <= 29 and Data.bissexto(ano) and mes == 2) or (dia > 0 and dia <= 28 and not Data.bissexto(ano) and mes == 2)) else None
            self.mes = mes if (mes == 1 or mes == 2 or mes == 3 or mes == 4 or mes == 5 or mes == 6 or mes == 7 or mes == 8 or mes == 9 or mes == 10 or mes == 11 or mes == 12) else None
            self.ano = ano if dt.max.year >= ano and ano >= dt.min.year else None

        if diaA != None and mesA != None and anoA != None:
            data = dt.today()
            self.diaA = data.day
            self.mesA = data.month
            self.anoA = data.year
    @property
    def Dia(self):
        return self.dia 
    @Dia.setter
    def Dia(self,valor):
        try:
            self.dia = valor if ((valor > 0 and valor <=31 and (self.mes == 1 or self.mes == 3 or self.mes == 5 or self.mes == 7 or self.mes == 8 or self.mes == 10 or self.mes == 12)) or (valor > 0 and valor <= 30 and(self.mes == 4 or self.mes == 6 or self.mes == 9 or self.mes == 11)) or (valor > 0 and valor <= 29 and (self.ano%4 == 0 and self.ano%100 != 0 or self.ano%400 == 0) and self.mes == 2) or (valor > 0 and valor <= 28 and (self.ano%4 != 0 and self.ano%100 == 0 or self.ano%400 != 0) and self.mes == 2)) else None
        except:
            print("Digite primeiro o ano e mês para digitar o dia!!")
    @property
    def Mes(self):
        return self.mes
    @Mes.setter
    def Mes(self,valor):
        self.mes = valor if (valor == 1 or valor == 2 or valor == 3 or valor == 4 or valor == 5 or valor == 6 or valor == 7 or valor == 8 or valor == 9 or valor == 10 or valor == 11 or valor == 12) else None
    @property
    def Ano(self):
        return self.ano 
    @Ano.setter
    def Ano(self,valor):
        self.ano = valor if dt.max.year >= valor and valor >= dt.min.year else None
    @property
    def DiaA(self):
        return self.diaA
    @DiaA.setter
    def DiaA(self,valor):
        try:
            self.diaA = valor if ((valor > 0 and valor <=31 and (self.mes == 1 or self.mes == 3 or self.mes == 5 or self.mes == 7 or self.mes == 8 or self.mes == 10 or self.mes == 12)) or (valor > 0 and valor <= 30 and(self.mes == 4 or self.mes == 6 or self.mes == 9 or self.mes == 11)) or (valor > 0 and valor <= 29 and (self.ano%4 == 0 and self.ano%100 != 0 or self.ano%400 == 0) and self.mes == 2) or (valor > 0 and valor <= 28 and (self.ano%4 != 0 and self.ano%100 == 0 or self.ano%400 != 0) and self.mes == 2)) else None
        except:
            print("Digite primeiro o ano e mês para digitar o dia!!")
    @property
    def MesA(self):
        return self.mesA
    @MesA.setter
    def MesA(self,valor):
        self.mesA = valor if (valor == 1 or valor == 2 or valor == 3 or valor == 4 or valor == 5 or valor == 6 or valor == 7 or valor == 8 or valor == 9 or valor == 10 or valor == 11 or valor == 12) else None
    @property
    def AnoA(self):
        return self.anoA 
    @AnoA.setter
    def AnoA(self,valor):
        self.anoA = valor if dt.max.year >= valor and valor >= dt.min.year else None
    def avancar(self):
        self.dia += 1
        if ((self.dia > 30 and (self.mes == 4 or self.mes == 6 or self.mes == 9 or self.mes == 11)) or (self.dia > 31 and (self.mes == 1 or self.mes == 3 or self.mes == 5 or self.mes == 7 or self.mes == 8 or self.mes == 10 or self.mes == 12)) or (self.dia > 28 and not Data.bissexto(self.ano) and self.mes == 2) or (self.dia > 29 and Data.bissexto(self.ano) and self.mes == 2)):
            self.dia = 1
            self.mes += 1
            if(self.mes > 12):
                self.mes = 1
                self.ano += 1
    @staticmethod
    def bissexto(ano):
        if(ano%4 == 0 and ano%100 != 0):
            return True
        elif(ano%400 == 0):
            return True
        else:
            return False
    def __str__(self):
        if (self.dia != None and self.mes != None and self.ano != None) and not (self.diaA != None and self.mesA != None and self.anoA != None):
            return(f'{self.dia}/{self.mes}/{self.ano}')
        elif (self.diaA != None and self.mesA != None and self.anoA != None) and not (self.dia != None and self.mes != None and self.ano != None):
            return(f'{self.diaA}/{self.mesA}/{self.anoA}')
        elif (self.dia != None and self.mes != None and self.ano != None) and (self.diaA != None and self.mesA != None and self.anoA != None):
             return(f'Data Inserida: {self.dia}/{self.mes}/{self.ano}\n\n Data Atual: {self.diaA}/{self.mesA}/{self.anoA}')
        else:
            print("Nenhuma data inserida!!")
print('Avançar:. ')
data = Data(28,2,2020)
print(data.__str__())
data.avancar()
print(data.__str__())
print("\nAvançar (ano):.")
data = Data(31,12,2019)
print(data.__str__())
data.avancar()
print(data.__str__())

data = Data(diaA= 1, mesA= 1, anoA= 1)
print(f'Dia Atual: {data.__str__()}\n')
data = Data(28,2,2019,1,1,1)
print(data.__str__())