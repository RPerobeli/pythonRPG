import Arma
import Pocao
class Bag:
    items = []
    def InserirArma(self,_nome, _dano):
        item = self.GetItem(_nome)
        if(item == None):
            arma = Arma(_nome, _dano)
            self.items.append([arma,1])
        else:
            item[1] += 1
        #endif
    #endfunc
    def InserirPot(self, _nome, _cargas, _heal, _tipo):
        item = self.GetItem(_nome)
        if(item == None):
            pocao = Pocao(_nome, _cargas, _heal, _tipo)
            self.items.append([pocao,1])
        else:
            item[1] += 1
        #endif
    #endfunc
    def RemoverPot(self, nome):
        item = self.GetItem(nome)
        self.items.remove(item)
    #endfunc
    def GetItem(self, nome):
        for item in self.items:
            if(item[0] == nome):
                return item
            #endif
        #endfor
        return None
    #endfunc
#endclass