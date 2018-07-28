# Shadowcrest v0.0.15
# by Brett Alexander

# import game
import os   # import os to change working directory for paths
import pygame   # import pygame version
from pygame.locals import *

# warnings 
if not pygame.font: print('Warning, fonts disabled')
if not pygame.mixer: print('Warning, sound disabled')

# change working directory for file paths
os.chdir("C:/Users/Brett/Documents/GitHub/Workspace/Projects/Pygame/Shadowcrest/res")

# load image files from os.chdir path
def load_image(name, colorkey=None):
    fullname = os.path.join('imgs', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error:
        print('Cannot load image:', name)
        raise SystemExit
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at([0, 0])
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

# load .wav sounds from os.chdir path
def load_sound(name):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('sounds', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error:
        print('Cannot load sound:', wav)
        raise SystemExit
    return sound

# create cursor
class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('gcursor.png', 0)

    # cursor follows mouse
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.topleft = pos

# create background
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

# initialize game
def main():
    # initialize pygame
    pygame.init()

    # load and set window icon and name
    logo = pygame.image.load("./imgs/sword.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption('Shadowcrest')
    pygame.mouse.set_visible(0)
    
    # set window size
    window_width = 1280
    window_height = 720
    screen = pygame.display.set_mode((window_width, window_height))

    # setup background
    background = pygame.Surface(screen.get_size())
    BackGround = Background('./imgs/mainmenu.png', [0,0])

    # call cursor
    cursor = Cursor()
    clock = pygame.time.Clock()
    allsprites = pygame.sprite.RenderPlain((cursor))

    # game loop
    running = True
    while running:
        clock.tick(30)

        # quit cleanly
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                running = False

        # fill background
        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)

        # add title
        if pygame.font:
            font = pygame.font.SysFont('inkfree', 96)
            font.set_bold(True)
            text = font.render("Shadowcrest", 1, (150, 20, 20))
            textpos = text.get_rect(centerx=background.get_width()/2, centery=background.get_height()/3)
            screen.blit(text, textpos)

        # draw all of sprites (ie. cursor)
        allsprites.update()
        allsprites.draw(screen)
        pygame.display.flip()

    # exit game
    pygame.quit()

# initialize game
if __name__ == '__main__':
    main()