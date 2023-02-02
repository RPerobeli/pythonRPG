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
    f = open("Config/config.json")
    data = json.load(f)
    f.close()
    return data['Font']
#endfunc

def GetTextSize():
    f = open("Config/config.json")
    data = json.load(f)
    f.close()
    return data['TextSize']
#endfunc

def GetSpeakerTextPosition():
    f = open("Config/config.json")
    data = json.load(f)
    f.close()
    x = data['Speaker_x']
    y = data['Speaker_y']
    return (x,y)
#endfunc

def GetSpeakerTextColor():
    f = open("Config/config.json")
    data = json.load(f)
    f.close()
    finalTuple = tuple(map(int, data['Speaker_textcolor'].split(',')))
    return finalTuple
#endfunc

def GetVerticalSpace():
    f = open("Config/config.json")
    data = json.load(f)
    f.close()
    return data['TextVerticalSpace']
#endfunc