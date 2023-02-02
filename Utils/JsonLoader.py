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