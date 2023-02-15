import pygame
import sys
import Interface.Utils as ut
import Utils.JsonLoader as jsonL
import Interface.BattleWindow as bw
import Interface.Button as btn
import Interacoes as lib
import Interface.States.GameState as GameState
import Domain.Heroi as Heroi



class Title(GameState.GameState):
    def __init__(self, screen):
        super().__init__(screen)
        self.BackgroundImage = pygame.image.load(f'{self.imagePath}/Background/ahegao.jpg').convert_alpha()
        self.count = 0
        self.Active = False
        self.HeroName = ""
        self.NumberOfBtn = 3
        self.Boundary = jsonL.GetBoundaryThickness()
        self.CreateButtons()
        self.CreateEditBoxes()
        
    #endfunc

    def ScenesManager(self, alpha = 255):
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

    def CreateButtons(self):
        self.ButtonList = []
        for i in range(1,self.NumberOfBtn + 1):
            self.ButtonList.append(btn.Button(i,i, self.Screen))
        #endfor
    #endfunc

    def LoadButtons(self):
        for button in self.ButtonList:
            button.Draw()
        #endfor
    #endfunc

    def CreateEditBoxes(self):
        self.editboxAtributes = jsonL.GetEditBox()
        self.EditBox = pygame.Rect(self.editboxAtributes['x'],self.editboxAtributes['y'],self.editboxAtributes['width'],self.editboxAtributes['height'])
        self.EditboxSurface = pygame.Surface((self.editboxAtributes['width']-10,self.editboxAtributes['height']-10))
        self.EditBoxBoundaryColor = tuple(map(int,self.editboxAtributes['color'].split(',')))
        self.EditboxSurface.fill((20,20,20))
    #endfunc
    def LoadEditBox(self):
        self.Screen.blit(self.EditboxSurface, (self.editboxAtributes['x']+5,self.editboxAtributes['y']+5))
        pygame.draw.rect(self.Screen,self.EditBoxBoundaryColor, self.EditBox, self.Boundary)
        ut.InsertText(self.HeroName,jsonL.GetTitleTextColor(),self.editboxAtributes['x']+5,self.editboxAtributes['y']+5,self.Screen,textSize = jsonL.GetTextSize()*2)
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
            #NAO MEXER NO VALOR DO TICKS -> XGH: FUNCIONA NAO RELA
            if(pygame.time.get_ticks()>=300 and self.count == 0):
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
                # If the user clicked on the input_box rectangle.
                if self.EditBox.collidepoint(event.pos):
                    # Toggle the active variable.
                    self.Active = not self.Active
                else:
                    self.Active = False
                #endif
                hero = None
                if self.ButtonList[0].Button.collidepoint(event.pos):
                    # Turn button boundary White
                    self.ButtonList[0].SetBoundaryColor(255,255,255)
                elif self.ButtonList[1].Button.collidepoint(event.pos):
                    # Turn button boundary White
                    self.ButtonList[1].SetBoundaryColor(255,255,255)
                elif self.ButtonList[2].Button.collidepoint(event.pos):
                    # Turn button boundary White
                    self.ButtonList[2].SetBoundaryColor(255,255,255)
                #endif
            #endif
            if event.type == pygame.MOUSEBUTTONUP:
                hero = None
                r = 20
                g = 20
                b = 20
                if self.ButtonList[0].Button.collidepoint(event.pos):
                    # Turn button boundary Black
                    self.ButtonList[0].SetBoundaryColor(r,g,b)
                    hero =  self.CreateHero("Guerreiro")
                elif self.ButtonList[1].Button.collidepoint(event.pos):
                    # Turn button boundary Black
                    self.ButtonList[1].SetBoundaryColor(r,g,b)
                    hero =  self.CreateHero("Arqueiro")
                elif self.ButtonList[2].Button.collidepoint(event.pos):
                    # Turn button boundary Black
                    self.ButtonList[2].SetBoundaryColor(r,g,b)
                    hero =  self.CreateHero("Mago")
                else:
                    for button in self.ButtonList:
                        button.SetBoundaryColor(r,g,b)
                    #endfor
                #endif
                if (hero != None):
                    return hero
                #endif
            #endif
            if event.type == pygame.KEYDOWN:
                if self.Active:
                    if event.key == pygame.K_RETURN:
                        print(self.HeroName)
                        self.HeroName = ''
                    elif event.key == pygame.K_BACKSPACE:
                        self.HeroName = self.HeroName[:-1]
                    else:
                        if(len(self.HeroName)<8):
                            self.HeroName += event.unicode
                        #endif
            pygame.display.update()
        #endfor
    #endFunction

    def CreateHero(self, heroClass):
        hero = None
        if(self.HeroName == ""):
            self.EditBoxBoundaryColor = (255,0,0)
        else:
            hero = Heroi.Heroi(self.HeroName,heroClass)
        #endif
        return hero
    #endfunc
#endclass