import pygame
import sys
from pygame.locals import *
from pygame import mixer

# Colors

RED = (255,0,0)
GREEN = (0,255,0)
retColor = RED

pygame.init()
DISPLAY = pygame.display.set_mode((500, 300))
pygame.display.set_caption('Draw')

mixer.init()

# pygame.draw.rect(DISPLAY,RED,(250,150,10,30), 1)
# pygame.draw.line(DISPLAY, GREEN,(100,20), (399,20), 10)

while True:
    pygame.draw.rect(DISPLAY,retColor,(250,150,10,30), 1)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_q:
                mixer.music.load("C.wav")
                mixer.music.play()
            elif event.key == K_2:
                mixer.music.load("c#.wav")
                mixer.music.play()    
            elif event.key == K_w:
                mixer.music.load("D.wav")
                mixer.music.play()
            elif event.key == K_3:
                mixer.music.load("d#.wav")
                mixer.music.play()
            elif event.key == K_e:
                mixer.music.load("E.wav")
                mixer.music.play()
            elif event.key == K_r:
                mixer.music.load("F.wav")
                mixer.music.play()
            elif event.key == K_5:
                mixer.music.load("f#.wav")
                mixer.music.play()
            elif event.key == K_t:
                mixer.music.load("G.wav")
                mixer.music.play()
            elif event.key == K_6:
                mixer.music.load("g#.wav")
                mixer.music.play()
            elif event.key == K_y:
                mixer.music.load("A.wav")
                mixer.music.play()
            elif event.key == K_7:
                mixer.music.load("a#.wav")
                mixer.music.play()
            elif event.key == K_u:
                mixer.music.load("B.wav")
                mixer.music.play()
            
                 
              
        elif event.type == KEYUP:
            mixer.music.pause()

    pygame.display.update()
