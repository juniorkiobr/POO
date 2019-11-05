class Fatura():
    def __init__(self,nItem,desc,quantC,preco):
        self._nItem = nItem
        self._desc = desc
        self._quantC = 0 if quantC < 0 else quantC
        self._preco = 0. if preco < 0 else preco
    @property
    def nItem(self):
        return(self._nItem)
    @nItem.setter
    def nItem(self,nItem):
        self._nItem = nItem
    @property
    def desc(self):
        return(self._desc)
    @desc.setter
    def desc(self,desc):
        self._desc = desc
    @property
    def quantC(self):
        return(self._quantC)
    @quantC.setter
    def quantC(self,quantC):
        try:
            quantC = int(quantC)
            if quantC < 0:
                self._quantC = 0
            else:
                self._quantC = quantC
        except:
            print("Por favor digite um número válido!!")
    @property
    def preco(self):
        return(self._preco)
    @preco.setter
    def preco(self,preco):
        try:
            preco = int(preco)
            if preco < 0:
                self._preco = 0.
            else:
                self._preco = preco
        except:
            print("Por favor digite um número válido!!")
    
    def get_valor_fatura(self):
        print(f'O valor da fatura é:{self._quantC * self._preco}')

fatura = Fatura('0001','Banana Grade',10,1.50)
fatura.get_valor_fatura()
    
    