from Setup import *
import Setup
import Login
import mainMenu
import ChooseClass
import runTurtle
import About
import Settings
import Instruction
import endGame
def mainloop():

    # mainloop
    run = True
    while run:
        pygame.display.update()
        screen.fill(pygame.Color(75, 193, 114))
        events = pygame.event.get()
        
        for event in events:
            if event.type == pygame.QUIT:
                run = False

        if Setup.state == 0:
            Login.Login(event,events)
        if Setup.state ==2:
            mainMenu.mainMenu(event,events)
        if Setup.state == 3:
            ChooseClass.chooseClass(event,events)
        if Setup.state == 4:
            Setup.check_mainGame = runTurtle.runGame(Setup.user_character, Setup.user_characterIndex)
            Setup.state = 5
        if Setup.state == 5:
            if Setup.check_mainGame:
                endGame.end_WIN(Setup.user_character, Setup.user_characterIndex,event)
            else:
                endGame.end_Lose(Setup.user_character, Setup.user_characterIndex,event)
        if Setup.state == 6:
            Instruction.introduction(event)
        if Setup.state == 9:
            Settings.settings(event)
        if Setup.state ==10:
            About.About(event,events)
if __name__ == '__main__':
    mainloop()
    pygame.quit()
