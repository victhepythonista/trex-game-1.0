import pygame

from random import randint, randrange, choice, choices
"""

cactus classes :
        - small         32
        - medium        40
        - large         60

        - general width = 10
"""

cactii_images = {
    'small':'./images/cacti/small.png',
    'large':'./images/cacti/large.png',
    'medium':'./images/cacti/medium.png',


        }
CACTUS_RECT_WIDTH = 10
CACTUS_Y = 370
SMALL_CACTUS_HEIGHT = 32
MEDIUM_CACTUS_HEIGHT = 40
LARGER_CACTUS_HEIGHT = 60

SMALL_CACTUS_Y = CACTUS_Y - SMALL_CACTUS_HEIGHT
MEDIUM_CACTUS_Y = CACTUS_Y - MEDIUM_CACTUS_HEIGHT
LARGE_CACTUS_Y = CACTUS_Y - LARGER_CACTUS_HEIGHT

class Cactus:
    """
    a basic cactus object...
    later modified to display different types of cacti"""
    def __init__(self, x,y, image ,h = 30 ):
        self.image = pygame.image.load(image) if image != None else None
        self.x = x
        self.y = y
        self.height = h
        self.rect = pygame.Rect(self.x, self.y, CACTUS_RECT_WIDTH,self.height )
        self.passed = False
    def move(self, speed):
        self.x -= speed
    def show(self, window, speed):
        self.rect = pygame.Rect(self.x, self.y, CACTUS_RECT_WIDTH,self.height )
        if self.x < -20:
            self.passed = True
        self.move(speed)
        if self.image != None:
            window.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(window, (30,20,2) ,self.rect , 2, 10)
        #pygame.draw.rect(window, (30,20,2) ,self.rect , 2, 10)
class SmallCactus(Cactus):
    def __init__(self, x ):
        image = cactii_images['small']
        Cactus.__init__(self,x,SMALL_CACTUS_Y,image, h = SMALL_CACTUS_HEIGHT )


class MediumCactus(Cactus):
    def __init__(self, x ):
        image = cactii_images['medium']
        Cactus.__init__(self,x, MEDIUM_CACTUS_Y,image, h = MEDIUM_CACTUS_HEIGHT )

class LargeCactus(Cactus):
    def __init__(self, x ):
        image = cactii_images['large']
        Cactus.__init__(self,x, LARGE_CACTUS_Y,image, h =LARGER_CACTUS_HEIGHT)

 #--------------------------------------------------

def get_cactii(x ):
    " returns a random cactus object  "
    size = choice([1,2,3])

    cactus = None
    if size == 1:
        cactus = SmallCactus
    if size == 2:
        cactus =  MediumCactus
    if size == 3:
        cactus =  LargeCactus
    cactus = cactus(x)
    return cactus

class CactiManager:
    """
    handles the cacti animation according to the current level's speed
    """
    def __init__(self, level = 1, speed = 5):
        self.cacti_groups = []
        self.level = level
        self.cacti_limit = 4
        self.cacti_group_proximity= 500
        self.speed = speed
    def generate(self):
        # generate a new cactus group/bush of up to 3 cacti
        number_of_cacti = choice([1,1,1,2,3])
        last_position = (self.cacti_groups[-1][-1].x + self.cacti_group_proximity) if self.cacti_groups != [] else 850
        cacti_group  = []
        for i in range(number_of_cacti):
            cacti = get_cactii(last_position)
            cacti_group.append(cacti )
            last_position += CACTUS_RECT_WIDTH
        self.cacti_groups.append(cacti_group)

    def get_rects(self):
        # get the rects of the cacti
        rects = []
        for g in self.cacti_groups:
            for c in g:
                rects.append(c.rect)
        return rects

    def manage_cacti(self, window, speed):
        # display and manage cacti
        if len(self.cacti_groups) < self.cacti_limit:
            # add a new cacti group 
            self.generate()

        for group in self.cacti_groups:
            if group == []:
                self.cacti_groups.pop(self.cacti_groups.index(group))
            for cactus in group:
                cactus.show(window, speed)
                if cactus.passed:
                    group.pop(group.index(cactus))
