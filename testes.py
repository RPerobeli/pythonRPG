import Utils.JsonLoader as jsonL
import Interacoes as lib
import Interface.Utils as ut

def WrapText(text, wrappedText):
    substring1,substring2 = get_substring(text, '\n')
    wrappedText.append(substring1)
    if(substring2 != ''):
        wrappedText = WrapText(substring2,wrappedText)
        return wrappedText
    else:
        return wrappedText
    #endfunc
#endfunc

def get_substring(text, character):
    index = text.find(character)
    if index != '':
        return text[:index], text[index+1:]
    else:
        return '',''
    #endif
#endfunc

StoryTextList = lib.SearchText("Introducao",1)
textDict = StoryTextList[0]
text = []
text = ut.WrapText(textDict['txt'],text)
print(text)