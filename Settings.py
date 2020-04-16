from Setup import *
import Setup
import runTurtle

# set up the window
title_surf_Settings, title_rect_Settings = textObj("SETTINGS", "Yellow",font_size=80)
title_rect_Settings.center = (screen_width/2), (screen_height*0.2)

title_surf_Volume, title_rect_Volume = textObj("Volume", "Yellow",font_size=40)
title_rect_Volume.center = (screen_width/2), (screen_height*0.4)

btn_Back = Button(surface=screen, rect=(screen_width/15, screen_height*0.83, 125, 35), caption='Back',
             borderColor=pygame.Color("Black"))

#Set up Slider

SLIDER_LENGTH = 500

CURSOR = runTurtle.Object('image/Circle Cursor.png', int((screen_width - SLIDER_LENGTH) / 2) + SLIDER_LENGTH, int(screen_height/2) - 10)
CURSOR.shape = pygame.transform.scale(CURSOR.shape, (25, 25))
CURSOR.setCoordinates(int((screen_width - SLIDER_LENGTH) / 2) + SLIDER_LENGTH, int(screen_height/2) - 10)

def settings(event):
    screen.blit(title_surf_Settings,title_rect_Settings)
    screen.blit(title_surf_Volume, title_rect_Volume)
    btn_Back.draw()
    SLIDER = pygame.draw.rect(screen, pygame.Color("grey"),
                              ((screen_width - SLIDER_LENGTH) / 2, screen_height / 2, SLIDER_LENGTH, 5))

    CURSOR_X = CURSOR.getCoordinates()[0]
    CURSOR_Y = CURSOR.getCoordinates()[1]

    click = pygame.mouse.get_pressed()
    if click[0] != 0:
        mouse_pos = pygame.mouse.get_pos()
        if abs(mouse_pos[1] - screen_height / 2) <30:
            if mouse_pos[0] < (screen_width - SLIDER_LENGTH) / 2:
                CURSOR_X = int((screen_width - SLIDER_LENGTH) / 2)

            elif mouse_pos[0] > (screen_width - SLIDER_LENGTH) / 2 + SLIDER_LENGTH:
                CURSOR_X = int((screen_width - SLIDER_LENGTH) / 2) + SLIDER_LENGTH

            else:
                CURSOR_X = mouse_pos[0]
        pygame.mixer.music.set_volume((mouse_pos[0] - (screen_width - SLIDER_LENGTH) / 2) / SLIDER_LENGTH)


    CURSOR.setCoordinates(CURSOR_X, CURSOR_Y)

    screen.blit(CURSOR.shape, CURSOR.getCoordinates())
    btn_Back.set_state(event)
    if btn_Back.is_clicked():
        Setup.state = 2

