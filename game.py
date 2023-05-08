try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

import random
import time

class Spritesheet:
    def __init__(self, sprite_url, dest_centre, velocity):
        self.sprite_url = sprite_url
        self.dest_centre = dest_centre
        self.velocity = velocity
    
class Keyboard:
    def __init__(self, right, left):
        self.right = right
        self.left = left
    
    def keyDown(self, key):
        if key == simplegui.KEY_MAP["right"]:
            self.right = True
        
        elif key == simplegui.KEY_MAP["left"]:
            self.left = True
    
    def keyUp(self, key):
        if key == simplegui.KEY_MAP["right"]:
            self.right = False
        
        elif key == simplegui.KEY_MAP["left"]:
            self.left = False

class Interaction:
    def __init__(self, game, keyboard):
        self.keyboard = keyboard
        self.game = game
