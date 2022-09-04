from ctypes.wintypes import PLARGE_INTEGER
from time import clock_getres
import pygame 

x = pygame.init()
gamewindow = pygame.display.set_mode((1200,700))
pygame.display.set_caption("Testing1 ")

cord_x = 50
cord_y = 50
vel_x = .5
vel_y = .5
exit_game = False
game_over = False

clock = pygame.time.Clock()
press = False
gamewindow.fill((255,255,255))
pygame.display.update()

while not exit_game:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            exit_game = True

    if events.type == pygame.MOUSEBUTTONDOWN:
        press = True 
     
    cord_x, cord_y = pygame.mouse.get_pos()    
    if press:
        if events.type == pygame.MOUSEBUTTONUP:
            press = False 
        pygame.draw.rect(gamewindow,(255,0,0),(cord_x,cord_y,10,10))
        pygame.display.update()
    clock.tick(6000)
    


pygame.QUIT
quit()