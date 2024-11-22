import sys
from pygame.locals import *
import pygame
from setting import *

def mainGame():
    pygame.init()
    screen = pygame.display.set_mode(SIZE, 0) # 窗口大小
    title = pygame.display.set_caption(TITLE)
    clock = pygame.time.Clock() # 设置时钟对象，用来追踪管理时间
    blackground = pygame.image.load()

    running = True

    while running:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()

if __name__ == "__main__":
    mainGame()