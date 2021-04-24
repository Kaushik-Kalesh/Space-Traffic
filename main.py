import pygame as pg
from math import *
import random

pg.init()

def spaceship_img(img):
    img = pg.image.load(img)
    img2 = pg.transform.rotate(img, 180)
    return img2

#adding images/objects
screen = pg.display.set_mode((800, 580))
pg.display.set_caption('Space Invaders')
player = pg.image.load('./images/spaceship.png')
pg.display.set_icon(player)
enemy1 = spaceship_img('./images/enemy1.png')
enemy2 = spaceship_img('./images/enemy2.png')
asteroid1 = spaceship_img('./images/asteroid.png')
asteroid2 = pg.image.load('./images/asteroid2.png')
enemy3 = spaceship_img('./images/enemy3.png')
enemy4 = spaceship_img('./images/enemy4.png')
enemy5 = spaceship_img('./images/enemy5.png')
bullet = pg.image.load('./images/bullet.png')

#adding backgrounds
bg_1 = pg.image.load('./images/spacebg.png')
bg = pg.transform.scale(bg_1, (800, 580))
font = pg.font.Font("freesansbold.ttf", 64)
font2 = pg.font.Font("freesansbold.ttf", 32)
gameover = font.render("GAME OVER", True, (255, 255, 255))
Paused_Screen = font.render("PAUSED", True, (255, 255, 255))
start = font.render("SPACE INVADERS", True, (255, 255, 255))
start2 = font2.render("Press Space to Start", True, (255, 255, 255))

#initializing/allotting coordinates/positions
distance2 = True
x = 350
y = 450
x2 = random.randint(0, 700)
x3 = -100
y2 = -100
y3 = 0
x4 = -100
y4 = 0
x5 = -100
y5 = 0
x6 = -100
y6 = 0
x7 = -100
y7 = 0
x8 = -100
y8 = 0
count = 0
score = 0
changeinx = 0
bx = -100
by = 450
changeinby = 0
distances = []
cnt = 0
paused = False

#related functions
def blit(img, position):
    screen.blit(img, position)

def distance(x, x2, y, y2):
    distance = sqrt(pow(x - x2, 2) + pow(y - y2, 2))
    if distance < 46:
        return True

'''def distance_2(bx, x2, by, y2):
        distance = sqrt(pow(bx - x2, 2) + pow(by - y2, 2))
        ''' '''if distance < 46:
            return {[x2,y2] : True}
        else:
            return {[x2,y2] : False}''' ''''
        if distance < 46:
            return y2'''

sx = 125
sy = 250
sx2 = 345
sy2 = 320

#game area(main code)
running = True

while running:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    if sy == 250:
        screen.blit(start, (sx, sy))
        screen.blit(start2, (sx2, sy2))
    for event in pg.event.get():
        if event == pg.QUIT:
            running = False
            break
        if event.type == pg.KEYDOWN:
            sy = -1000
            sy2 = -1000
            if event.key == pg.K_LEFT:
                changeinx = -4
            if event.key == pg.K_RIGHT:
                changeinx = 4
            if event.key == pg.K_ESCAPE:
                cnt += 1
                if cnt % 2 != 0:
                    paused = True
                else:
                    paused = False
            '''if sy == -1000:
                if event.key == pg.K_RETURN:
                    bx = x
                    changeinby = -6'''
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                changeinx = 0

    if paused != True:
        if sy == -1000:
            count += 1
            x += changeinx
            by += changeinby
            y2 += 5
            y3 += 5.5
            y4 += 2
            if x <= 0:
                x = 0
            elif x >= 736:
                x = 736
            if y2 >= 580:
                y2 = 0
                x2 = random.randint(0, 200)
            if y3 >= 580:
                y3 = 0
                x3 = random.randint(0, 700)
            if y4 >= 580:
                y4 = 0
                x4 = random.randint(200, 500)
            if y5 >= 580:
                y5 = 0
                x5 = random.randint(500, 700)
            if y6 >= 580:
                y6 = 0
                x6 = random.randint(100, 600)
            if y7 >= 580:
                y7 = 0
                x7 = random.randint(0, 750)
            if y8 >= 580:
                y8 = 0
                x8 = random.randint(0, 800)
            '''if by >= 580:
                bx = x
                by = 450'''
        '''for j in range(1,8):
          posy = position_y[j]
          posx = position_x[j]
          if posy >= 580:
            posy = 0
            posx = random.randint(0,800)'''

        position_x = [x, x2, x3, x4, x5, x6, x7, x8]
        position_y = [y, y2, y3, y4, y5, y6, y7, y8]

        '''position_bx = [bx, x2, x3, x4, x5, x6, x7, x8]
        position_by = [by, y2, y3, y4, y5, y6, y7, y8]'''

        blit(player, (x, y))
        blit(bullet, (bx, by))
        blit(enemy1, (x2, y2))
        if count > 100:
            blit(enemy2, (x3, y3))
        if count > 200:
            blit(asteroid1, (x4, y4))
        if count > 1000:
            y5 += 2
            blit(asteroid2, (x5, y5))
        if count > 1200:
            y6 += 5
            blit(enemy3, (x6, y6))
        if count > 2000:
            y7 += 7
            blit(enemy4, (x7, y7))
        if count > 2500:
            y8 += 9
            blit(enemy5, (x8, y8))

        for i in range(1, len(position_x)):
            posx = position_x[i]
            posy = position_y[i]
            distance2 = distance(x, posx, y, posy)
            distances.append(distance2)

        '''for i in range(1, len(position_bx)):
            posx = position_bx[i]
            posy = position_by[i]
            ty = distance_2(bx, posx, by, posy)
            ty = -200'''

        cond = any(distances)
        if cond == True:
            y = -100
            y2 = -100
            y3 = -100
            y4 = -100
            y5 = -100
            y6 = -100
            y7 = -100
            y8 = -100
            screen.blit(gameover, (200, 250))

        '''if fired == True:
          for i in distances_2:
              for j in i:
                if i[j] == True:
                  j[1] = 0
                  j[0] = random.randint(0, 800)'''

        if sy == -1000:
            if cond == False:
                score += 0.1
                score_final = font2.render("Score : " + str(round(score)),
                                           True, (255, 255, 255))
                screen.blit(score_final, (0, 10))
            else:
                score_final = font2.render("Score : " + str(round(score)),
                                           True, (255, 255, 255))
                screen.blit(score_final, (320, 320))

    else:
        screen.blit(Paused_Screen, (275, 250))
        
    pg.display.update()

#Just copy and paste this in a Python Interpreter
#with pygame installed and run it
#then have fun playing it! 

			
			
