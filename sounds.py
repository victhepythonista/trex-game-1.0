
import pygame

pygame.mixer.init()
sounds = {
    'jump':'sounds/jump1.mp3',
    'gameover':'sounds/descend8.mp3',
    'highscore':'sounds/highscore.wav',
            }


class GameSounds:
    '''
    manages the in-game Sounds
    '''
    @staticmethod
    def play(soundname, volume = .5):
        pygame.mixer.init()
        sound  = sounds[soundname]
        pygame.mixer.music.load(sound)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play()
