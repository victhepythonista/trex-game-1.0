import pygame
import random

clouds = [
    'images/clouds/cloud1.png',
    'images/clouds/cloud2.png',
    'images/clouds/cloud3.png',
    'images/clouds/cloud4.png',
    'images/clouds/cloud5.png',
]
loaded_clouds = [pygame.image.load(cloud) for cloud in clouds]

class Cloud:
    def __init__(self):
        self.image  =  random.choice(loaded_clouds)                    #choose a random cloud image
        self.x = random.randint(800, 1600)
        self.y = random.randint(50,250)
        self.passed = False
    def show(self, window):
        self.x -= .5
        if self.x < 0:
            self.passed = True

        if self.image:
            window.blit(self.image, (self.x,self.y))
class CloudManager:
    def __init__(self):
        self.clouds = []

    def show_clouds(self, window):
        if len(self.clouds) <  7:
            self.clouds.append(Cloud())
        for cloud in self.clouds:
            cloud.show(window)
            if cloud.passed:
                self.clouds.pop(self.clouds.index(cloud))
