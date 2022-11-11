from pygame import font

#Text Display Function
def text(text, x=0, y=0, size=20, color=(255,255,255), center=False):
    text_font = font.Font(None, size)
    text = text_font.render(text, 1, color)
    textrect = text.get_rect()
    textpos = (x,y)
    if center:
        textrect.center = textpos
        return text, textrect 
    else:
        textrect.topleft = textpos
        return text, textpos

#Text List Function
def text_list(text_list, x=0, y=0, size=20, color=(255,255,255), center=False):
    return [text(text_in_list, x, y + (round((4 * (size / 5)) * (text_list.index(text_in_list)))), size, color, center) for text_in_list in text_list]
        