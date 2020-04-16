from Setup import *
from pygame.locals import *
import time
from random import randint

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720

ROAD_WITDH = 100
ROAD_LENGTH = 1000

# set up the window
DISPLAYSURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT), 0, 32)
pygame.display.set_caption('Turtle Race')

TurTleList = [['Photo/turtle/tur1b.png', 'Photo/turtle/tur2b.png', 'Photo/turtle/tur3b.png'],
              ['Photo/turtle/tur1g.png', 'Photo/turtle/tur2g.png', 'Photo/turtle/tur3g.png'],
              ['Photo/turtle/tur1.png', 'Photo/turtle/tur2.png', 'Photo/turtle/tur3.png'],
              ['Photo/turtle/tur1r.png', 'Photo/turtle/tur2r.png', 'Photo/turtle/tur3r.png'],
              ['Photo/turtle/tur1y.png', 'Photo/turtle/tur2y.png', 'Photo/turtle/tur3y.png']]
BirdList = [['Photo/Bird/b1.png', 'Photo/Bird/b2.png', 'Photo/Bird/b3.png'],
              ['Photo/Bird/g1.png', 'Photo/Bird/g2.png', 'Photo/Bird/g3.png'],
              ['Photo/Bird/k1.png', 'Photo/Bird/k2.png', 'Photo/Bird/k3.png'],
              ['Photo/Bird/r1.png', 'Photo/Bird/r2.png', 'Photo/Bird/r3.png'],
              ['Photo/Bird/y1.png', 'Photo/Bird/y2.png', 'Photo/Bird/y3.png']]
HorseList = [['Photo/Horse/b1.png', 'Photo/Horse/b2.png', 'Photo/Horse/b3.png'],
              ['Photo/Horse/g1.png', 'Photo/Horse/g2.png', 'Photo/Horse/g3.png'],
              ['Photo/Horse/k1.png', 'Photo/Horse/k2.png', 'Photo/Horse/k3.png'],
              ['Photo/Horse/r1.png', 'Photo/Horse/r2.png', 'Photo/Horse/r3.png'],
              ['Photo/Horse/y1.png', 'Photo/Horse/y2.png', 'Photo/Horse/y3.png']]
KangarooList = [['Photo/Kangaroo/b1.png', 'Photo/Kangaroo/b2.png', 'Photo/Kangaroo/b3.png'],
              ['Photo/Kangaroo/g1.png', 'Photo/Kangaroo/g2.png', 'Photo/Kangaroo/g3.png'],
              ['Photo/Kangaroo/k1.png', 'Photo/Kangaroo/k2.png', 'Photo/Kangaroo/k3.png'],
              ['Photo/Kangaroo/r1.png', 'Photo/Kangaroo/r2.png', 'Photo/Kangaroo/r3.png'],
              ['Photo/Kangaroo/y1.png', 'Photo/Kangaroo/y2.png', 'Photo/Kangaroo/y3.png']]
FishList = [['Photo/Fish/b1.png', 'Photo/Fish/b2.png', 'Photo/Fish/b3.png'],
              ['Photo/Fish/g1.png', 'Photo/Fish/g2.png', 'Photo/Fish/g3.png'],
              ['Photo/Fish/k1.png', 'Photo/Fish/k2.png', 'Photo/Fish/k3.png'],
              ['Photo/Fish/r1.png', 'Photo/Fish/r2.png', 'Photo/Fish/r3.png'],
              ['Photo/Fish/y1.png', 'Photo/Fish/y2.png', 'Photo/Fish/y3.png']]
HumanList = [['image/HLong.png', 'image/HLong.png', 'image/HLong.png'],
              ['image/Lam.png', 'image/Lam.png', 'image/Lam.png'],
              ['image/Minh.png', 'image/Minh.png', 'image/Minh.png'],
              ['image/Nam.png', 'image/Nam.png', 'image/Nam.png'],
              ['image/TLong.png', 'image/TLong.png', 'image/TLong.png']]

RacerList = []

RacerList.append(TurTleList)
RacerList.append(BirdList)
RacerList.append(HorseList)
RacerList.append(KangarooList)
RacerList.append(FishList)
RacerList.append(HumanList)

rank_ID = 0
RankList = ['image/1.png', 'image/2.png', 'image/3.png', 'image/4.png', 'image/5.png']
AmuletList = []
Racers = []
RoadList = []

class Object:
    def __init__(self, shape, x, y):
        self.setShape(shape)
        self.setCoordinates(x ,y)

    def setShape(self, image):
        self.shape = pygame.image.load(image)
        self.image = image

    def getShape(self):
        return self.shape

    def getImage(self):
        return self.image

    def setCoordinates(self, x, y):
        if x < 0:
            x = 0
        self.Coordinates = (x, y)

    def getCoordinates(self):
        return self.Coordinates

class Racer(Object):
    def __init__(self, shape, x, y):
        self.setSpeed(3, 6)
        Object.__init__(self, shape[0], x, y)
        self.setStunning(False)
        self.setTurnBack(False)
        self.setRank(0)
        self.shapeList = shape
        self.SttList = []
        self.shape_index = 0
        self.step = 1

    def addStatusList(self, shape):
        if self.SttList.__contains__(shape) == False:
            self.SttList.append(shape)

    def removeFromSttList(self, shape):
        if self.SttList.__contains__(shape):
            self.SttList.remove(shape)

    def setSpeed(self, min, max):
        self.Speed = (min, max)

    def getSpeed(self):
        return self.Speed

    def isCollideWith(self, object):
        return abs(self.getCoordinates()[0]-object.getCoordinates()[0]) < 10 and abs(self.getCoordinates()[1] - object.getCoordinates()[1]) < 10

    def setStunning(self, Bool):
        self.stun = Bool

    def isStunning(self):
        return self.stun

    def setTurnBack(self, Bool):
        self.turn_back = Bool

    def isTurnBack(self):
        return self.turn_back

    def flipRacer(self):
        self.shape = pygame.transform.flip(self.shape, True, False)

    def setTime(self):
        self.time = time.time()

    def isProtect(self):
        return self.SttList.__contains__('image/shield_amulet.png')

    def isFinish(self):
        return self.getCoordinates()[0] > 1200

    def setRank(self, rank):
        self.rank = rank

    def getRank(self):
        return self.rank

    def getDistance(self, object):
        return abs(self.getCoordinates()[0] - object.getCoordinates()[0])

    def getAnimationIndex(self):
        if (self.shape_index == len(self.shapeList) -1 and self.step > 0) or (self.shape_index == 0 and self.step < 0):
            self.step = -self.step
        self.shape_index += self.step
        return self.shape_index

    def preMove(self):
        if self.isStunning():
            if (time.time() - self.time) * 1000 >= 2000:
                self.setStunning(False)
                self.removeFromSttList('image/stop.png')
                return True
            else:
                return False
        elif self.isTurnBack():
            if (time.time() - self.time) * 1000 >= 2000:
                self.setTurnBack(False)
                self.removeFromSttList('image/turnback.png')
                self.flipRacer()
                return True
            else:
                return True
        elif self.isFinish():
            if self.getRank() == 0:
                global rank_ID
                rank_ID += 1
                self.setRank(rank_ID)
            return False
        else:
            return True

    def moveRacer(self, step):
        if self.preMove():
            if self.isTurnBack():
                step = -step
            self.setCoordinates(self.getCoordinates()[0] + step, self.getCoordinates()[1])
            self.setShape(self.shapeList[self.getAnimationIndex()])
            if self.isTurnBack():
                self.shape = pygame.transform.flip(self.shape, True, False)
            for amulet in AmuletList:
                if self.getDistance(amulet) < 150 and self.getCoordinates()[1] == amulet.getCoordinates()[1]:
                    self.setSpeed(3, 6)
                    self.removeFromSttList('image/speeddown_amulet.png')
                    self.removeFromSttList('image/speedup_amulet.png')
                if self.isCollideWith(amulet):
                    amulet.handleAmulet(self)
                    AmuletList.remove(amulet)

class Amulet(Object):
    def __init__(self, type, shape, x, y):
        self.type = type
        Object.__init__(self, shape, x, y)
        self.shape = pygame.transform.scale(self.shape, (50, 50))

    def handleAmulet(self, racer):
        if self.type == 'inc':
            self.incSpeed(racer)
            if racer.getSpeed()[0] > 3:
                racer.addStatusList(self.image)
                racer.removeFromSttList('image/speeddown_amulet.png')

        elif self.type == 'dec':
            if racer.isProtect():
                racer.removeFromSttList('image/shield_amulet.png')
            else:
                self.decSpeed(racer)
                if racer.getSpeed()[0] < 3:
                    racer.addStatusList(self.image)
                    racer.removeFromSttList('image/speedup_amulet.png')

        elif self.type == 'stun':
            if racer.isProtect():
                racer.removeFromSttList('image/shield_amulet.png')
            else:
                self.executeStunning(racer)
                racer.addStatusList(self.image)

        elif self.type == 'reRun':
            if racer.isProtect():
                racer.removeFromSttList('image/shield_amulet.png')
            else:
                self.reRun(racer)

        elif self.type == 'turnBack':
            if racer.isProtect():
                racer.removeFromSttList('image/shield_amulet.png')
            else:
                self.turnBack(racer)
                racer.addStatusList(self.image)

        elif self.type == 'protect':
            self.buffShield(racer)


    def incSpeed(self, racer):
        increase_speed = 3
        speed_min = racer.getSpeed()[0] + increase_speed
        speed_max = racer.getSpeed()[1] + increase_speed
        racer.setSpeed(speed_min, speed_max)

    def decSpeed(self, racer):
        decrease_speed = 3
        speed_min = racer.getSpeed()[0] - decrease_speed
        speed_max = racer.getSpeed()[1] - decrease_speed

        if speed_max < 3:
            speed_max = 3

        if speed_min < 1:
            speed_min = 1

        racer.setSpeed(speed_min, speed_max)

    def executeStunning(self, racer):
        racer.setTime()
        racer.setStunning(True)

    def turnBack(self, racer):
        if racer.isTurnBack():
            racer.setTime()
        else:
            racer.setTime()
            racer.flipRacer()
            racer.setTurnBack(True)

    def reRun(self, racer):
        racer.setCoordinates(0, racer.getCoordinates()[1])

    def buffShield(self, racer):
        racer.SttList.append(self.image)

def ShowEffect(amulet, index):
    SCALE = 300

    while SCALE != 0:
        SCALE = SCALE - 20
        amulet.shape = pygame.transform.smoothscale(amulet.shape, (SCALE, SCALE))

        DISPLAYSURF.blit(amulet.shape, (Racers[index].getCoordinates()[0], Racers[index].getCoordinates()[1]))
        pygame.display.update()
        fpsClock.tick(60)

    amulet.handleAmulet(Racers[index])
    del amulet

def runGame(ClassIndex, UnitIndex):
    pygame.mixer.init()
    pygame.mixer.music.load('music/Overworld Map - Pokémon GO Music Extended.mp3')
    pygame.mixer.music.play(-1)


    Amulet_type_List = ['inc', 'dec', 'stun', 'reRun', 'turnBack', 'protect']
    Amulet_List_icon = ['image/speedup_amulet.png', 'image/speeddown_amulet.png', 'image/stop.png', 'image/bomb_amulet.png', 'image/turnback.png', 'image/shield_amulet.png']

    X_margin = 0
    Y_margin = WINDOW_HEIGHT/2 + (ROAD_WITDH+20)*2
    Check_Endgame = False

    START_LINE = Object('image/finish_line.png', 100, 200)
    FINISH_LINE = Object('image/finish_line.png', 1300, 200)
    THEME = Object('image/galaxy.jpg',0, 0)
    THEME.shape = pygame.transform.scale(THEME.shape, (WINDOW_WIDTH, WINDOW_HEIGHT))
    Arrow = Object('image/ArrowDown.png', 0, 0)
    Arrow.shape = pygame.transform.scale(Arrow.shape, (40, 40))

    Rank_Image_List = []
    Lucky_Button = Button(surface=DISPLAYSURF, rect=(1000, 10 , 250, 30), caption = 'LUCKY BUTTON', borderColor = pygame.Color("Black"))

    for image in RankList:
        rank_img = pygame.image.load(image)
        rank_img = pygame.transform.scale(rank_img, (50, 50))
        Rank_Image_List.append(rank_img)


    for i in range(5):
        Racers.append(Racer(RacerList[ClassIndex][i], X_margin, Y_margin - i*(ROAD_WITDH + 20)));
        RoadList.append(Object('image/Road.jpg', 0, Y_margin - i*(ROAD_WITDH + 20) - 20))
        dem = 0
        while dem < ROAD_LENGTH:
            dem = dem + 200
            index = randint(0, 5)
            AmuletList.append(Amulet(Amulet_type_List[index], Amulet_List_icon[index], X_margin + dem + randint(50, 120), Y_margin - i*(ROAD_WITDH + 20)))

    while True:
        DISPLAYSURF.blit(THEME.shape, (0, 0))

        Lucky_Button.draw()


        for i in range(5):
            Racers[i].moveRacer(randint(Racers[i].getSpeed()[0], Racers[i].getSpeed()[1]))
            DISPLAYSURF.blit(RoadList[i].getShape(), (RoadList[i].getCoordinates()))
            DISPLAYSURF.blit(START_LINE.shape, (80, 105))
            DISPLAYSURF.blit(FINISH_LINE.shape, (1200, 105))

        Check_Endgame = True
        for i in range(5):
            DISPLAYSURF.blit(Racers[i].getShape(), (Racers[i].getCoordinates()))

            if Racers[i].isFinish():
                Rank_index = Racers[i].getRank() - 1
                DISPLAYSURF.blit(Rank_Image_List[Rank_index], (Racers[i].getCoordinates()[0] - 10, Racers[i].getCoordinates()[1] + 10))
            else:
                Check_Endgame = False

            for stt in Racers[i].SttList:
                img = pygame.image.load(stt)
                img = pygame.transform.scale(img, (25, 25))
                DISPLAYSURF.blit(img, (Racers[i].getCoordinates()[0] - 10 + 20 * Racers[i].SttList.index(stt), Racers[i].getCoordinates()[1] - 20 ))

        for amulet in AmuletList:
            DISPLAYSURF.blit(amulet.getShape(), (amulet.getCoordinates()))

        DISPLAYSURF.blit(Arrow.shape, (Racers[UnitIndex].getCoordinates()[0] + 15, Racers[UnitIndex].getCoordinates()[1] - 50))

        if Check_Endgame:
            if Racers[UnitIndex].getRank() == 1:
                return True
            else:
                return False

        for event in pygame.event.get():
            Lucky_Button.set_state(event)
            if Lucky_Button.is_clicked(event) and Check_Endgame == False:
                if randint(1, 100) < 40 or Racers[UnitIndex].isFinish(): #40% cơ hội nhận bùa hại cho đối thủ
                    lucky_punish = randint(1, 4)
                    amulet_temp = Amulet(Amulet_type_List[lucky_punish], Amulet_List_icon[lucky_punish], 0, 0)
                    lucky_punish = randint(0, 4)
                    while lucky_punish == UnitIndex or Racers[lucky_punish].isFinish():
                        lucky_punish = randint(0, 4)
                    ShowEffect(amulet_temp, lucky_punish)

                else: #60% cơ hội nhận bùa lợi cho mình
                    if randint(1, 100) < 40:
                        amulet_temp = Amulet(Amulet_type_List[0], Amulet_List_icon[0], 0, 0)
                        amulet_temp.handleAmulet(Racers[UnitIndex])
                        ShowEffect(amulet_temp, UnitIndex)
                    else:
                        amulet_temp = Amulet(Amulet_type_List[5], Amulet_List_icon[5], 0, 0)
                        amulet_temp.handleAmulet(Racers[UnitIndex])
                        Racers[UnitIndex].removeFromSttList(Amulet_List_icon[5])
                        ShowEffect(amulet_temp, UnitIndex)
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        fpsClock.tick(FPS)