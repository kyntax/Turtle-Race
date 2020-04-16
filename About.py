from Setup import *
import Setup  #Declare to get Setup.state

title_surf_About, title_rect_About = textObj("ABOUT", "Yellow",font_size=80)
title_rect_About.center = (screen_width/2), (screen_height*0.2)
#Delare Button
btn_Back = Button(surface=screen, rect=(screen_width/15, screen_height*0.83, 125, 35), caption='Back',
             borderColor=pygame.Color("Black"))
def About(event,events):
    screen.fill(pygame.Color(75, 193, 114))
    screen.blit(title_surf_About,title_rect_About)
    about_line1 = "This is an offline game for single player"
    about_line2 = "This game is written with Pygame in Python IDLE"
    about_line3 = "Developer: Nguyễn Hoàng Long, Trần Thành Long"
    about_line4 = "                                                   Nguyễn Văn Minh, Nguyễn Văn Lâm, Hoàng Trung Nam"
    about_line5 = "Designer: Nguyễn Hoàng Long, Hoàng Trung Nam"
    about_line6 = "RewindTeamHCMUS©2019"
    about_line1_surf, about_line1_rect = textObj(about_line1, "White", "Calibri")
    about_line2_surf, about_line2_rect = textObj(about_line2, "White", "Calibri")
    about_line3_surf, about_line3_rect = textObj(about_line3, "White", "Calibri")
    about_line4_surf, about_line4_rect = textObj(about_line4, "White", "Calibri")
    about_line5_surf, about_line5_rect = textObj(about_line5, "White", "Calibri")
    about_line6_surf, about_line6_rect = textObj(about_line6, "White", "Calibri")

    about_line1_rect.center = (screen_width / 2), (screen_height * 0.35)
    about_line2_rect.center = (screen_width / 2), (screen_height * 0.4)
    about_line3_rect.center = (screen_width / 2), (screen_height * 0.45)
    about_line4_rect.center = (screen_width / 2), (screen_height * 0.5)
    about_line5_rect.center = (screen_width / 2), (screen_height * 0.55)
    about_line6_rect.center = (screen_width / 2), (screen_height * 0.65)

    screen.blit(about_line1_surf, about_line1_rect)
    screen.blit(about_line2_surf, about_line2_rect)
    screen.blit(about_line3_surf, about_line3_rect)
    screen.blit(about_line4_surf, about_line4_rect)
    screen.blit(about_line5_surf, about_line5_rect)
    screen.blit(about_line6_surf, about_line6_rect)

    btn_Back.draw()
    btn_Back.set_state(event)
    if btn_Back.is_clicked():
        Setup.state = 2