class Digitais():
    @staticmethod
    def AND(expr):
        res = expr.split('.')
        while len(res) > 1:
            try:
                if(res[0] == '1' and res[1] == '1'):
                    res.append('1')
                    res.pop(0)
                    res.pop(0)
                else:
                    res.append('0')
                    res.pop(0)
                    res.pop(0)
            except:
                pass
        print(res)
    @staticmethod
    def OR(expr):
        res = expr.split('+')
        while len(res) > 1:
            try:
                if(res[0] == '0' and res[1] == '0'):
                    res.append('0')
                    res.pop(0)
                    res.pop(0)
                else:
                    res.append('1')
                    res.pop(0)
                    res.pop(0)
            except:
                pass
        print(res)
    @staticmethod
    def XOR(expr):
        res = expr.split('+')
        while len(res) > 1:
            try:
                if((res[0] == '0' and res[1] == '0') or (res[0] == '1' and res[1] == '1')):
                    res.append('0')
                    res.pop(0)
                    res.pop(0)
                else:
                    res.append('1')
                    res.pop(0)
                    res.pop(0)
            except:
                pass
        return(res[0])