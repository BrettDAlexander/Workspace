# Shadowcrest v0.0.1
# by Brett Alexander

import pygame as pg
import random
from settings import *

class Game():
    def __init__(self): # initialize game
        self.running = True
    def new(self): # new game
        pass
    def run(self): # game loop
        pass
    def draw(self): # game loop - draw
        pass
    def update(self): # game loop - update
        pass
    def events(self): # game loop - events
        pass
    def show_titlemenu(self):
        pass
    def level_1(self):

g = Game()
g.show_titlemenu()

while g.running:
    g.new()
    g.level_1()

pg.quit()