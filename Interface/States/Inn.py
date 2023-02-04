import pygame
import sys
import Interface.Utils as ut
import Utils.JsonLoader as jsonL
import Interface.BattleWindow as bw
import Interacoes as lib
import Interface.States.GameState as GameState

class Inn(GameState.GameState):
    def __init__(self, screen, dialogBox, personagem, monstros, npcs = None):
        super().__init__(screen)
        imagePath =  jsonL.GetImagePath()
        self.BackgroundImage = pygame.image.load(f'{imagePath}/Background/quarto.jpg').convert_alpha()
        self.DialogBox = dialogBox
        self.Personagem = personagem
        self.Monstros = monstros
        self.Actors = []
        self.Actors.append(personagem)
        self.Npcs = npcs
        self.Alpha = 0
        self.Scene = 1
        arq = "Arquivostxt/Introducao.txt"
        lib.SubstituiNomeHeroiNoArquivo(arq, self.Personagem.name)
    #endfunc

    def LoadImages(self):
        if (self.Scene == 2):
            actorPos = self.PlaceActors()
            ut.InsertBackground(self.BackgroundImage, self.Screen)
            ut.InsertImage(self.Actors[0].Image.File, self.Actors[0].Image.Width, self.Actors[0].Image.Height, actorPos['x0'],actorPos['y0'], self.Screen)
            ut.InsertImage(self.DialogBox.image,self.DialogBox.Width,self.DialogBox.Height, self.DialogBox.x, self.DialogBox.y, self.Screen)
        elif ((self.Scene == 1)):
            actorPos = self.PlaceActors()
            if (self.Alpha <= 255):
                ut.InsertBackground(self.BackgroundImage, self.Screen,255)
                ut.InsertImage(self.Actors[0].Image.File, self.Actors[0].Image.Width, self.Actors[0].Image.Height, actorPos['x0'],actorPos['y0'], self.Screen,self.Alpha)
                ut.InsertImage(self.DialogBox.image,self.DialogBox.Width,self.DialogBox.Height, self.DialogBox.x, self.DialogBox.y, self.Screen, self.Alpha)
                self.Alpha+=1
            else:    
                ut.InsertBackground(self.BackgroundImage, self.Screen)
                ut.InsertImage(self.Actors[0].Image.File, self.Actors[0].Image.Width, self.Actors[0].Image.Height, actorPos['x0'],actorPos['y0'], self.Screen)
                ut.InsertImage(self.DialogBox.image,self.DialogBox.Width,self.DialogBox.Height, self.DialogBox.x, self.DialogBox.y, self.Screen)
                self.Scene += 1
            #endif
        else:
            print("else")
        #endif
    #endfunc

    def LoadText(self, text):
        text_color = jsonL.GetSpeakerTextColor()
        (x,y) = jsonL.GetSpeakerTextPosition()
        ut.InsertText(text,text_color, x, y, self.Screen)
    #endfunc


    def Update(self):
        #Cena tapa na cachorra
        pygame.display.set_caption("Hospedagem")
        self.LoadImages()
        #self.LoadText(lib.ProcuraTexto("Q1-ini", "Q1-fim", arq, self.Actors.name,self.Screen))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #endif
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER):
                pygame.quit()
                sys.exit()
            #endif
        #endfor
        pygame.display.update()

    #endFunction

#endclass
