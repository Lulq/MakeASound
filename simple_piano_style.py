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

do5 = mixer.Sound("C5.wav")
do5_s = mixer.Sound("c5#.wav")
re5 = mixer.Sound("D5.wav")
re5_s = mixer.Sound("d5#.wav")
mi5 = mixer.Sound("E5.wav")
fa5 = mixer.Sound("F5.wav")
fa5_s = mixer.Sound("f5#.wav")
sol5 = mixer.Sound("G5.wav")
sol5_s = mixer.Sound("g5#.wav")
la5 = mixer.Sound("A5.wav")
la5_s = mixer.Sound("a5#.wav")
si5 = mixer.Sound("B5.wav")



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
            # segunda oitava c5 a b5
            if event.key == K_v:
                mixer.Sound.play(do5)
            elif event.key == K_g:
                mixer.Sound.play(do5_s)
            elif event.key == K_b:
                mixer.Sound.play(re5)
            elif event.key == K_h:
               mixer.Sound.play(re5_s)
            elif event.key == K_n:
                mixer.Sound.play(mi5)
            elif event.key == K_m:
                mixer.Sound.play(fa5)
            elif event.key == K_k:
                mixer.Sound.play(fa5_s)
            elif event.key == K_COMMA:
                mixer.Sound.play(sol5)
            elif event.key == K_l:
                mixer.Sound.play(sol5_s)
            elif event.key == K_PERIOD:
                mixer.Sound.play(la5)
            elif event.key == K_RCTRL:
                mixer.Sound.play(la5_s)
            elif event.key == K_SEMICOLON:
                mixer.Sound.play(si5)


        #Stop Sound

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
            # segunda oitava c5 a b5
            if event.key == K_v:
                mixer.Sound.stop(do5)
            if event.key == K_g:
                mixer.Sound.stop(do5_s)
            if event.key == K_b:
                mixer.Sound.stop(re5)
            if event.key == K_h:
               mixer.Sound.stop(re5_s)
            if event.key == K_n:
                mixer.Sound.stop(mi5)
            if event.key == K_m:
                mixer.Sound.stop(fa5)
            if event.key == K_k:
                mixer.Sound.stop(fa5_s)
            if event.key == K_COMMA:
                mixer.Sound.stop(sol5)
            if event.key == K_l:
                mixer.Sound.stop(sol5_s)
            if event.key == K_PERIOD:
                mixer.Sound.stop(la5)
            if event.key == K_RCTRL:
                mixer.Sound.stop(la5_s)
            if event.key == K_SEMICOLON:
                mixer.Sound.stop(si5)
            
                
    
    pygame.display.update()
