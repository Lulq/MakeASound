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
do = mixer.Sound("C.wav")
do_s = mixer.Sound("c#.wav")
re = mixer.Sound("D.wav")
re_s = mixer.Sound("d#.wav")
mi = mixer.Sound("E.wav")
fa = mixer.Sound("F.wav")
fa_s = mixer.Sound("f#.wav")
sol = mixer.Sound("G.wav")
sol_s = mixer.Sound("g#.wav")
la = mixer.Sound("A.wav")
la_s = mixer.Sound("a#.wav")
si = mixer.Sound("B.wav")


while True:
    pygame.draw.rect(DISPLAY,retColor,(250,150,10,30), 1)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_q:
                mixer.Sound.play(do)
            elif event.key == K_2:
                mixer.Sound.play(do_s)
            elif event.key == K_w:
                mixer.Sound.play(re)
            elif event.key == K_3:
               mixer.Sound.play(re_s)
            elif event.key == K_e:
                mixer.Sound.play(mi)
            elif event.key == K_r:
                mixer.Sound.play(fa)
            elif event.key == K_5:
                mixer.Sound.play(fa_s)
            elif event.key == K_t:
                mixer.Sound.play(sol)
            elif event.key == K_6:
                mixer.Sound.play(sol_s)
            elif event.key == K_y:
                mixer.Sound.play(la)
            elif event.key == K_7:
                mixer.Sound.play(la_s)
            elif event.key == K_u:
                mixer.Sound.play(si)

        if event.type == KEYUP:
            if event.key == K_q:
                mixer.Sound.stop(do)
            if event.key == K_2:
                mixer.Sound.stop(do_s)
            if event.key == K_w:
                mixer.Sound.stop(re)
            if event.key == K_3:
                mixer.Sound.stop(re_s)
            if event.key == K_e:
                mixer.Sound.stop(mi)
            if event.key == K_r:
                mixer.Sound.stop(fa)
            if event.key == K_5:
                mixer.Sound.stop(fa_s)
            if event.key == K_t:
                mixer.Sound.stop(sol)
            if event.key == K_6:
                mixer.Sound.stop(sol_s)
            if event.key == K_y:
                mixer.Sound.stop(la)
            if event.key == K_7:
                mixer.Sound.stop(la_s)
            if event.key == K_u:
                mixer.Sound.stop(si)
      

           
           
                
    
    pygame.display.update()
