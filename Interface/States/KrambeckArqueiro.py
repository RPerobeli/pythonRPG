import pygame
import sys
#import Interface.Utils as ut
import Utils.JsonLoader as jsonL
import Interface.BattleWindow as bw
import Interface.GameOverWindow as gow
import Interacoes as lib
import Interface.States.GameState as GameState

class KrambeckArqueiro(GameState.GameState):
    def __init__(self, screen, dialogBox, personagem, monstros, npcs = None, armas= None):
        super().__init__(screen)
        self.ImagePath =  jsonL.GetImagePath()
        self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/Krambeck.jpg').convert_alpha()
        self.DialogBox = dialogBox
        self.Personagem = personagem
        self.Monstros = monstros
        self.Actors = []
        self.Actors.append(personagem)
        self.Npcs = npcs
        self.Alpha = 255
        self.Scene = 1
        self.Filename = "KrambeckArqueiro"
        self.MaxStoryIndex = 4
        self.Count = 0
        self.Armas = armas
        
    #endfunc

    def ScenesManager(self):
        if (self.Scene == 1):
            actorPos = self.PlaceActors()
            self.LoadImages(actorPos)
            self.LoadTextWithList(self.StoryTextList[self.StoryListId], heroName=self.Personagem.name)
        else:
            print("erro ao entrar nas Cenas -> inn.ScenesManager()")
        #endif
    #endfunc

    def SelectNextStory(self):
        return (self.Personagem, self.NextStory, True)
    #endfunc
    
    def VerifyEvent(self):
        print('verificou possiveis eventos')
        if(self.StoryTextList[self.StoryListId]['txt'] == "RemoverAtor1\n"):
            self.Actors.pop(1)
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        #endif

        #region NPCs
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirPelegolas\n"):
            self.Actors.append(lib.GetNpc(self.Npcs,"Pelegolas"))
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirFerreiro\n"):
            self.Actors.append(lib.GetNpc(self.Npcs,"Ferreiro"))
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirElfaFloresta\n"):
            self.Actors.append(lib.GetNpc(self.Npcs,"Elfa da Floresta"))
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirElfoFloresta2\n"):
            self.Actors.append(lib.GetNpc(self.Npcs,"Elfo da Floresta2"))
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirElfoFloresta\n"):
            self.Actors.append(lib.GetNpc(self.Npcs,"Elfo da Floresta"))
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirAltoElfo\n"):
            self.Actors.append(lib.GetNpc(self.Npcs,"Alto Elfo"))
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirEndilien\n"):
            self.Actors.append(lib.GetNpc(self.Npcs,"Endilien"))
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirMago\n"):
            self.Actors.append(lib.GetNpc(self.Npcs,"Mago"))
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        #endregion
        
        #region Sound
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirMusicReggae\n"):
            self.Sound.StopMusic()
            self.Sound.PlayMusic("reggae")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirMusicaBordel\n"):
            self.Sound.StopMusic()
            self.Sound.PlayMusic("brothel")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "UmaMaquina\n"):
            self.Sound.PlaySFX("umaMaquina")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        #endregion

        #region Battles 
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaCriminosoAtirador\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Criminoso Atirador"), "KrambeckNight")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("KrambeckArq")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaCriminosoAtiradorNoDeposito\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Criminoso Atirador"), "BurningDeposit")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("KrambeckArq")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaElfoLarapio\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Elfo Larapio"), "KrambeckNight")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("KrambeckArq")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaAcolito\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Elfo Acolito"), "Krambeck2")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("KrambeckArq")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaWraith\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Wraith"), "Krambeck2")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("KrambeckArq")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaImp\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Imp"), "Krambeck2")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("KrambeckArq")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaHidra\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Hydra do Oeste"), "ObeliskKrambeck")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("KrambeckArq")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaRhonAldyn\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Rhon'Aldyn"), "AltarKrambeck")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("KrambeckArq")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        #endregion

        #region Monsters
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirAcolito\n"):
            self.Actors.append(lib.GetMonstro(self.Monstros,"Elfo Acolito"))
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirCriminosoAtirador\n"):
            self.Actors.append(lib.GetMonstro(self.Monstros,"Criminoso Atirador"))
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirRhonAldyn\n"):
            self.Actors.append(lib.GetMonstro(self.Monstros,"Rhon'Aldyn"))
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif  
        #endregion      

        #region Backgrounds
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundKrambeck\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/Krambeck.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundStrategyRoom\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/ElvenCouncilRoomKrambeck.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundKrambeckNight\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/KrambeckNight.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundKrambeckObelisk\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/ObeliskKrambeck.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundQuartoElfico\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/ElvenRoom.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundKrambeck2\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/Krambeck2.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundElfEmcampment\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/ElfEmcampmentDay.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundDepositoQueimando\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/BurningDeposit.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundSantuario\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/AltarKrambeck.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        #endregion

        #region Weapons and status
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirArcoMelhoradoDosElfos\n"):
            self.Personagem.arma = lib.GetArma(self.Armas,"arma2Arqueiro")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirArcoAbençoadoDosElfos\n"):
            self.Personagem.arma = lib.GetArma(self.Armas,"arma3Arqueiro")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        
        if(self.StoryTextList[self.StoryListId]['txt'] == "GameOverEvent\n"):
            self.GameOver = gow.GameOverWindow(self.Screen)
            self.Sound.StopMusic()
            self.GameOver.GameOver()
        #endif
        #endregion
    #endif

    def Update(self):
        self.VerifyFirstTimeInWindowToPlayMusic("KrambeckArq")
        pygame.display.set_caption("KrambeckArqueiro")
        if(self.Count == 0):
            self.StoryTextList = lib.SearchText(self.Filename,self.StoryIndex)
            self.Count+=1
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
        return self.Personagem,'KrambeckArqueiro',False
    #endFunction

#endclass
