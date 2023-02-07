import Utils.JsonLoader as jsonL
import Interacoes as lib
import Interface.Utils as ut
import pygame

data = jsonL.GetOptionsPosition()
print(data["Options"]["PositionHealthBars"]["x"])