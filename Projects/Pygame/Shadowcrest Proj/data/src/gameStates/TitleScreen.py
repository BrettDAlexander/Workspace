# Shadowcrest v0.0.21
# by Brett Alexander

# import pygame
import os   # import os to change working directory for paths
import pygame   # import pygame version
from data.src.funcs import load_asset
from pygame.locals import *

class TitleSceneBG(pygame.sprite.Sprite):
    def __init__(self):
        os.chdir("C:/Users/Brett/Documents/GitHub/Workspace/Projects/Pygame/Shadowcrest/")
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_asset.load_image('TitleScreen.jpg', 0)
        pos = 0, 0

class TitleScene(object):
    def __init__(self):
        pass
    def render(self, screen):
        pass
    def update(self):
        pass
    def handle_events(self, events):
        pass