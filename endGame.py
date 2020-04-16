import runTurtle
from Setup import *
import Setup

bg = pygame.image.load('image/sky.gif')
bg = pygame.transform.scale(bg, (1280, 720))

WINNER_IMAGE = ['image/winner1.gif', 'image/winner2.gif', 'image/winner3.gif', 'image/winner4.gif']
happy_image = ['image/happy/img1.bmp','image/happy/img2.bmp','image/happy/img3.bmp','image/happy/img4.bmp','image/happy/img5.bmp',
                                  'image/happy/img6.bmp','image/happy/img7.bmp']
huhu_image = ['image/hu/huhu1.bmp','image/hu/huhu2.bmp','image/hu/huhu3.bmp','image/hu/huhu4.bmp']
cup = pygame.image.load('image/cup.png')
cup = pygame.transform.scale(cup, (300,300))
#co = pygame.image.load('image/race.jbg')
#co = pygame.transform.scale(co, (200,200))
INDEX = 0

SCALE = [(70, 128), (188, 128), (286, 128), (534, 128)]

HAPPY = runTurtle.Racer(happy_image, 900, 100)
HUHU = runTurtle.Racer(huhu_image, 900, 100)

btn_Back = Button(surface=screen, rect=(screen_width/15, screen_height*0.83, 125, 35), caption='Back',
             borderColor=pygame.Color("Black"))

def redrawGameWindow(ClassIndex, UnitIndex, winner, WINNER):

    screen.blit(bg, (0, 0))  # This will draw our background image at (0,0)

    A_index = winner.getAnimationIndex()
    winner.setShape(winner.shapeList[A_index])
    winner.shape = pygame.transform.scale(winner.shape, (200, 150))
    screen.blit(winner.shape, (400, 300))

    screen.blit(cup,(100,300))

    INDEX = WINNER.getAnimationIndex()
    WINNER.setShape(WINNER.shapeList[INDEX])
    WINNER.shape = pygame.transform.scale(WINNER.shape, SCALE[INDEX])
    screen.blit(WINNER.shape, ((WINNER.getCoordinates()[0]- SCALE[INDEX][0])/2, WINNER.getCoordinates()[1]))
    #Qoobee
    INDEX = HAPPY.getAnimationIndex()
    HAPPY.setShape(HAPPY.shapeList[INDEX])
    HAPPY.shape = pygame.transform.scale(HAPPY.shape, (300, 300))
    screen.blit(HAPPY.shape, HAPPY.getCoordinates())

    pygame.display.update()

def end_WIN(ClassIndex, UnitIndex,event):
    winner = runTurtle.Racer(runTurtle.RacerList[ClassIndex][UnitIndex], 0, 0)
    WINNER = runTurtle.Racer(WINNER_IMAGE, 1300, 100)

    pygame.time.delay(200)  # This will delay the game the given amount of milliseconds. In our casee 0.1 seconds will be the delay
    redrawGameWindow(ClassIndex, UnitIndex, winner, WINNER)
    title_surf_noi, title_rect_noi = textObj("Congratulations !!", "Red", "Calibri", font_size=50)
    title_rect_noi.center = (900, 500)
    screen.blit(title_surf_noi, title_rect_noi)

    btn_Back.draw()
    if btn_Back.is_clicked():
        Setup.state = 2

def end_Lose(ClassIndex, UnitIndex,event):

    winner = runTurtle.Racer(runTurtle.RacerList[ClassIndex][UnitIndex], 0, 0)

    pygame.time.delay(200)  # This will delay the game the given amount of milliseconds. In our casee 0.1 seconds will be the delay
    screen.blit(bg, (0, 0))
    title_surf_END, title_rect_END = textObj("YOU LOSE", "Red", "Calibri", font_size=80)
    title_rect_END.center = (screen_width / 2), (screen_height * 0.13)
    screen.blit(title_surf_END, title_rect_END)
    title_surf_noi, title_rect_noi = textObj("POOR YOU !!", "Red", "Calibri", font_size=50)
    title_rect_noi.center = (900, 500)
    screen.blit(title_surf_noi, title_rect_noi)
    screen.blit(cup, (100, 300))
    A_index = winner.getAnimationIndex()
    winner.setShape(winner.shapeList[A_index])
    winner.shape = pygame.transform.scale(winner.shape, (200, 150))
    screen.blit(winner.shape, (550, 400))

    INDEX = HUHU.getAnimationIndex()
    HUHU.setShape(HUHU.shapeList[INDEX])
    screen.blit(HUHU.shape, HUHU.getCoordinates())

    btn_Back.draw()
    btn_Back.set_state(event)
    if btn_Back.is_clicked():
        Setup.state = 2
