import pygame
def write_on_screen(  message, position, window, color, fontsize, font = 'consolas'):
    #### _this function  writes  a message to the user
    pygame.font.init()
    mess_obj = pygame.font.SysFont(font, fontsize)
    mess_render = mess_obj.render(message, 20, color)
    window.blit(mess_render, position)
