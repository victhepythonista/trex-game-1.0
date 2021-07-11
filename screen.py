import pygame
import sys

class Screen:
    '''

    a simple screen... just define the size
    and you are ready to go

    the fps  and screen title can be changed
    the screen will have no frame if noframe is set to true

    '''
    def __init__(self, size, fps = 50, title = 'basic screen',  noframe = False):
        pygame.init()
        self.title = title
        self.running = True
        self.name = ""
        self.size = size
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.events = pygame.event.get()
        self.window = pygame.display.set_mode(self.size, pygame.NOFRAME  ) if noframe else pygame.display.set_mode(self.size  )
        

    def screen_backend(self):
        self.clock.tick(self.fps)
        pygame.display.set_caption(self.name)



    def exit(self):
        # exit the screen
        self.running = False

    def quit_event(self  ):
            # anticipate a quit event

        for ev in self.events:
            if ev.type == pygame.QUIT:
                pygame.quit()
                self.running = False
                sys.exit()
    def quit_screen(self):
        pygame.quit()
        self.running = False
        sys.exit()
    def custom_display(self):
        # your displays and widgets go here
        pass
    def show(self):

        while self.running:

            self.custom_display()
            self.events = pygame.event.get()
            self.screen_backend()

            self.quit_event()
            pygame.display.update()
            continue
