import pygame
import Interface.Utils as ut
import Utils.JsonLoader as jsonL
import Interface.BattleWindow as bw
import Interacoes as lib

class Inn:
    def __init__(self, screen, dialogBox, personagem):
        imagePath =  jsonL.GetImagePath()
        self.BackgroundImage = pygame.image.load(f'{imagePath}/Background/quarto.jpg').convert_alpha()
        self.DialogBox = dialogBox
        self.Screen = screen
        self.FrameRate = jsonL.GetFrameRate()
        self.Clock = pygame.time.Clock()
        self.Actors = personagem
    #endfunc

    def LoadImages(self):
        ut.InsertBackground(self.BackgroundImage, self.Screen)
        ut.InsertImage(self.Actors.Image.File, self.Actors.Image.Width, self.Actors.Image.Height, 0,200, self.Screen)
        ut.InsertImage(self.DialogBox.image,self.DialogBox.Width,self.DialogBox.Height, self.DialogBox.x, self.DialogBox.y, self.Screen)
    #endfunc

    def LoadText(self, text):
        text_color = jsonL.GetSpeakerTextColor()
        (x,y) = jsonL.GetSpeakerTextPosition()
        ut.InsertText(text,text_color, x, y, self.Screen)
        #endfunc


    def InnDialog1(self):
        arq = "Arquivostxt/Introducao.txt"
        lib.SubstituiNomeHeroiNoArquivo(arq, self.Actors.name)
        #Cena tapa na cachorra
        pygame.display.set_caption("Hospedagem")
        run = True
        while run:
            self.Clock.tick(self.FrameRate)
            self.LoadImages()
            self.LoadText(lib.ProcuraTexto("Q1-ini", "Q1-fim", arq, self.Actors.name,self.Screen))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                #endif
            #endfor
            pygame.display.update()
        #endwhile
    #endFunction

#endclass
