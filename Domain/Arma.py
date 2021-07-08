#ToDo: Substituir atk especial por atk especial da ARMA
class Arma:
    def __init__(self, _name, _dano, _atkEspecial, _tag):
        self.name = _name
        self.danoBase = _dano
        self.durabilidade = 100
        self.textoAtkEspecial = _atkEspecial
        self.Tag = _tag
    #endfunc
#endclass
