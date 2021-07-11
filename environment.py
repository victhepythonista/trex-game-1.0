import random
import pygame


class Dirt:
    '''
    those little lines and dashes that represent the ground
    they are basically created using the pygame 'pygame.draw.lines' function
    '''
    def __init__(self,  width = random.randint(1,10), speed = 5 ):
        self.x =   random.randint(700, 1400)
        self.y =    random.randint(353,400)
        self.width = 3 *width/10
        self.speed = speed
    def show(self, window, speed):
        self.x -= speed
        coods = [
        [self.x,self.y],
        [self.x + self.width, self.y]
        ]
        pygame.draw.lines(window, (0,0,0),True, coods, 1 )


class Environmnent:
    """
    handles everything  involving the ground animation
    """
    def __init__(self):
        self.dirt = []
        self.limit = 100
    def show_dirt(self, window, speed):
        if len(self.dirt) < self.limit:
            self.dirt.append(Dirt())
        for d in self.dirt:
            d.show(window,speed)
            if d.x < 0:
                self.dirt.pop(self.dirt.index(d))

    def draw_ground(self, window):
        coods = [[0,350], [900,350]]
        pygame.draw.lines(window, (0,0,0),True, coods, 1 )
    def show_environment(self, window, speed):
        self.draw_ground(window)
        self.show_dirt(window, speed)
