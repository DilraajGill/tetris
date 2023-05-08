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
    def __init__(self):
        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.space = False
    
    def keyDown(self, key):
        if key == simplegui.KEY_MAP["right"]:
            self.right = True
        
        elif key == simplegui.KEY_MAP["left"]:
            self.left = True
        
        elif key == simplegui.KEY_MAP["space"]:
            self.space = True

        elif key == simplegui.KEY_MAP["up"]:
            self.up = True
        
        elif key == simplegui.KEY_MAP["down"]:
            self.down = True
    
    def keyUp(self, key):
        if key == simplegui.KEY_MAP["right"]:
            self.right = False
        
        elif key == simplegui.KEY_MAP["left"]:
            self.left = False

        elif key == simplegui.KEY_MAP["space"]:
            self.space = False

        elif key == simplegui.KEY_MAP["up"]:
            self.up = False
        
        elif key == simplegui.KEY_MAP["down"]:
            self.down = False

class Interaction:
    def __init__(self, game, keyboard):
        self.keyboard = keyboard
        self.game = game
    
    def update(self):   
        if self.game.screen == "Welcome":
            self.updateWelcome()
    
    def updateWelcome(self):
        if self.keyboard.space == True:
            self.game.screen = "gameplay"


class Game:
    def __init__(self):
        self.screen = "Welcome"
        self.frame_width = 1920
        self.frame_height = 1080
        self.frame = simplegui.create_frame("TETRIS", self.frame_width, self.frame_height)
        self.initWelcome()

        self.interObj = Interaction(self, Keyboard())
        self.frame.set_draw_handler(self.draw)
        self.frame.set_keydown_handler(self.interObj.keyboard.keyDown)
        self.frame.set_keyup_handler(self.interObj.keyboard.keyUp)
        self.frame.start()
    
    def draw(self, canvas):
        self.interObj.update()
        if self.screen == "Welcome":
            self.drawWelcome(canvas)

    def initWelcome(self):
        self.welcomeText = "TETRIS"
        self.welcome_width = (self.frame_width - self.frame.get_canvas_textwidth(self.welcomeText, 60, "monospace")) / 2
        self.controlText = "CONTROLS:"

    def drawWelcome(self, canvas):
        canvas.draw_text(self.welcomeText, [self.welcome_width, 90], 60, "white", "monospace")
        canvas.draw_text(self.controlText, [200, 200], 60, "Red", "monospace")
        canvas.draw_text("Right Arrow: Move Right", [100, 250], 30, "white", "monospace")
        canvas.draw_text("Left Arrow: Move Left", [100, 300], 30, "white", "monospace")
        canvas.draw_text("Up Arrow: Rotate Clockwise", [100, 350], 30, "white", "monospace")
        canvas.draw_text("Down Arrow: Rotate Anticlockwise", [100, 400], 30, "white", "monospace")
game = Game()