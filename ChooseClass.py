from Setup import *
import Setup

avatar = [pygame.image.load('image/ava/Cat.png'), pygame.image.load('image/ava/Chicken.png'), pygame.image.load('image/ava/Dog.png'),
          pygame.image.load('image/ava/Fox.png'), pygame.image.load('image/ava/Pig.png'), pygame.image.load('image/ava/person.png')]
pickColor = [pygame.image.load('image/color/blue.png'),pygame.image.load('image/color/green.png'),pygame.image.load('image/color/dark.png'),
             pygame.image.load('image/color/red.png'),pygame.image.load('image/color/yellow.png')]
pickColorUpdate =[pygame.image.load('image/color/blue-onclick.png'),pygame.image.load('image/color/green-onclick.png'),
                  pygame.image.load('image/color/dark-onclick.png'),pygame.image.load('image/color/red-onclick.png'),
                  pygame.image.load('image/color/yellow-onclick.png')]


#Declare title
title_surf_Race, title_rect_Race = textObj("CHOOSE CLASS", "yellow","Calibri", font_size= 80)
title_rect_Race.center = (screen_width/2), (screen_height*0.15)

#Declare Avatar
ava1 = Image(avatar[0], screen_width*0.23,screen_height*0.3)
ava2 = Image(avatar[1], screen_width*0.33,screen_height*0.3)
ava3 = Image(avatar[2], screen_width*0.43,screen_height*0.3)
ava4 = Image(avatar[3], screen_width*0.53,screen_height*0.3)
ava5 = Image(avatar[4], screen_width*0.63,screen_height*0.3)
ava6 = Image(avatar[5], screen_width*0.73,screen_height*0.3)


#Delare Button
btn_Back = Button(surface=screen, rect=(screen_width/15, screen_height*0.83, 125, 35), caption='Back',
             borderColor=pygame.Color("Black"))
btn_Next = Button(surface=screen, rect=(screen_width*0.82, screen_height*0.83, 125, 35), caption='Next',
             borderColor=pygame.Color("Black"))
#Declare colorBox
yellowBox = Image(pickColor[4], screen_width*0.38,screen_height*0.45)
redBox = Image(pickColor[3], screen_width*0.43,screen_height*0.45)
darkBox = Image(pickColor[2], screen_width*0.48,screen_height*0.45)
greenBox = Image(pickColor[1], screen_width*0.53,screen_height*0.45)
blueBox = Image(pickColor[0], screen_width*0.58,screen_height*0.45)


def displayAvatar():
    ava1.display()
    ava2.display()
    ava3.display()
    ava4.display()
    ava5.display()
    ava6.display()
def displayColor():
    redBox.display()
    blueBox.display()
    greenBox.display()
    yellowBox.display()
    darkBox.display()
def checkAvatar(event):
    # Choose Avatar
    if (ava1.onclick(event)):
        Setup.user_character = 0
    if (ava2.onclick(event)):
        Setup.user_character = 1
    if (ava3.onclick(event)):
        Setup.user_character = 2
    if (ava4.onclick(event)):
        Setup.user_character = 3
    if (ava5.onclick(event)):
        Setup.user_character = 4
    if (ava6.onclick(event)):
        Setup.user_character = 5
def checkColor(event):
    # Choose Color
    if (blueBox.onclick(event)):
        Setup.user_characterIndex = 0
        blueBox.update(pickColorUpdate[0])
        greenBox.update(pickColor[1])
        darkBox.update(pickColor[2])
        redBox.update(pickColor[3])
        yellowBox.update(pickColor[4])
    if (greenBox.onclick(event)):
        Setup.user_characterIndex = 1
        greenBox.update(pickColorUpdate[1])
        redBox.update(pickColor[3])
        blueBox.update(pickColor[0])
        yellowBox.update(pickColor[4])
        darkBox.update(pickColor[2])
    if (darkBox.onclick(event)):
        Setup.user_characterIndex = 2
        darkBox.update(pickColorUpdate[2])
        redBox.update(pickColor[3])
        blueBox.update(pickColor[0])
        greenBox.update(pickColor[1])
        yellowBox.update(pickColor[4])
    if(redBox.onclick(event)):
        Setup.user_characterIndex = 3
        redBox.update(pickColorUpdate[3])
        blueBox.update(pickColor[0])
        greenBox.update(pickColor[1])
        yellowBox.update(pickColor[4])
        darkBox.update(pickColor[2])
    if (yellowBox.onclick(event)):
        Setup.user_characterIndex = 4
        yellowBox.update(pickColorUpdate[4])
        redBox.update(pickColor[3])
        blueBox.update(pickColor[0])
        greenBox.update(pickColor[1])
        darkBox.update(pickColor[2])

def drawBtn(event):
    # Display Button
    btn_Back.draw()
    btn_Back.set_state(event)
    btn_Next.draw()
    btn_Next.set_state(event)

    if btn_Back.is_clicked():
        Setup.state = 2
    if btn_Next.is_clicked():
        Setup.state = 4

def chooseClass(event,events): #STATE = 3
    screen.fill(pygame.Color(75, 193, 114))

    # Display Text Title
    screen.blit(title_surf_Race, title_rect_Race)

    #Display avatar - color
    displayAvatar()
    displayColor()

    #Choose avate - color
    checkAvatar(event)
    checkColor(event)

    #DrawButton
    drawBtn(event)
