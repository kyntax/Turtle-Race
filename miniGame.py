import pygame
import random
from Setup import *

block_size = 20;
FPS = 15

font = pygame.font.SysFont(None, 25)

snake_color = (0, 155, 0)
img_apple = pygame.image.load('image/apple.png')
img_apple = pygame.transform.scale(img_apple,(20,20))
feed_color = (255, 0, 0)
#Hoang Long them
title_surf_GameOver, title_rect_GameOver = textObj("Game Over!", "Yellow", font_size=60)
title_rect_GameOver.center = (screen_width / 2), (screen_height*0.4)
title_surf_subGameOver, title_rect_subGameOver = textObj("Press C To Play Again Or Q To Quit Game!", "white", font_size=30)
title_rect_subGameOver.center = (screen_width / 2), (screen_height*0.5)
def score(score):
    text = font.render("Score: " + str(score), True, pygame.Color("black"))
    screen.blit(text, (20, 20))


def message_death(msg, color, x, y):
    text_died = font.render(msg, True, color)
    screen.blit(text_died, [x, y])


def game_intro():
    screen.fill(pygame.Color(75, 193, 114))
    message_death("WELCOME TO SLITHER", snake_color, 400, 250)
    message_death("You will die if you touch myself or run over game screen", pygame.Color("red"), 200, 290)
    message_death("or you back when you go ahead:", pygame.Color("red"), 280, 310)
    message_death("Get more point by way eat each apple:", pygame.Color("red"), 250, 330)
    message_death("Get more and more apple you can:", pygame.Color("red"), 260, 350)
    message_death("Press BACKSPACE to start game", pygame.Color("red"), 260, 350)

def your_score(score):
    text = font.render("Your Score: " + str(score), True, pygame.Color("black"))
    screen.blit(text, (screen_width / 2 - 80, screen_height / 2 + 50))

def character(characterl):
    for XnY in characterl:
        pygame.draw.rect(screen, snake_color, (XnY[0], XnY[1], block_size, block_size))

def GameLoop():
    gameExit = False #run
    gameOver = False
    gameIntro = True
    characterl = []
    characterlen = 1

    largeApple = 20

    lead_x = screen_width / 2
    lead_y = screen_height / 2
    lead_x2 = 0
    lead_y2 = 0
    apple_Xcor = random.randrange(0, screen_width - 3 * block_size,20)
    apple_Ycor = random.randrange(0, screen_height - 3 * block_size,20)
    while not gameExit:
        #while gameIntro:
         #   pygame.display.update()
          #  for event in pygame.event.get():
           #     if event.type == pygame.QUIT:
            #        gameExit = True
             #       gameIntro = False
              #  if event.type == pygame.KEYDOWN:
               #     if event.key == pygame.K_q: #If press q => Exit Game
                #        gameExit = True
                 #       gameIntro = False
                  #  if event.key == pygame.K_SPACE:
                   #     GameLoop()
        while gameOver == True: #If the snake is dead run this subState
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: #If press q => Exit Game
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        GameLoop()
            screen.fill(pygame.Color(75, 193, 114))
            screen.blit(title_surf_GameOver, title_rect_GameOver)
            screen.blit(title_surf_subGameOver,title_rect_subGameOver)
            your_score(characterlen - 1)

        #While Game is not Over
        screen.fill(pygame.Color(75, 193, 114))
        pygame.draw.rect(screen,pygame.Color("Black"),(40,40,1200,640),2)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    lead_x2 = -block_size
                    lead_y2 = 0

                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    lead_x2 = block_size
                    lead_y2 = 0

                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    lead_y2 = block_size
                    lead_x2 = 0

                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    lead_y2 = -block_size
                    lead_x2 = 0
        if lead_x >= screen_width-40 or lead_x < 40 or lead_y >= screen_height-40 or lead_y < 40:
            gameOver = True
        lead_x += lead_x2
        lead_y += lead_y2

        screen.blit(img_apple, (apple_Xcor, apple_Ycor))

        Head = []
        Head.append(lead_x)
        Head.append(lead_y)
        characterl.append(Head)

        if len(characterl) > characterlen:
            del characterl[0]
        for eachSegment in characterl[:-1]:
            if eachSegment == Head:
                gameOver = True

        character(characterl)

        score(characterlen - 1)

        pygame.display.update()

        if (apple_Xcor == lead_x and apple_Ycor == lead_y):
            apple_Xcor = random.randrange(40, screen_width - largeApple-40,20)
            apple_Ycor = random.randrange(40, screen_height - largeApple-40,20)
            characterlen += 1
        fpsClock.tick(FPS)

    return characterlen -1

    pygame.quit()
    quit()


game_intro()
GameLoop()

