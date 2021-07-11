'''

desc        : a close enough copy of the famous trex browser game
author      : Leting Victor Kipkemboie
date        :7/11/2021
github      :victhepythonnista

ENJOY :)
'''


import pygame
import os
import time

# my custom modules
from screen import Screen
from tools import write_on_screen
from dino import Dino,Pterodactyl
from sounds import GameSounds
from environment import Environmnent
from cacti import CactiManager
from clouds import CloudManager

# constants
sky_image = pygame.image.load('images/sky.png')
game_icon = pygame.image.load('images/dino/dino3.png')
HIGHSCORE_FILE = './data/highscore.txt'
RUNNING = True
DEAD = False
SCREENSIZE = 850,400
INITIAL_SPEED = 6
SCORE = 0
LEVEL = 0
FONT = 20
bg_color = 240,240,240


class ScoreManager:
    '''
    checks if the highscore is beaten and saves the new HIGHSCORE
    '''
    @staticmethod
    def check_file():
        # check if the highscore file exists
        if os.path.isfile(HIGHSCORE_FILE):
            pass
        else:
            # make a new one if it doesnt exist
            with open(HIGHSCORE_FILE, 'w') as f:f.write('0')
    @staticmethod
    def get_highscore():
        # get the current highscore
        ScoreManager.check_file()
        with open(HIGHSCORE_FILE, 'r') as h:
            data =  h.read()
        try:
            current_highscore = int(data)
        except:
            ScoreManager.new_highscore(0)
            current_highscore = 0

        return current_highscore
    @staticmethod
    def new_highscore(score):
        # enter the new highscore
        with open(HIGHSCORE_FILE, 'w') as file:file.write(str(score))
    @staticmethod
    def is_highscore(score):
        # check if the score provided is a highscore
        current_highscore = ScoreManager.get_highscore()
        highscore = score > current_highscore
        if highscore:
            ScoreManager.new_highscore(score)
            return True
        else:
            return False




class GameScreen(Screen):
    '''

    the game screen...inherits from Screen


    check the Screen object it inherits from to learn more
    '''
    def __init__(self):
        Screen.__init__(self, SCREENSIZE, fps = 60)
        self.title = 'TREX GAME'
        self.score = 0
        self.environment_manager = Environmnent()
        self.cactimanager = CactiManager()
        self.speed = INITIAL_SPEED
        self.score_cache = 1000
        self.pterodactyls = [Pterodactyl(500)]  # should have called it dinobird ....pterodactyl is a long long word :)
        self.cloud_manager  = CloudManager()
        self.dino = Dino()
        self.dino_is_alive = True
        self.checked_highscore = False
        self.results_color = 30,30,30
        self.results = ''
        pygame.display.set_icon(game_icon)
        pygame.display.set_caption(self.title)
    def show_score(self  ):
        # display the score and highscore
        current_score = "SCORE : %s" % self.score
        highscore = 'highscore : %s' %ScoreManager.get_highscore()
        write_on_screen( current_score, (500,20), self.window, (30,50,70), FONT )
        write_on_screen( highscore, (200,20), self.window, (10,50,70), FONT )

    def manage_speed(self):
        # mange the game speed
        # increases game speed after every 2000 points
        if   self.score > self.score_cache:
            self.score_cache += 2000
            self.speed += 1
        if self.score%500 == 0 and self.score > 0:
            # add a pterodactyl
            pos_x = self.cactimanager.cacti_groups[-1][-1].x + 200   # the last cactus x position
            self.pterodactyls.append(Pterodactyl(pos_x))
    def handle_cacti(self):
        # display the cacti
        self.cactimanager.manage_cacti(self.window, self.speed)
    def reset_game(self):
        # reset the game variables and constants
        self.score = 0
        self.speed = INITIAL_SPEED
        self.cactimanager = CactiManager()
        self.environment_manager = Environmnent()
        self.cloud_manager  = CloudManager()
        self.checked_highscore = False
        self.pterodactyls = []
    def unpause(self):
        # wait for r to start the gameover#
        # and q to quit
        keys = pygame.key.get_pressed()
        if keys[pygame.K_r]:
            self.dino = Dino()
            self.reset_game()
        if keys[pygame.K_q]:
            self.quit_screen()
            # quit the game

    def get_pterodactyl_rect(self):
        # get the rects of the pterodactyls
        rects = []
        for pt in self.pterodactyls:
            rects.append(pt.get_rect())
        return rects

    def handle_dino(self):
        # display the trex
        self.dino.show(self.window)
        # get environment rects and check for collisions
        rects = self.cactimanager.get_rects() + self.get_pterodactyl_rect()
        self.dino.handle_environment(rects)
        if self.dino.dead:
            # GAME OVER !
            if ScoreManager.is_highscore(self.score):
                # write new highscore if the score is a highscore
                self.results = 'NEW HIGHSCORE !!'
                self.results_color = 100,200,120
                GameSounds.play('highscore')

            else:
                GameSounds.play('gameover', .2)
                self.results = ' GAME OVER !'
                self.results_color = 100,20,12

    def handle_pterodactyls(self):
        # display those pterodactyls
        for pterodactyl in self.pterodactyls:
            pterodactyl.show(self.window, self.speed)
            if pterodactyl.passed:
                self.pterodactyls.pop(self.pterodactyls.index(pterodactyl))

    def custom_display(self):

        if self.dino.dead:
            self.unpause()
            self.dino.show(self.window)
            write_on_screen(self.results, (250,100), self.window, self.results_color, 60)
            write_on_screen('  press R to RESTART', (250,200), self.window, (40,10,70), 20)
            write_on_screen('  press Q to QUIT', (250,300), self.window, (40,10,70), 20)

        else:
            # continue playing as the trex aint dead
            self.manage_speed()
            self.window.fill(bg_color)
            self.window.blit(sky_image,(0,-10))

            self.cloud_manager.show_clouds(self.window)
            self.environment_manager.show_environment(self.window, self.speed)
            self.handle_cacti()
            self.handle_pterodactyls()
            self.handle_dino()
            self.score += 1
            self.show_score()


if __name__ == '__main__':
    # start the game
    GameScreen().show()
