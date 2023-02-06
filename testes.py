import Utils.JsonLoader as jsonL
import Interacoes as lib
import Interface.Utils as ut
import pygame

monsterConfig = jsonL.GetAllMonstersConfig()
print(monsterConfig)
for config in monsterConfig:
    if(config["Nome"] == "Cao Infernal"):
        print(config)