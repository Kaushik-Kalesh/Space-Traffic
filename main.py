import pygame as pg
import math
import random

pg.init()

rotate_img = lambda img:pg.transform.rotate(pg.image.load(img), 180)

#adding images/objects
screen = pg.display.set_mode((800, 580))
pg.display.set_caption('Space Traffic')
player = pg.image.load('./images/spaceship.png')
pg.display.set_icon(player)

#adding fonts
font = pg.font.Font("freesansbold.ttf", 64)
font2 = pg.font.Font("freesansbold.ttf", 32) 

#allocating coordinates and related values
x = 350
y = 450
x1 = random.randint(0, 700)
x2, y1, x3, x4, x5, x6, x7 = [-100] * 7
y2, y3, y4, y5, y6, y7 = [0] * 6
count = 0
score = 0
change_in_x = 0
distances = []
cnt = 0
paused = 0

#related functions
def blit(img, pos):screen.blit(img, pos)

distance = lambda x, x1, y, y1:math.sqrt(math.pow(x - x1, 2) + math.pow(y - y1, 2)) < 46

sx = 125
sy = 250
sx1 = 345
sy1 = 320

#game logic
while True:
    screen.fill((0, 0, 0))
    screen.blit(pg.transform.scale(pg.image.load('./images/spacebg.png'), (800, 580)), (0, 0))
    if sy == 250:
        screen.blit(font.render("SPACE TRAFFIC", True, (255, 255, 255)), (sx, sy))
        screen.blit(font2.render("Press Space to Start", True, (255, 255, 255)), (sx1, sy1))
    for event in pg.event.get():
        if event.type == pg.QUIT: exit()
        if event.type == pg.KEYDOWN:
            sy = -1000
            sy1 = -1000
            if event.key == pg.K_LEFT:change_in_x = -4
            if event.key == pg.K_RIGHT:change_in_x = 4
            if event.key == pg.K_ESCAPE:
                cnt += 1
                paused = cnt % 2 != 0
        if event.type == pg.KEYUP:
            if event.key in (pg.K_LEFT, pg.K_RIGHT):change_in_x = 0

    if paused:screen.blit(font.render("PAUSED", True, (255, 255, 255)), (275, 250))
    else:
        if sy == -1000:
            count += 1
            x += change_in_x
            y1 += 5
            y2 += 5.5
            y3 += 2
            if x <= 0:x = 0
            elif x >= 736:x = 736
            if y1 >= 580:x1, y1 = random.randint(0, 200), 0
            if y2 >= 580:x2, y2 = x, 0
            if y3 >= 580:x3, y3 = random.randint(200, 500), 0
            if y4 >= 580:x4, y4 = random.randint(500, 700), 0
            if y5 >= 580:x5, y5 = x, 0
            if y6 >= 580:x6, y6 = random.randint(0, 750), 0
            if y7 >= 580:x7, y7 = random.randint(0, 800), 0

        position_x = [x, x1, x2, x3, x4, x5, x6, x7]
        position_y = [y, y1, y2, y3, y4, y5, y6, y7]

        blit(player, (x, y))
        blit(rotate_img('./images/enemy1.png'), (x1, y1))
        if count > 100:blit(rotate_img('./images/enemy2.png'), (x2, y2))
        if count > 200:blit(rotate_img('./images/asteroid.png'), (x3, y3))
        if count > 1000:
            y4 += 2
            blit(pg.image.load('./images/asteroid2.png'), (x4, y4))
        if count > 1200:
            y5 += 5
            blit(rotate_img('./images/enemy3.png'), (x5, y5))
        if count > 2000:
            y6 += 7
            blit(rotate_img('./images/enemy4.png'), (x6, y6))
        if count > 2500:
            y7 += 9
            blit(rotate_img('./images/enemy5.png'), (x7, y7))

        for i in range(1, len(position_x)):distances.append(distance(x, position_x[i], y, position_y[i]))

        cond = any(distances)
        if cond:
            y, y1, y2, y3, y4, y5, y6, y7 = [-100] * 8
            screen.blit(font.render("GAME OVER", True, (255, 255, 255)), (200, 250))
            screen.blit(font2.render(f'Score : {round(score)}', True, (255, 255, 255)), (320, 320))     

        if sy == -1000 and not cond:
                score += 0.1
                screen.blit(font2.render(f'Score : {round(score)}', True, (255, 255, 255)), (0, 10))

    pg.display.update()
