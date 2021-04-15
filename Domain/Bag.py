import Domain.Arma as A
import Domain.Pocao as P
import os
class Bag:
    def __init__(self):
        self.items = []
    #endfunc
    def InserirArma(self, _nome, _dano):
        item = self.GetItem(_nome)
        if(item == None):
            arma = A.Arma(_nome, _dano)
            self.items.append([arma,1])
        else:
            item[1] += 1
        #endif
    #endfunc
    def InserirArma(self, arma):
        item = self.GetItem(arma.name)
        if(item == None):
            self.items.append([arma,1])
        else:
            item[1] += 1
        #endif
    #endfunc
    def InserirPot(self, _nome, _cargas, _heal, _tipo):
        item = self.GetItem(_nome)
        if(item == None):
            pocao = P.Pocao(_nome, _cargas, _heal, _tipo)
            self.items.append([pocao,1])
        else:
            item[1] += 1
        #endif
    #endfunc
    def RemoverPot(self, nome):
        item = self.GetItem(nome)
        if(item == None):
            print("item retornado é nulo")
        #endif
        self.items.remove(item)
    #endfunc
    def GetItem(self, nome):
        for item in self.items:
            if(item[0].name.lower() == nome.lower()):
                return item
            #endif
        #endfor
        return None
    #endfunc
    def ShowBag(self):
        for item in self.items:
            print(item[0].name)
        #endfor
        resp = input("Deseja a descrição de um item específico? (s/n)")
        if(resp != 'n'):
            self.SearchItem()
        #endif
    #endfunc
    def SearchItem(self):
        nomeItem = input("Qual o nome do item do qual deseja saber mais?\n")
        item = self.GetItem(nomeItem.lower())
        if(item == None):
            print("item desejado não existe")
        else:
            print(item[0].name + " --> dano:" + str(item[0].danoBase) + "  Qtd:" + str(item[1]))
        #endif
    #endfunc
#endclass