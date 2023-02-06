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
        self.ImagePath =  jsonL.GetImagePath()
        self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/quarto.jpg').convert_alpha()
        self.DialogBox = dialogBox
        self.Personagem = personagem
        self.Monstros = monstros
        self.Actors = []
        self.Actors.append(personagem)
        self.Npcs = npcs
        self.Alpha = 0
        self.Scene = 1
        self.Filename = "Introducao"
        self.MaxStoryIndex = 3
        
    #endfunc

    def ScenesManager(self):
        if (self.Scene == 2):
            actorPos = self.PlaceActors()
            self.LoadImages(actorPos)
            self.LoadTextWithList(self.StoryTextList[self.StoryListId])
        elif ((self.Scene == 1)):
            actorPos = self.PlaceActors()
            if (self.Alpha <= 255):
                self.FadeIn(actorPos)
            else:    
                self.LoadImages(actorPos)
                self.Scene += 1
            #endif
        else:
            print("erro ao entrar nas Cenas -> inn.ScenesManager()")

    def LoadImages(self, actorPos):
        ut.InsertBackground(self.BackgroundImage, self.Screen)
        ut.InsertImage(self.Actors[0].Image.File, self.Actors[0].Image.Width, self.Actors[0].Image.Height, actorPos['x0'],actorPos['y0'], self.Screen)
        if(len(self.Actors) > 1):
            ut.InsertImage(self.Actors[1].Image.File, self.Actors[1].Image.Width, self.Actors[1].Image.Height, actorPos['x1'],actorPos['y1'], self.Screen,self.Alpha)
                #endif
        ut.InsertImage(self.DialogBox.image,self.DialogBox.Width,self.DialogBox.Height, self.DialogBox.x, self.DialogBox.y, self.Screen)
        #endif
    #endfunc



    def SelectNextStory(self):
        if(self.Personagem.classe.lower() == 'guerreiro'):
            return (self.Personagem, 'caminhoTeofilo')
        elif(self.Personagem.classe.lower() == 'mago'):
            return (self.Personagem, 'caravana')
        elif(self.Personagem.classe.lower() == 'arqueiro'):
            return (self.Personagem, 'caravana')
        else:
            print('erro ao selecionar proxima historia')
        #endif
    #endfunc
    
    def VerifyEvent(self):
        print('verificou possiveis eventos')
        if(self.StoryTextList[self.StoryListId]['txt'] == "battleCachorra\n"):
            print("criar tela de batalha")
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "perde 2 de hp\n"):
            self.Personagem.HP -= 2
            self.StoryListId += 2
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "removerCachorra\n"):
            print("removeu a cachorra")
            self.Actors.pop(1)
            self.StoryListId += 1
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "inserirCachorra\n"):
            print("inseriu a cachorra")
            self.Actors.append(lib.GetMonstro(self.Monstros,"Cao Infernal"))
            self.StoryListId += 2
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundCidade\n"):
            print('inseriu background')
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/SnowyCity.png').convert_alpha()
            self.StoryListId += 1
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirTaverneira\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/guild.png').convert_alpha()
            print('inserir taverneira')
            self.StoryListId += 1
            return
        #endif
        
    #endif

    def Update(self):
        #Cena tapa na cachorra
        pygame.display.set_caption("Hospedagem")
        if(self.Scene == 1):
            self.StoryTextList = lib.SearchText(self.Filename,self.StoryIndex)
        #endif
        self.ScenesManager()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #endif
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_KP_ENTER):
                if(self.StoryListId == len(self.StoryTextList)-1):
                    if(self.isQuestion):
                        print("Ta com pressa irmao? para de pular os dialogos.")
                    else:
                        self.isQuestion = True
                        self.StoryIndex += 1 
                        if(self.StoryIndex == self.MaxStoryIndex):
                            return self.SelectNextStory()
                        #endif
                        self.StoryTextList = lib.SearchText(self.Filename,self.StoryIndex)
                        self.StoryListId = 0 
                else:
                    self.StoryListId += 1
                    self.VerifyEvent()
                #endif
            #endif
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_1):
                self.SearchAnswerByUserInput(1)
                self.VerifyEvent()
            #endif
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_2):
                self.SearchAnswerByUserInput(2)
                self.VerifyEvent()
            #endif
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_3):
                self.SearchAnswerByUserInput(3)
                self.VerifyEvent()
            #endif
        #endfor
        pygame.display.update()
        return self.Personagem,'inn'
    #endFunction

#endclass
