        if(resp <= 0 or resp > cont):
            print("vai se fuder QA")
            lib.LimpaConsole()
            magiaSelecionada = self.SelectMagia(personagem)
            if(magiaSelecionada != None):
                return magiaSelecionada
            # endif
        else:
            return personagem.magias[resp-1]