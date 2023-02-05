import pygame
import Utils.JsonLoader as jsonL
def InsertBackground(background, screen, alpha = 255):
    background = pygame.transform.scale(background, (screen.get_width(), screen.get_height()))
    background.set_alpha(alpha)
    screen.blit(background, (0,0))
#endFunction

def InsertImage(img, width, height, x,y, screen, alpha = 255):
    img = pygame.transform.scale(img, (width, height))
    img.set_alpha(alpha)
    screen.blit(img, (x,y))
#endFunction

def InsertText(text, text_color, x, y, screen, fontName = None, textSize = None):
    if(fontName == None):
        fontName = jsonL.GetFont()
    #endif
    if(textSize == None):
        textSize = jsonL.GetTextSize()
    #endif
    font = pygame.font.Font(fontName, textSize)
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))
#endfunction

def TransformCenterCoordIntoBorder(img, x,y):
    x = x - img.Width/2
    y = y - img.Height/2
    return (x,y)
#endfunc

def TransformCenterCoordIntoBorder(img, x,y):
    x = x - img.Width/2
    y = y - img.Height/2
    return (x,y)
#endfunc

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
    if index != -1:
        return text[:index], text[index+1:]
    else:
        return '',''
    #endif
#endfunc