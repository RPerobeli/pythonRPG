import pygame
import sys
import random as rnd
import Interface.InterfaceUtils as ut
import Utils.JsonLoader as jsonL
import Interface.BattleWindow as bw
import Interacoes as lib
import Interface.States.GameState as GameState
#import Interface.Sound as Sound

class Inn(GameState.GameState):
    def __init__(self, screen, dialogBox, personagem, monstros, npcs = None):
        super().__init__(screen)
        self.ImagePath =  jsonL.GetImagePath()
        self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/quarto.jpg').convert_alpha()
        self.DialogBox = dialogBox
        self.Personagem = personagem
        self.Monstros = monstros
        self.Actors = []
        self.Actors[0] = personagem
        self.Npcs = npcs
        self.Alpha = 0
        self.Scene = 1
        self.Filename = "Introducao"
        self.MaxStoryIndex = 3
        self.Count = 0
        
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
        #endif
    #endfunc

    def SelectNextStory(self):
        self.Sound.StopMusic()
        if(self.Personagem.classe.lower() == 'guerreiro'):
            return (self.Personagem, 'caminhoTeofilo',True)
        elif(self.Personagem.classe.lower() == 'mago'):
            return (self.Personagem, 'caravana',True)
        elif(self.Personagem.classe.lower() == 'arqueiro'):
            return (self.Personagem, 'Recursos',True)
        else:
            print('erro ao selecionar proxima historia')
        #endif
    #endfunc
    
    def VerifyEvent(self):
        print('verificou possiveis eventos')
        if(self.StoryTextList[self.StoryListId]['txt'] == "battleCachorra\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Cao Infernal"), "quarto")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("inn")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "perde 2 de hp\n"):
            self.Personagem.HP -= 2
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "Temer\n"):
            self.Sound.PlaySFX("temer")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "removerCachorra\n"):
            print("removeu a cachorra")
            self.Actors.pop(1)
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "inserirCachorra\n"):
            print("inseriu a cachorra")
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Cao Infernal")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundCidade\n"):
            print('inseriu background')
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/SnowyCity.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirTaverneira\n"):
            print('inserir taverneira')
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/guild.jpg').convert_alpha()
            self.Actors[1] = lib.GetNpc(self.Npcs,"Jessie")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "perder10hp\n"):
            self.Personagem.HP -= 10
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        
    #endif

    def Update(self):
        #Cena tapa na cachorra
        pygame.display.set_caption("Hospedagem")
        self.VerifyFirstTimeInWindowToPlayMusic("inn")
        if(self.Scene == 1):
            self.StoryTextList = lib.SearchText(self.Filename,self.StoryIndex)
            self.Count += 1
        #endif
        self.ScenesManager()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            #endif
            if (event.type == pygame.KEYDOWN and (event.key == pygame.K_KP_ENTER or event.key == pygame.K_SPACE)):
                if(self.StoryListId == len(self.StoryTextList)-1):
                    if(self.isQuestion):
                        self.Sound.PlaySFX("cursorError")
                        print("Ta com pressa irmao? para de pular os dialogos.")
                    else:
                        self.Sound.PlaySFX("cursorForward")
                        self.isQuestion = True
                        self.StoryIndex += 1 
                        if(self.StoryIndex == self.MaxStoryIndex):
                            return self.SelectNextStory()
                        #endif
                        self.StoryTextList = lib.SearchText(self.Filename,self.StoryIndex)
                        self.StoryListId = 0 
                        self.VerifyEvent()
                else:
                    self.Sound.PlaySFX("cursorForward")
                    self.StoryListId += 1
                    self.Done = False
                    self.VerifyEvent()
                #endif
            #endif
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_1):
                self.Sound.PlaySFX("cursorForward")
                self.Personagem.Good += 1
                self.SearchAnswerByUserInput(1)
                self.VerifyEvent()
            #endif
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_2):
                self.Sound.PlaySFX("cursorForward")
                #self.Sound.PlaySFX("cursorForward")
                #self.Sound.PlaySFX("cursorForward")
                self.Personagem.Neutral += 1
                self.SearchAnswerByUserInput(2)
                self.VerifyEvent()
            #endif
            if (event.type == pygame.KEYDOWN and event.key == pygame.K_3):
                self.Sound.PlaySFX("cursorForward")
                self.Personagem.Evil += 1
                self.SearchAnswerByUserInput(3)
                self.VerifyEvent()
            #endif
        #endfor
        pygame.display.update()
        return self.Personagem,'inn', False
    #endFunction

#endclass
