# Shadowcrest v0.0.21
# by Brett Alexander

# import pygame
import os   # import os to change working directory for paths
import pygame   # import pygame version
from pygame.locals import *

# load image files from '/data/res/sounds' path
def load_image(name, colorkey=None):
    os.chdir("C:/Users/Brett/Documents/GitHub/Workspace/Projects/Pygame/Shadowcrest/")
    fullname = os.path.join(os.getcwd(), 'data', 'res', 'imgs', name)
    try:
        image = pygame.image.load(fullname)
    except:
        print('Cannot load image:', name)
        print ('tried path: ' + fullname)
        raise SystemExit
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at([0, 0])
        image.set_colorkey(colorkey, RLEACCEL)
    return image, image.get_rect()

# load .wav sounds from '/data/res/sounds' path
def load_sound(name):
    class NoneSound:
        def play(self):
            pass
    if not pygame.mixer:
        return NoneSound()
    os.chdir("C:/Users/Brett/Documents/GitHub/Workspace/Projects/Pygame/Shadowcrest/")
    fullname = os.path.join(os.getcwd(), 'data','res','sounds', name)
    try:
        sound = pygame.mixer.Sound(fullname)
    except:
        print('Cannot load sound:', wav)
        print ('tried path: ' + fullname)
        raise SystemExit
    return sound