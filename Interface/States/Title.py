import pygame
import sys
import Interface.Utils as ut
import Utils.JsonLoader as jsonL
import Interface.BattleWindow as bw
import Interface.Button as btn
import Interacoes as lib
import Interface.States.GameState as GameState
import Domain.Personagem as Personagem



class Title(GameState.GameState):
    def __init__(self, screen):
        super().__init__(screen)
        self.BackgroundImage = pygame.image.load(f'{self.imagePath}/Background/ahegao.jpg').convert_alpha()
        self.count = 0
        self.Active = False
        self.HeroName = ""
        self.NumberOfBtn = 3
        self.Boundary = jsonL.GetBoundaryThickness()
    #endfunc

    def LoadImages(self, alpha = 255):
        ut.InsertBackground(self.BackgroundImage, self.Screen, alpha)
        if(self.count==1):
            self.LoadTitle("D&D DA DEEPWEP")
            pos = jsonL.GetNameTextPosition()
            ut.InsertText("Nome:", jsonL.GetTitleTextColor(),pos['x'], pos['y'],self.Screen,textSize = jsonL.GetTextSize()*2)
            self.LoadEditBox()
            pos = jsonL.GetClassePosition()
            ut.InsertText("Classes:", jsonL.GetTitleTextColor(),pos['x'], pos['y'],self.Screen,textSize = jsonL.GetTextSize()*2)
            self.LoadButtons()
        #endif
    #endfunc

    def LoadButtons(self):
        buttonList = []
        for i in range(1,self.NumberOfBtn + 1):
            buttonList.append(btn.Button(i,i, self.Screen))
        #endfor
        for button in buttonList:
            button.Draw()
        #endfor
    #endfunc

    def LoadEditBox(self):
        editbox = jsonL.GetEditBox()
        self.EditBox = pygame.Rect(editbox['x'],editbox['y'],editbox['width'],editbox['height'])
        editboxSurface = pygame.Surface((editbox['width']-10,editbox['height']-10))
        editboxSurface.fill((20,20,20))
        self.Screen.blit(editboxSurface, (editbox['x']+5,editbox['y']+5))
        color = tuple(map(int,editbox['color'].split(',')))
        pygame.draw.rect(self.Screen,color, self.EditBox, self.Boundary)
        ut.InsertText(self.HeroName,jsonL.GetTitleTextColor(),editbox['x']+5,editbox['y']+5,self.Screen,textSize = jsonL.GetTextSize()*2)
    #endfunc

    def LoadTitle(self, text):
        text_color = jsonL.GetTitleTextColor()
        (x,y) = (jsonL.GetTitleTextPosition())
        titleFont = jsonL.GetTitleFont()
        size = jsonL.GetTitleTextSize()
        ut.InsertText(text,text_color, x, y, self.Screen,fontName = titleFont, textSize = size)
    #endfunc

    def Update(self):

        pygame.display.set_caption("Título")
        for event in pygame.event.get():
            if(pygame.time.get_ticks()>=400 and self.count == 0):
                self.BackgroundImage = pygame.Surface((self.Screen.get_width(), self.Screen.get_height()))
                self.BackgroundImage.fill((45,45,45))
                self.BackgroundImage.set_alpha(255)
                self.count = 1
            #endif
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #endif
            if event.type == pygame.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if self.EditBox.collidepoint(event.pos):
                    # Toggle the active variable.
                    self.Active = not self.Active
                else:
                    self.Active = False
                #endif
            if event.type == pygame.KEYDOWN:
                if self.Active:
                    if event.key == pygame.K_RETURN:
                        print(self.HeroName)
                        self.HeroName = ''
                    elif event.key == pygame.K_BACKSPACE:
                        self.HeroName = self.HeroName[:-1]
                    else:
                        self.HeroName += event.unicode
            pygame.display.update()
        #endfor
    #endFunction

#endclass