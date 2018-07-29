# Shadowcrest v0.0.21
# by Brett Alexander

# import pygame
import os   # import os to change working directory for paths
import pygame   # import pygame version
from data.src.funcs import load_asset
from data.src.gameStates import TitleScreen
from pygame.locals import *

# change working directory for file paths
os.chdir("C:/Users/Brett/Documents/GitHub/Workspace/Projects/Pygame/Shadowcrest/")

# create cursor
class Cursor(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_asset.load_image('GameCursor.png', 0)
    # cursor follows mouse
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.topleft = pos

# template to handle scenes
class Scene(object):
    def __init__(self):
        pass
    def render(self, screen):
        pass
    def update(self):
        pass
    def handle_events(self, events):
        pass

# manage scenes
class SceneManager(object):
    def __init__(self):
        self.go_to(TitleScreen.TitleScene())

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self

# gameplay for scene
class GameScene(Scene):
    def __init__(self):
        super(GameScene, self).__init__()
    def render(self, scene):
        pass
    def update(self):
        pass
    def handle_events(self, events):
        pass

# initialize game
def main():
    # initialize pygame
    pygame.init()

    # set window size
    window_width = 1280
    window_height = 720
    screen = pygame.display.set_mode([window_width, window_height])

    # load and set window icon and name
    logo = pygame.image.load('icon.png')
    pygame.display.set_icon(logo)
    pygame.display.set_caption('Shadowcrest (pre-concept)')
    pygame.mouse.set_visible(0)

    # define vars
    cursor = Cursor()   # var define game cursor
    titlescreen = TitleScreen.TitleSceneBG()    # var define title screen background
    cursorsprite = pygame.sprite.RenderPlain([cursor])  # var define render game cursor
    titlesprite = pygame.sprite.RenderPlain([titlescreen])  # var define render title screen background
    clock = pygame.time.Clock() # var define game clock speed
    scene = GameScene() # var define scene
    manager = SceneManager()    # var define scene manager

    # game state to boot to
    gameState = 0

    # game loop
    running = True
    while running:
        clock.tick(60)
        # close game on window close via red 'X' button
        for event in pygame.event.get(QUIT):
            running = False

        # render black screen for game window
        screen.fill([0, 0, 0])

        # render scene
        manager.scene.handle_events(pygame.event.get())
        manager.scene.update()
        manager.scene.render(screen)

        # show title screen background
        if gameState == 0:
            titlesprite.update()
            titlesprite.draw(screen)

        # draw and update cursor
        cursorsprite.update()
        cursorsprite.draw(screen)
        pygame.display.flip()

    # exit game
    pygame.quit()

# initialize game
if __name__ == '__main__':
    main()