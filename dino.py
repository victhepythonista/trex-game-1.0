import pygame
from sounds import GameSounds

DINOBIRD_Y = 300
dino_images = [
        'images/dino/dino1.png',
        'images/dino/dino2.png',
        'images/dino/dino3.png',
        'images/dino/dino4.png',
        'images/dino/dino5.png',
        'images/dino/dino6.png',
        'images/dino/dino7.png',
        ]
pterodactyl_images = [
        'images/pterodactyl/1.png',
        'images/pterodactyl/2.png',
        'images/pterodactyl/3.png',
        'images/pterodactyl/4.png',
        'images/pterodactyl/5.png',
        'images/pterodactyl/6.png',
        'images/pterodactyl/7.png',
        'images/pterodactyl/8.png',
        'images/pterodactyl/9.png',
        'images/pterodactyl/10.png',
        'images/pterodactyl/11.png',
        'images/pterodactyl/12.png',
        'images/pterodactyl/13.png',
        'images/pterodactyl/14.png',
        'images/pterodactyl/15.png',
        'images/pterodactyl/16.png',
        'images/pterodactyl/17.png',
        'images/pterodactyl/18.png',
        'images/pterodactyl/19.png',
        'images/pterodactyl/20.png',
]

dino_loaded_images = [pygame.image.load(img) for img in dino_images]
loaded_pterodactyl_images = [pygame.image.load(img) for img in pterodactyl_images]

dead_dino = pygame.image.load('images/dino/dead.png')
velocity = 9
class Dino:
    def __init__(self,position = (50,300)):
        self.x = position[0]
        self.y = position[1]
        self.position = position
        self.width = 40
        self.height = 50
        self.images = dino_loaded_images
        self.image_count = 0
        self.dead = False
        self.current_image = self.images[self.image_count]

        self.rect_x = self.x + 10
        self.rect_y = self.y
        self.rect = pygame.Rect(self.rect_x, self.y, self.width, self.height)

        self.can_jump = True
        self.is_jumping = False
        self.mass = 1

        self.velocity = velocity
        self.velocity_limit = -(self.velocity + 1)
    def jump(self):
        if self.is_jumping:

            force = .5 * self.mass *  (self.velocity ** 2)

            self.y -= force
            self.velocity -= 1
            if self.velocity < 0:
                self.mass = -1

            if self.velocity == self.velocity_limit :
                self.can_jump = True
                self.is_jumping = False
                self.mass = 1
                self.velocity = velocity

    def handle_environment(self, rects_in_environment):

        for rect in rects_in_environment:
            if self.rect.colliderect(rect):
                self.dead = True
                self.current_image = dead_dino

    def handle_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.is_jumping == False:
            self.is_jumping = True
            GameSounds.play('jump')
    def run_animation(self):

        if self.images[-1] == self.images[self.image_count]:
            self.image_count = 0
        else:
            self.image_count+= 1

        self.current_image = self.images[self.image_count]

    def show(self, window):
        if self.dead:
            window.blit(self.current_image, (self.x,self.y))
        else:
            self.handle_keys()
            self.jump()
            self.run_animation()
            self.rect = pygame.Rect(self.rect_x, self.y, self.width, self.height)
            #pygame.draw.rect(window, (10,130,24), self.rect, 1)
            window.blit(self.current_image, (self.x,self.y))

class Pterodactyl:
    def __init__(self, x):
        self.x = x
        self.rect = pygame.Rect(self.x,DINOBIRD_Y, 40,20)
        self.image =  None
        self.passed = False
        self.image_count = 0
        self.images = loaded_pterodactyl_images
        self.current_image = self.images[self.image_count]
    def flying_animation(self):
        if self.images[-1] == self.images[self.image_count]:
            self.image_count = 0
        else:
            self.image_count+= 1
        self.current_image = self.images[self.image_count]
    def get_rect(self):
        return self.rect
    def show(self, window, speed):
        self.flying_animation()
        if self.x < 0:
            self.passed = True
        self.x -= (speed*1.3)
        self.rect = pygame.Rect(self.x,DINOBIRD_Y + 20, 40,20)
        #pygame.draw.rect(window, (170,10,24), self.rect, 1)
        window.blit(self.current_image,(self.x,DINOBIRD_Y) )
