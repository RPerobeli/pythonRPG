import pygame
import sys
#import Interface.Utils as ut
import Utils.JsonLoader as jsonL
import Interface.BattleWindow as bw
import Interface.GameOverWindow as gow
import Interacoes as lib
import Interface.States.GameState as GameState

class SagaFinal(GameState.GameState):
    def __init__(self, screen, dialogBox, personagem, monstros, npcs = None, armas= None):
        super().__init__(screen)
        self.ImagePath =  jsonL.GetImagePath()
        self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/SnowyCityNight.jpg').convert_alpha()
        self.DialogBox = dialogBox
        self.Personagem = personagem
        self.Monstros = monstros
        self.Actors = [None]*3
        self.Actors[0] = personagem
        self.Npcs = npcs
        self.Alpha = 255
        self.Scene = 1
        self.Filename = "SagaFinal"
        self.MaxStoryIndex = 1
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

    def SelectFinal(self):
        self.Sound.StopMusic()
        lista = [self.Personagem.Good,self.Personagem.Neutral, self.Personagem.Evil]
        final_id = lista.index(max(lista))
        if(final_id==0):
            return "Good"
        if(final_id==1):
            return "Neutral"
        if(final_id==2):
            return "evil"    

        return 
    #endfunc
    
    def VerifyEvent(self):
        print('verificou possiveis eventos')
        
        #region status
        if(self.StoryTextList[self.StoryListId]['txt'] == "RemoverAtor1\n"):
            self.Actors[1] = None
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "RemoverAtor0\n"):
            self.Actors[0] = None
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirPersonagem\n"):
            self.Actors[0] = self.Personagem
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "SelecionarFinal\n"):
            self.NextStory = self.SelectFinal()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        #endregion

        #region NPCs
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirAldeaoFinal1\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Aldeao Final 1")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirJessie\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Jessie")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirValquiriaLuz\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Rainha Valquiria")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirElfoNegro\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Elfo Negro")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirDeusa\n"):
            self.Actors[1] = lib.GetNpc(self.Npcs,"Anjo")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        
        #endregion
        
        #region Sound
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirSoundShot\n"):
            self.Sound.StopMusic()
            self.Sound.PlaySFX("Tiro")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirMusicaBatalhaFinal\n"):
            self.Sound.StopMusic()
            self.Sound.PlayMusic("BatalhasFinais")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirSoundDeusa\n"):
            self.Sound.StopMusic()
            self.Sound.PlayMusic("Deusa")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        #endregion

        #region Battles 
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaEspiritoMaldito\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Espirito Maligno"), "SnowyCityNight")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("SagaFinal")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaDavion\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Davion Stormfury"), "guild")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("SagaFinal")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaValquiria\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Rainha Valquiria"), "Brasilia")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("BatalhasFinais")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaSenhordosLobisomens\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Senhor dos Lobos"), "BrasiliaGardens")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("BatalhasFinais")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaDemonioSuperior\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Demonio Superior"), "BrasiliaDemonRoom")
            self.Personagem = battleWindow.Battle()
            self.Sound.PlayMusic("BatalhasFinais")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaLich1\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Metherax"), "BrasiliaThrone")
            self.Personagem = battleWindow.Battle(isLichFirstBattle=True, danoBase=30)
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "BatalhaLich2\n"):
            self.Sound.StopMusic()
            battleWindow = bw.BattleWindow(self.Screen,self.DialogBox, self.Personagem,lib.GetMonstro(self.Monstros,"Metherax"), "BrasiliaThrone")
            self.Personagem = battleWindow.Battle(danoBase=2)
            self.Sound.PlayMusic("BatalhasFinais")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif

        #endregion

        #region Monsters
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirEspiritoMaldito\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Espirito Maligno")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirMetherax\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Metherax")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif 
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirDavion\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Davion Stormfury")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif 
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirValquiria\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Rainha Valquiria")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif 
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirSenhorDosLobisomens\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Senhor dos Lobos")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif 
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirDemonioSuperior\n"):
            self.Actors[1] = lib.GetMonstro(self.Monstros,"Demonio Superior")
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif  
        #endregion      

        #region Backgrounds
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundSnowyKrambeck\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/SnowyKrambeck.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundGuild\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/guild.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundBrasilia\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/Brasilia.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundBrasiliaGardens\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/BrasiliaGardens.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundBrasiliaDemonRoom\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/BrasiliaDemonRoom.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundBrasiliaThrone\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/BrasiliaThrone.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        if(self.StoryTextList[self.StoryListId]['txt'] == "InserirBackgroundTelaPreta\n"):
            self.BackgroundImage = pygame.image.load(f'{self.ImagePath}/Background/TelaPreta.jpg').convert_alpha()
            self.StoryListId += 1
            self.VerifyEvent()
            return
        #endif
        #endregion

        #region Weapons        
        if(self.StoryTextList[self.StoryListId]['txt'] == "GameOverEvent\n"):
            self.GameOver = gow.GameOverWindow(self.Screen)
            self.Sound.StopMusic()
            self.GameOver.GameOver()
        #endif
        #endregion
    #endif

    def Update(self, nomeState):
        pygame.display.set_caption(nomeState)
        self.VerifyFirstTimeInWindowToPlayMusic(nomeState)
        if(self.Count == 0):
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
                    if(self.isQuestion and self.StoryIndex < self.MaxStoryIndex):
                        self.Sound.PlaySFX("cursorError")
                        print(self.MaxStoryIndex)
                        print("Ta com pressa irmao? para de pular os dialogos.")
                    else:
                        self.Sound.PlaySFX("cursorForward")
                        self.isQuestion = True
                        self.StoryIndex += 1 
                        if(self.StoryIndex > self.MaxStoryIndex):
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
        return self.Personagem,nomeState, False
    #endFunction
#endclass
