import json

def GetImagePath():
    f = open("Config/config.json")
    data = json.load(f)
    f.close()
    return data['ImagePath']
#endfunc

def GetFrameRate():
    f = open("Config/config.json")
    data = json.load(f)
    f.close()
    return data['frameRate']
#endfunc

def GetFont():
    f = open("Config/TextConfig.json")
    data = json.load(f)
    f.close()
    return data['SpeakerFont']
#endfunc

def GetTextSize():
    f = open("Config/TextConfig.json")
    data = json.load(f)
    f.close()
    return data['TextSize']
#endfunc

def GetSpeakerTextPosition():
    f = open("Config/TextConfig.json")
    data = json.load(f)
    f.close()
    x = data['Speaker_x']
    y = data['Speaker_y']
    return (x,y)
#endfunc

def GetSpeakerTextColor():
    f = open("Config/TextConfig.json")
    data = json.load(f)
    f.close()
    finalTuple = tuple(map(int, data['Speaker_textcolor'].split(',')))
    return finalTuple
#endfunc

def GetVerticalSpace():
    f = open("Config/TextConfig.json")
    data = json.load(f)
    f.close()
    return data['TextVerticalSpace']
#endfunc

def GetClassesDisponiveis():
    f = open("Config/ClassesConfig.json")
    data = json.load(f)
    f.close()
    return data['ClassesDisponiveis']
#endfunc

def GetTitleTextSize():
    f = open("Config/TitleConfig.json")
    data = json.load(f)
    f.close()
    return data['TitleTextSize']
#endfunc

def GetTitleTextPosition():
    f = open("Config/TitleConfig.json")
    data = json.load(f)
    f.close()
    x = data['Title_x']
    y = data['Title_y']
    return (x,y)
#endfunc

def GetTitleTextColor():
    f = open("Config/TitleConfig.json")
    data = json.load(f)
    f.close()
    finalTuple = tuple(map(int, data['Title_textcolor'].split(',')))
    return finalTuple
#endfunc

def GetTitleFont():
    f = open("Config/TitleConfig.json")
    data = json.load(f)
    f.close()
    return data['TitleFont']
#endfunc

def GetTitleTextSize():
    f = open("Config/TitleConfig.json")
    data = json.load(f)
    f.close()
    return data['TitleTextSize']
#endfunc

def GetNameTextPosition():
    f = open("Config/TitleConfig.json")
    data = json.load(f)
    f.close()
    pos = data['NomeTextPosition']
    return pos
#endfunc

def GetEditBox():
    f = open("Config/TitleConfig.json")
    data = json.load(f)
    f.close()
    eb = data['EditBoxHeroName']
    return eb
#endfunc

def GetButton(id):
    f = open("Config/TitleConfig.json")
    data = json.load(f)
    f.close()
    btn = data[f'Button{id}']
    return btn
#endfunc

def GetClassePosition():
    f = open("Config/TitleConfig.json")
    data = json.load(f)
    f.close()
    pos = data['ClasseTextPosition']
    return pos
#endfunc
def GetBoundaryThickness():
    f = open("Config/Config.json")
    data = json.load(f)
    f.close()
    return data['BoundaryThickness']
#endfunc

def GetActorPosition(id):
    f = open("Config/CharacterConfig.json")
    data = json.load(f)
    f.close()
    actor = data[f'Actor{id}']
    return actor
#endfunc