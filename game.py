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
    
    