from Setup import *
import Setup
#Declare Label username and password
LABEL_FONT = pygame.font.SysFont("comicsansms", 20, True)
username_labelSurf = LABEL_FONT.render("Username:",1,pygame.Color("white"))
password_labelSurf = LABEL_FONT.render("Password:",1,pygame.Color("white"))

# Declare textbox_username
textbox_username = Textbox(font_size=30,text_color=(255,255,255))
rect_username = pygame.Rect(screen_width/2, screen_height/3.5, 200, 30)
textbox_username.set_rect(rect_username)

# Declare textbox_password
textbox_password = Textbox(font_size=30)
rect_password = pygame.Rect(screen_width/2, screen_height/3.5+40, 200, 30)
textbox_password.set_rect(rect_password)

#Declare Header
title_surf_Login, title_rect_Login = textObj("Welcome to Turtle Race","Black", font_size=60)
title_rect_Login.center = (screen_width/2), (screen_height*0.12)
#Declare Button
btn_Login = Button(surface=screen, rect=(screen_width / 2 - 50, screen_height*0.4, 100, 35), caption='Login',
             borderColor=pygame.Color("Black"))
img = pygame.transform.scale(pygame.image.load('image/bgmain.jpg'), (1280, 720))

def checkLogin():
    userdata = 'userdata.txt'
    dem =-1
    with open(userdata, 'r') as fread:
        for line in fread:
            if line.strip():
                line = line.rstrip()
                values = line.split()
                if (Setup.username == values[0] and Setup.password == values[1]):
                    Setup.userMoney = values[2]
                    dem +=1
                    return True
                else:
                    line = line +'\n'
        if dem ==-1:
            return False

def Login(event,events): #STATE = 0
    global bool
    screen.blit(img, (0, 0))
    # Display Text Title
    screen.blit(title_surf_Login, title_rect_Login)

    #Draw rect surf with low opacity
    box_surface_rect = pygame.Surface((500, 200), pygame.SRCALPHA)
    pygame.draw.rect(box_surface_rect, (0,0,0, 100), (0, 0, 500, 200))
    screen.blit(box_surface_rect, (screen_width/3, screen_height/3.5-50))

    # Display username_textbox
    pygame.draw.rect(screen, pygame.Color("white"), textbox_username.get_rect(), 2)
    screen.blit(textbox_username.get_surface(), (screen_width/2+5, screen_height/3.5+5))
    # Display username_textbox_label
    screen.blit(username_labelSurf, (screen_width/2-110, screen_height/3.5-3))


    # Display password_textbox
    pygame.draw.rect(screen, pygame.Color("white"), textbox_password.get_rect(), 2)
    passLength = len(textbox_password.get_text())
    passSurf = DEFAULT_FONT.render("*" * passLength, 1, pygame.Color("white"))
    screen.blit(passSurf, (screen_width/2+5, screen_height/3.5+50))
    # Display password_textbox_label
    screen.blit(password_labelSurf, (screen_width/2-107, screen_height/3.5+37))

    #Check click  Mouse_collision textbox
    if textbox_username.is_clicked():
        bool = 1
    elif textbox_password.is_clicked():
        bool = 0
    if bool == 1:
        textbox_username.update(events)
    else:
        textbox_password.update(events)


    # Display button
    btn_Login.draw()
    btn_Login.set_state(event)

    # Khi nhấn nút sẽ xảy ra cái gì ở đây???
    if btn_Login.is_clicked():
       Setup.username = textbox_username.get_text()
       Setup.password = textbox_password.get_text()

       if checkLogin():
           print("Valid", "LOGIN SUCCESSFUL ")
           print(Setup.userMoney)
           Setup.state = 2
           textbox_username.clear_text()
           textbox_password.clear_text()
       else:
           print("Invalid", "Failed to login! Try again")