class JogoDaVelha():
    def __init__(self):
        self._jogadores = ['x','0']
        self._jogo = [['?','?','?'],['?','?','?'],['?','?','?']]
        self._jgAtual = self._jogadores[0]
    def grade(self):
        print(f'{self._jogo[0]}\n{self._jogo[1]}\n{self._jogo[2]}')
    def jogo(self):
        posx = None
        posy = None
        win = False
        while win == False:
            self.grade()
            jog = 1
            posx = int(input(f'Jogador {self._jgAtual} escolha o X(0-2):.'))
            posy = int(input(f'Jogador {self._jgAtual} escolha o Y(0-2):.'))
            if(self._jogo[posx][posy] == '?'):
                self._jogo[posx][posy] = self._jgAtual   
                jog += 1             
            else:
                print("Já utilizado!!")
            try:
                if(self._jogo[posx][posy] == self._jgAtual and self._jogo[posx+1][posy] == self._jgAtual and self._jogo[posx+2][posy] == self._jgAtual):
                    print(f"{self._jgAtual} ganhou!1")
                    win = True
            except:
                pass
            
            try:
                if(self._jogo[posx][posy] == self._jgAtual and self._jogo[posx+1][posy] == self._jgAtual and self._jogo[posx-1][posy] == self._jgAtual):
                    print(f"{self._jgAtual} ganhou!2")
                    win = True
            except:
                pass

            try:   
                if(self._jogo[posx][posy] == self._jgAtual and self._jogo[posx-1][posy] == self._jgAtual and self._jogo[posx-2][posy] == self._jgAtual):
                    print(f"{self._jgAtual} ganhou!3")
                    win = True
            except:
                pass

            try:
                if(self._jogo[posx][posy] == self._jgAtual and self._jogo[posx][posy+1] == self._jgAtual and self._jogo[posx][posy+2] == self._jgAtual):
                    print(f"{self._jgAtual} ganhou!4")
                    win = True
            except:
                pass
            
            try:
                if(self._jogo[posx][posy] == self._jgAtual and self._jogo[posx][posy+1] == self._jgAtual and self._jogo[posx][posy-1] == self._jgAtual):
                    print(f"{self._jgAtual} ganhou!5")
                    win = True
            except:
                pass

            try:
                if(self._jogo[posx][posy] == self._jgAtual and self._jogo[posx][posy-1] == self._jgAtual and self._jogo[posx][posy-2] == self._jgAtual):
                    print(f"{self._jgAtual} ganhou!6")
                    win = True
            except:
                pass
            
            try:
                if(self._jogo[posx][posy] == self._jgAtual and self._jogo[posx+1][posy+1] == self._jgAtual and self._jogo[posx+2][posy+2] == self._jgAtual):
                    print(f"{self._jgAtual} ganhou!7")
                    win = True
            except:
                pass

            try:
                if(self._jogo[posx][posy] == self._jgAtual and self._jogo[posx+1][posy+1] == self._jgAtual and self._jogo[posx-1][posy-1] == self._jgAtual):
                    print(f"{self._jgAtual} ganhou!8")
                    win = True
            except:
                pass

            try:
                if(self._jogo[posx][posy] == self._jgAtual and self._jogo[posx-1][posy-1] == self._jgAtual and self._jogo[posx-2][posy-2] == self._jgAtual):
                    print(f"{self._jgAtual} ganhou!9")
                    win = True
            except:
                pass

            try:
                if(self._jogo[posx][posy] == self._jgAtual and self._jogo[posx-1][posy+1] == self._jgAtual and self._jogo[posx-2][posy+2] == self._jgAtual):
                    print(f"{self._jgAtual} ganhou!10")
                    win = True
            except:
                pass

            try:
                if(self._jogo[posx][posy] == self._jgAtual and self._jogo[posx+1][posy-1] == self._jgAtual and self._jogo[posx-1][posy+1] == self._jgAtual):
                    print(f"{self._jgAtual} ganhou!11")
                    win = True
            except:
                pass

            try:
                if(self._jogo[posx][posy] == self._jgAtual and self._jogo[posx+1][posy+1] == self._jgAtual and self._jogo[posx+2][posy+2] == self._jgAtual):
                    print(f"{self._jgAtual} ganhou!12")
                    win = True
            except:
                pass
            
            if self._jgAtual == self._jogadores[0]:
                self._jgAtual = self._jogadores[1]
            else:
                self._jgAtual = self._jogadores[0]
teste = JogoDaVelha()
teste.jogo()

