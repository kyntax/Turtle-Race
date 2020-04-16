from Setup import *
import Setup
Amulet_List_icon = [pygame.image.load('image/speedup_amulet.png'), pygame.image.load('image/speeddown_amulet.png'),
                    pygame.image.load('image/stop.png'), pygame.image.load('image/bomb_amulet.png'),
                    pygame.image.load('image/turnback.png'), pygame.image.load('image/shield_amulet.png')]
heading_surf_Instruction, heading_rect_Instruction = textObj("Instruction", "Yellow",font_size=80)
heading_rect_Instruction.center = (screen_width/2), (screen_height*0.16)

btn_Back = Button(surface=screen, rect=(screen_width/15, screen_height*0.83, 125, 35), caption='Back',
             borderColor=pygame.Color("Black"))

def show_icon():
    gap = 70
    amulet0 = pygame.transform.scale(Amulet_List_icon[0], (50, 50))
    amulet1 = pygame.transform.scale(Amulet_List_icon[1], (50, 50))
    amulet2 = pygame.transform.scale(Amulet_List_icon[2], (50, 50))
    amulet3 = pygame.transform.scale(Amulet_List_icon[3], (50, 50))
    amulet4 = pygame.transform.scale(Amulet_List_icon[4], (50, 50))
    amulet5 = pygame.transform.scale(Amulet_List_icon[5], (50, 50))

    #screen.blit(amulet0, (screen_width*0.2, screen_height*0.35))
    #screen.blit(amulet1, (screen_width*0.2, screen_height*0.35+ gap))
    #screen.blit(amulet2, (screen_width*0.42, screen_height*0.35))
    #screen.blit(amulet3, (screen_width*0.42, screen_height*0.35+ gap))
    #screen.blit(amulet4, (screen_width*0.66, screen_height*0.35))
    #screen.blit(amulet5, (screen_width*0.66, screen_height*0.35+ gap))

    amulet0 = Image(amulet0, screen_width * 0.2 + 25, screen_height * 0.39)
    amulet1 = Image(amulet1, screen_width * 0.2 + 25, screen_height * 0.39+gap)
    amulet2 = Image(amulet2, screen_width * 0.42 + 25, screen_height * 0.39)
    amulet3 = Image(amulet3, screen_width * 0.42 + 25, screen_height * 0.39+gap)
    amulet4 = Image(amulet4, screen_width * 0.66 + 25, screen_height * 0.39)
    amulet5 = Image(amulet5, screen_width * 0.66 + 25, screen_height * 0.39+gap)
    amulet0.display()
    amulet1.display()
    amulet2.display()
    amulet3.display()
    amulet4.display()
    amulet5.display()
    text_surf_node0, text_rect_node0 = textObj("Speed up character in a period of time", "Yellow",font_size=20)
    text_surf_node1, text_rect_node1 = textObj("Slow down character in a period of time", "Yellow", font_size=20)
    text_surf_node2, text_rect_node2 = textObj("Stop character in a period of time", "Yellow", font_size=20)
    text_surf_node3, text_rect_node3 = textObj("Brings character back to the starting point", "Yellow", font_size=20)
    text_surf_node4, text_rect_node4 = textObj("Turn character back in a period of time", "Yellow", font_size=20)
    text_surf_node5, text_rect_node5 = textObj("Protect character against the next disadvantage amulet", "Yellow", font_size=20)

    if amulet0.mouseEnter():
        pygame.draw.rect(screen,(48, 53, 46),(amulet0._x+30,amulet0._y-50,400,40))
        screen.blit(text_surf_node0,(amulet0._x+35,amulet0._y-45))
    if amulet1.mouseEnter():
        pygame.draw.rect(screen,(48, 53, 46),(amulet1._x+30,amulet1._y-50,410,40))
        screen.blit(text_surf_node1,(amulet1._x+35,amulet1._y-45))
    if amulet2.mouseEnter():
        pygame.draw.rect(screen,(48, 53, 46),(amulet2._x+30,amulet2._y-50,360,40))
        screen.blit(text_surf_node2,(amulet2._x+35,amulet2._y-45))
    if amulet3.mouseEnter():
        pygame.draw.rect(screen,(48, 53, 46),(amulet3._x+30,amulet3._y-50,445,40))
        screen.blit(text_surf_node3,(amulet3._x+35,amulet3._y-45))
    if amulet4.mouseEnter():
        pygame.draw.rect(screen,(48, 53, 46),(amulet4._x-435,amulet4._y-50,410,40))
        screen.blit(text_surf_node4,(amulet4._x-430,amulet4._y-45))
    if amulet5.mouseEnter():
        pygame.draw.rect(screen,(48, 53, 46),(amulet5._x-590,amulet5._y-50,565,40))
        screen.blit(text_surf_node5,(amulet5._x-580,amulet5._y-45))
def show_icon_text():
    gap_height=70
    gap_width = 255
    ratio_height = 0.38
    ratio_width = 0.31
    text_surf_ic1, text_rect_ic1 = textObj("Speed Up", "Yellow", font_size=30)
    text_surf_ic2, text_rect_ic2 = textObj("Slow Down", "Yellow", font_size=30)
    text_surf_ic3, text_rect_ic3 = textObj("Stop", "Yellow", font_size=30)
    text_surf_ic4, text_rect_ic4 = textObj("Destroy", "Yellow", font_size=30)
    text_surf_ic5, text_rect_ic5 = textObj("Turn Back", "Yellow", font_size=30)
    text_surf_ic6, text_rect_ic6 = textObj("Defence", "Yellow", font_size=30)

    text_rect_ic1.center = (screen_width*ratio_width), (screen_height*ratio_height)
    text_rect_ic2.center = (screen_width*ratio_width+10), (screen_height*ratio_height+ gap_height)
    text_rect_ic3.center = (screen_width*ratio_width+250), (screen_height*ratio_height)
    text_rect_ic4.center = (screen_width*ratio_width+270), (screen_height*ratio_height+ gap_height)
    text_rect_ic5.center = (screen_width*ratio_width+595), (screen_height*ratio_height)
    text_rect_ic6.center = (screen_width*ratio_width+585), (screen_height *ratio_height+ gap_height)

    screen.blit(text_surf_ic1,text_rect_ic1)
    screen.blit(text_surf_ic2, text_rect_ic2)
    screen.blit(text_surf_ic3, text_rect_ic3)
    screen.blit(text_surf_ic4, text_rect_ic4)
    screen.blit(text_surf_ic5, text_rect_ic5)
    screen.blit(text_surf_ic6, text_rect_ic6)
def show_luckybtn_guide():
    text_surf_guide1,text_rect_guide1 = textObj("Give your character an advantage amulet or give an another", "Yellow", font_size=30)
    text_surf_guide2, text_rect_guide2 = textObj("opponent a disavantage amulet.", "Yellow", font_size=30)
    text_rect_guide2.center = (screen_width /2), (screen_height * 0.68)
    text_surf_guide3, text_rect_guide3 = textObj("But you have to pay an amount of money to use this button.", "Yellow", font_size=30)
    screen.blit(text_surf_guide1, ((screen_width * 0.17), (screen_height * 0.6)))
    screen.blit(text_surf_guide2, text_rect_guide2)
    screen.blit(text_surf_guide3, ((screen_width * 0.17), (screen_height * 0.7)))

def show_title():
    title_surf_amulet, title_rect_amulet = textObj("------------------Amulet function------------------", "White", font_size=30)
    title_rect_amulet.center = (screen_width/2), (screen_height * 0.3)

    title_surf_luckybtn, title_rect_luckybtn = textObj("-------------------Lucky Button-------------------", "White", font_size=30)
    title_rect_luckybtn.center = (screen_width/2), (screen_height * 0.5+40)

    screen.blit(title_surf_amulet, title_rect_amulet)
    screen.blit(title_surf_luckybtn, title_rect_luckybtn)

def introduction(event):
    screen.blit(heading_surf_Instruction, heading_rect_Instruction)
    show_title()
    show_icon_text()
    show_icon()

    show_luckybtn_guide()
    btn_Back.draw()
    btn_Back.set_state(event)
    if btn_Back.is_clicked():
        Setup.state = 2

