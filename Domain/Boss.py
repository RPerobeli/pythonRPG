import Domain.Monstro as monstro


class Boss(monstro.Monstro):
    def __init__(self, nome, classe):
        super().__init__(nome, classe)
        self.atk = 15
    # endfunc
# endclass
