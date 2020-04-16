from Login import *
import Setup
from Setup import *
#Declare text
title_surf_Race, title_rect_Race = textObj("Turtle Race", "Red","Calibri", font_size= 80)
title_rect_Race.center = (screen_width/2), (screen_height*0.13)
title_surf_subRace, title_rect_subRace = textObj("The best game ever!", "Black", "Calibri")
title_rect_subRace.center = (screen_width/2+130), (screen_height*0.23)

#Declare Button
# Declare Button

btn_StartGame = Button(surface=screen, rect=(screen_width /2 - 100, screen_height*0.45, 200, 35), caption='Start Game',
             borderColor=pygame.Color("Black"))
btn_Instruction = Button(surface=screen, rect=(screen_width /2 - 150, screen_height*0.53, 300, 35), caption='Instruction',
             borderColor=pygame.Color("Black"))
btn_MiniGame = Button(surface=screen, rect=(screen_width /2 - 150, screen_height*0.61, 300, 35), caption='Minigame',
             borderColor=pygame.Color("Black"))
btn_Settings = Button(surface=screen, rect=(screen_width /2 - 150, screen_height*0.69, 300, 35), caption='Settings',
             borderColor=pygame.Color("Black"))
btn_About = Button(surface=screen, rect=(screen_width/2- 150, screen_height*0.77, 300, 35), caption='About',
             borderColor=pygame.Color("Black"))
btn_Logout = Button(surface=screen, rect=(screen_width/2 - 150, screen_height*0.85, 300, 35), caption='Log Out',
             borderColor=pygame.Color("Black"))


def mainMenu(event,events): #state = 2
    screen.fill(pygame.Color(75, 193, 114))
    title_surf_Money, title_rect_Money = textObj("Money: " + str(Setup.userMoney), "Red", "Calibri", font_size=35)
    title_rect_Money.center = (screen_width / 2), (screen_height * 0.35)
    # Display Text Title
    screen.blit(title_surf_Race, title_rect_Race)
    screen.blit(title_surf_subRace, title_rect_subRace)
    screen.blit(title_surf_Money, title_rect_Money)
    #Display Button
    btn_StartGame.draw()
    btn_StartGame.set_state(event)
    btn_Instruction.draw()
    btn_Instruction.set_state(event)
    btn_MiniGame.draw()
    btn_MiniGame.set_state(event)
    btn_Settings.draw()
    btn_Settings.set_state(event)
    btn_About.draw()
    btn_About.set_state(event)
    btn_Logout.draw()
    btn_Logout.set_state(event)
    img = pygame.transform.scale(pygame.image.load('image/TurtlePic.png'), (120, 120))
    screen.blit(img, (850, 40))
    #Button work

    if btn_Logout.is_clicked():
        Setup.state = 0
    if btn_StartGame.is_clicked():
        Setup.state = 3
    if btn_Instruction.is_clicked():
        Setup.state = 6
    if btn_Settings.is_clicked():
        Setup.state = 9
    if btn_About.is_clicked():
        Setup.state = 10
        checkBet(200)
def checkBet(betMoney):
    oldfiledata = []
    line_index = -1
    accoutnline_index = -1
    with open('userdata.txt', 'r+') as fread:
        for line in fread:
            if line.strip():
                line_index +=1
                line = line.rstrip()
                values = line.split()
                if (Setup.username == values[0] and Setup.password == values[1]):
                    accoutnline_index = line_index
                    Setup.userMoney =  betMoney +int(Setup.userMoney)
                oldfiledata.append(line)
                line = line +'\n'
        oldfiledata[accoutnline_index] = Setup.username + '\t' + Setup.password + '\t' + str(Setup.userMoney)
    with open('userdata.txt', 'w') as fwrite:
        for i in range (len(oldfiledata)):
            fwrite.write(oldfiledata[i])
            fwrite.write('\n')


