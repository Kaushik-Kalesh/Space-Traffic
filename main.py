import pygame as pg
import math
import random

pg.init()

rotate_img = lambda img:pg.transform.rotate(pg.image.load(img), 180)

#adding images/objects
screen = pg.display.set_mode((800, 580))
pg.display.set_caption('Space Invaders')
player = pg.image.load('./images/spaceship.png')
pg.display.set_icon(player)
enemy1 = rotate_img('./images/enemy1.png')
enemy2 = rotate_img('./images/enemy2.png')
enemy3 = rotate_img('./images/enemy3.png')
enemy4 = rotate_img('./images/enemy4.png')
enemy5 = rotate_img('./images/enemy5.png')
asteroid1 = rotate_img('./images/asteroid.png')
asteroid2 = pg.image.load('./images/asteroid2.png')

#adding background, fonts, text
bg = pg.transform.scale(pg.image.load('./images/spacebg.png'), (800, 580))
font = pg.font.Font("freesansbold.ttf", 64)
font2 = pg.font.Font("freesansbold.ttf", 32)
gameover = font.render("GAME OVER", 1, (255, 255, 255))
paused_screen = font.render("PAUSED", 1, (255, 255, 255))
start1 = font.render("SPACE INVADERS", 1, (255, 255, 255))
start2 = font2.render("Press Space to Start", 1, (255, 255, 255))

#allotting coordinates
x1 = 350
y1 = 450
x2 = random.randint(0, 700)
x3, y2, x4, x5, x6, x7, x8 = [-100] * 7
y3, y4, y5, y6, y7, y8 = [0] * 6
count = 0
score = 0
change_in_x = 0

distances = []
cnt = 0
paused = 0

#related functions
def blit(img, pos):screen.blit(img, pos)

distance = lambda x1, x2, y1, y2:math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2)) < 46

sx1 = 125
sy1 = 250
sx2 = 345
sy2 = 320

#game area(main code)
running = 1

while running:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    if sy1 == 250:
        screen.blit(start1, (sx1, sy1))
        screen.blit(start2, (sx2, sy2))
    for event in pg.event.get():
        if event == pg.QUIT:
            running = 0
            break
        if event.type == pg.KEYDOWN:
            sy1 = -1000
            sy2 = -1000
            if event.key == pg.K_LEFT:change_in_x = -4
            if event.key == pg.K_RIGHT:change_in_x = 4
            if event.key == pg.K_ESCAPE:
                cnt += 1
                paused = cnt % 2 != 0
        if event.type == pg.KEYUP:
            if event.key in (pg.K_LEFT, pg.K_RIGHT):change_in_x = 0

    if paused:screen.blit(paused_screen, (275, 250))
    else:
        if sy1 == -1000:
            count += 1
            x1 += change_in_x
            y2 += 5
            y3 += 5.5
            y4 += 2
            if x1 <= 0:x1 = 0
            elif x1 >= 736:x1 = 736
            if y2 >= 580:x2, y2 = random.randint(0, 200), 0
            if y3 >= 580:x3, y3 = random.randint(0, 700), 0
            if y4 >= 580:x4, y4 = random.randint(200, 500), 0
            if y5 >= 580:x5, y5 = random.randint(500, 700), 0
            if y6 >= 580:x6, y6 = random.randint(100, 600), 0
            if y7 >= 580:x7, y7 = random.randint(0, 750), 0
            if y8 >= 580:x8, y8 = random.randint(0, 800), 0

        position_x = [x1, x2, x3, x4, x5, x6, x7, x8]
        position_y = [y1, y2, y3, y4, y5, y6, y7, y8]

        blit(player, (x1, y1))

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

        for i in range(1, len(position_x)):distances.append(distance(x1, position_x[i], y1, position_y[i]))

        cond = any(distances)
        if cond:
            y1, y2, y3, y4, y5, y6, y7, y8 = [-100] * 8
            screen.blit(gameover, (200, 250))

        if sy1 == -1000:
            if cond:screen.blit(font2.render(f'Score : {round(score)}', 1, (255, 255, 255)), (320, 320))
            else:
                score += 0.1
                screen.blit(font2.render(f'Score : {round(score)}', 1, (255, 255, 255)), (0, 10))

    pg.display.update()
