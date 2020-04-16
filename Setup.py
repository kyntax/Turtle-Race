import pygame, sys
import os.path
from pygame import *
import pygame.locals as pl

pygame.init()
pygame.font.init()

#Set displayScreen
sizescreen = screen_width, screen_height = 1280,720
screen = pygame.display.set_mode(sizescreen)
pygame.display.set_caption("Login window")

FPS = 50  # frames per second setting
fpsClock = pygame.time.Clock()
DEFAULT_FONT = pygame.font.SysFont("freesansbold.ttf", 30, True)

state =  0 #Trạng thái: state = 0 (Login); state = 1 (Sign Up); state = 2 (Main Menu); state = 3 (Before Start); state = 4 (Game Screen)
         #Trạng thái: state = 5 (4->5)(Result Game); state = 6 (Introductions); state = 7 (MiniGame); state = 8 (Result MiniGame)
         #Trạng thái: state = 9 (Settings); state = 10 (About)
userMoney = -1
username = ''
password = ''
global check_mainGame
user_character =1
user_characterIndex =1
#COLOR BUTTON STATE
normal_COLOR = (52,144,247)
hightlight_COLOR = (69,161,249)
down_COLOR = (43,122,210)
def drawRoundedRect(surface,color,rect,radius=0.2):

    """
    AAfilledRoundedRect(surface,rect,color,radius=0.4)

    surface : destination
    rect    : rectangle
    color   : rgb or rgba
    radius  : 0 <= radius <= 1
    """

    rect         = Rect(rect)
    color        = Color(*color)
    alpha        = color.a
    color.a      = 0
    pos          = rect.topleft
    rect.topleft = 0,0
    rectangle    = Surface(rect.size,SRCALPHA)

    circle       = Surface([min(rect.size)*3]*2,SRCALPHA)
    draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
    circle       = transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)

    radius              = rectangle.blit(circle,(0,0))
    radius.bottomright  = rect.bottomright
    rectangle.blit(circle,radius)
    radius.topright     = rect.topright
    rectangle.blit(circle,radius)
    radius.bottomleft   = rect.bottomleft
    rectangle.blit(circle,radius)

    rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
    rectangle.fill((0,0,0),rect.inflate(0,-radius.h))

    rectangle.fill(color,special_flags=BLEND_RGBA_MAX)
    rectangle.fill((255,255,255,alpha),special_flags=BLEND_RGBA_MIN)

    return surface.blit(rectangle,pos)
class BUTTON(object):
    def __init__(self,
                 surface, #Bề mặt hiển thị button
                 rect = None, #Shape button
                 caption = '', #Nội dung trong button
                 bgcolor = normal_COLOR, #Màu nền button mặc định
                 fgcolor = pygame.Color("White"), #Màu chữ button
                 font = None, #font chữ text trong button
                 borderColor = None): #Button có viền hay không prameter color
        #Declare button_properties
        self._surface = surface
        if rect is None:
            self._rect = pygame.Rect(0, 0, 40, 60)
        else:
            self._rect = pygame.Rect(rect[0],rect[1],rect[2],rect[3])

        self._caption = caption
        self._bgcolor = bgcolor
        self._fgcolor = fgcolor
        self._border = borderColor
        if font is None:
            self._font = DEFAULT_FONT
        else:
            self._font = font

    def draw(self):
        # Call this method to draw the button on the screen
        if self._border is not None:
            drawRoundedRect(self._surface, self._border, (self._rect.left, self._rect.top, self._rect.width + 4, self._rect.height + 4))
            drawRoundedRect(self._surface, self._bgcolor, (self._rect.left + 2, self._rect.top + 2, self._rect.width, self._rect.height))
        else:
            drawRoundedRect(self._surface, self._bgcolor, (self._rect.left, self._rect.top , self._rect.width, self._rect.height))
        #Set font, location cua button
        if self._caption != '':
            captionSurf = self._font.render(self._caption, 1, self._fgcolor)
            captionRect = captionSurf.get_rect()
            captionRect.center = self._rect.center
            self._surface.blit(captionSurf, captionRect)

    def mouseEnter(self):
        #Check whether moupos is in button or not
        return self._rect.collidepoint(pygame.mouse.get_pos())
    #method cài đặt state cho button
    def set_state(self,event):
        if event.type == pygame.MOUSEMOTION:
            if self.mouseEnter():
                self._bgcolor = hightlight_COLOR
            else:
                self._bgcolor = normal_COLOR
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.mouseEnter():
               self._bgcolor = down_COLOR
        if event.type == pygame.MOUSEBUTTONUP:
            if self.mouseEnter():
                self._bgcolor = hightlight_COLOR
    def is_clicked(self, *arg):
        pass
class Button(BUTTON):
    def is_clicked(self, *args):
        if len(args) == 5:
            return args[0].type == pygame.MOUSEBUTTONUP and self._rect.collidepoint(pygame.mouse.get_pos())
        else:
            return pygame.mouse.get_pressed()[0] and self._rect.collidepoint(pygame.mouse.get_pos())
class Textbox:

    def __init__(
            self,
            initial_string="",
            font_family="",
            font_size=35,
            antialias=True,
            text_color=(0, 0, 0),
            cursor_color=(0, 0, 1),
            repeat_keys_initial_ms=400,
            repeat_keys_interval_ms=35):
        """
        :param initial_string: Initial text to be displayed
        :param font_family: name or list of names for font (see pygame.font.match_font for precise format)
        :param font_size:  Size of font in pixels
        :param antialias: Determines if antialias is applied to font (uses more processing power)
        :param text_color: Color of text (duh)
        :param cursor_color: Color of cursor
        :param repeat_keys_initial_ms: Time in ms before keys are repeated when held
        :param repeat_keys_interval_ms: Interval between key press repetition when helpd
        """

        # Text related vars:
        self.antialias = antialias
        self.text_color = text_color
        self.font_size = font_size
        self.input_string = initial_string  # Inputted text

        if not os.path.isfile(font_family):
            font_family = pygame.font.match_font(font_family)

        self.font_object = pygame.font.Font(font_family, font_size)

        # Text-surface will be created during the first update call:
        self.surface = pygame.Surface((1, 1))
        self.surface.set_alpha(0)

        # Vars to make keydowns repeat after user pressed a key for some time:
        self.keyrepeat_counters = {}  # {event.key: (counter_int, event.unicode)} (look for "***")
        self.keyrepeat_intial_interval_ms = repeat_keys_initial_ms
        self.keyrepeat_interval_ms = repeat_keys_interval_ms

        # Things cursor:
        self.cursor_surface = pygame.Surface((int(self.font_size/20+1), self.font_size))
        self.cursor_surface.fill(cursor_color)
        self.cursor_position = len(initial_string)  # Inside text
        self.cursor_visible = True  # Switches every self.cursor_switch_ms ms
        self.cursor_switch_ms = 500  # /|\
        self.cursor_ms_counter = 0

        self.clock = pygame.time.Clock()

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.cursor_visible = True  # So the user sees where he writes

                # If none exist, create counter for that key:
                if event.key not in self.keyrepeat_counters:
                    self.keyrepeat_counters[event.key] = [0, event.unicode]

                if event.key == pl.K_BACKSPACE:
                    self.input_string = (
                        self.input_string[:max(self.cursor_position - 1, 0)]
                        + self.input_string[self.cursor_position:]
                    )

                    # Subtract one from cursor_pos, but do not go below zero:
                    self.cursor_position = max(self.cursor_position - 1, 0)
                elif event.key == pl.K_DELETE:
                    self.input_string = (
                        self.input_string[:self.cursor_position]
                        + self.input_string[self.cursor_position + 1:]
                    )

                elif event.key == pl.K_RETURN:
                    return True

                elif event.key == pl.K_RIGHT:
                    # Add one to cursor_pos, but do not exceed len(input_string)
                    self.cursor_position = min(self.cursor_position + 1, len(self.input_string))

                elif event.key == pl.K_LEFT:
                    # Subtract one from cursor_pos, but do not go below zero:
                    self.cursor_position = max(self.cursor_position - 1, 0)

                elif event.key == pl.K_END:
                    self.cursor_position = len(self.input_string)

                elif event.key == pl.K_HOME:
                    self.cursor_position = 0

                else:
                    # If no special key is pressed, add unicode of key to input_string
                    self.input_string = (
                        self.input_string[:self.cursor_position]
                        + event.unicode
                        + self.input_string[self.cursor_position:]
                    )
                    self.cursor_position += len(event.unicode)  # Some are empty, e.g. K_UP

            elif event.type == pl.KEYUP:
                # *** Because KEYUP doesn't include event.unicode, this dict is stored in such a weird way
                if event.key in self.keyrepeat_counters:
                    del self.keyrepeat_counters[event.key]

        # Update key counters:
        for key in self.keyrepeat_counters:
            self.keyrepeat_counters[key][0] += self.clock.get_time()  # Update clock

            # Generate new key events if enough time has passed:
            if self.keyrepeat_counters[key][0] >= self.keyrepeat_intial_interval_ms:
                self.keyrepeat_counters[key][0] = (
                    self.keyrepeat_intial_interval_ms
                    - self.keyrepeat_interval_ms
                )

                event_key, event_unicode = key, self.keyrepeat_counters[key][1]
                pygame.event.post(pygame.event.Event(pl.KEYDOWN, key=event_key, unicode=event_unicode))

        # Re-render text surface:
        self.surface = self.font_object.render(self.input_string, self.antialias, self.text_color)

        # Update self.cursor_visible
        self.cursor_ms_counter += self.clock.get_time()
        if self.cursor_ms_counter >= self.cursor_switch_ms:
            self.cursor_ms_counter %= self.cursor_switch_ms
            self.cursor_visible = not self.cursor_visible

        if self.cursor_visible:
            cursor_y_pos = self.font_object.size(self.input_string[:self.cursor_position])[0]
            # Without this, the cursor is invisible when self.cursor_position > 0:
            if self.cursor_position > 0:
                cursor_y_pos -= self.cursor_surface.get_width()
            self.surface.blit(self.cursor_surface, (cursor_y_pos, 0))

        self.clock.tick()
        return False

    def get_surface(self):
        return self.surface

    def get_text(self):
        return self.input_string

    def get_cursor_position(self):
        return self.cursor_position

    def set_text_color(self, color):
        self.text_color = color

    def set_cursor_color(self, color):
        self.cursor_surface.fill(color)

    def clear_text(self):
        self.input_string = ""
        self.cursor_position = 0
        self.update(pygame.event.get())
    def set_rect(self,rect):
        self._rect = pygame.Rect(rect)
    def get_rect(self):
        return self._rect

    def mouseEnter(self):
        return self._rect.collidepoint(pygame.mouse.get_pos())
    def is_clicked(self):
        return pygame.mouse.get_pressed()[0] and self._rect.collidepoint(pygame.mouse.get_pos())

class Image():
    def __init__(self,image,x,y):
        self._x = x
        self._y = y
        self._image = image
        self._size = self._image.get_rect().size
        self._rect = pygame.Rect(self._x, self._y,self._size[0], self._size[1])
        self._rect.center = self._x, self._y
    def display(self):
        screen.blit(self._image, self._rect)
    def update(self, imageUpdate):
        self._image = imageUpdate
        self._size = self._image.get_rect().size
        self._rect = pygame.Rect(self._x, self._y, self._size[0], self._size[1])
        self._rect.center = self._x, self._y
        self.display()
    def mouseEnter(self):
        # Check whether moupos is in button or not
        return self._rect.collidepoint(pygame.mouse.get_pos())
    def onclick(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self._rect.collidepoint(pygame.mouse.get_pos())
    def mouseDown(self,event):
        return event.type == pygame.MOUSEBUTTONDOWN
    def mouseUp(self,event):
        return event.type == pygame.MOUSEBUTTONUP
# Declare Title
def textObj(caption, color, font_family = None, font_size = None):
    if font_family == None and font_size ==None:
        font = pygame.font.SysFont("comicsansms", 30, True)
    if font_family != None and font_size!= None:
        font = pygame.font.SysFont(font_family, font_size, True)
    if font_family != None and font_size == None:
        font = pygame.font.SysFont(font_family, 30, True)
    if font_family == None and font_size != None:
        font = pygame.font.SysFont("comicsansms", font_size, True)
    surf = font.render(caption, 1, pygame.Color(color))
    rect = surf.get_rect()
    return surf,rect


