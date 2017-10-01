import pygame
import random
import time
# REQUIRES FILES:
# SnakeHead.png
# Apple.png
# Icon.png
# Highscore.dat
#
#
#
#
#
#

pygame.init()


# predefined

win_width = 800
win_height = 600

icon = pygame.image.load('Icon.png')

gameDisplay = pygame.display.set_mode((win_width, win_height))
#outlineDisplay = pygame.display.set_mode((win_width-15, win_height-15))
pygame.display.set_caption('Snake Game')
pygame.display.set_icon(icon)

# Code
pygame.display.update()

with open('Highscore.dat', 'r') as data:
    highscore = data.read()

def gameloop():
    # Mandatory functions

    def draw_apple():
        apple_x = int(random.randrange(0, win_width - apple_width))  # / apple_width) * apple_width
        apple_y = int(random.randrange(0, win_height - apple_height))  # / apple_height) * apple_height

        return apple_x, apple_y

    # Predefined
    gameExit = False
    gameOver = False

    img = pygame.image.load('SnakeHead.png')
    appleimg = pygame.image.load('Apple.png')  # Best to be 32 x 32

    snakelist = []
    snake_score = 1

    real_score = 0

    border_thickness = 3

    apple_width = 30
    apple_height = 30

    apple_x, apple_y = draw_apple()

    snake_width = 20
    snake_length = 20
    # Commented as the collision of apple boundaries need not be a multiple of snake width

    lead_x = win_width / 2
    lead_y = win_height / 2
    lead_x_change = 10
    lead_y_change = 0

    direction = 'right'

    max_change = 10
    min_change = -10

    difficulty = 10

    fps = 20
    clock = pygame.time.Clock()

    smallfont = pygame.font.SysFont('comicsansms', 30)
    medfont = pygame.font.SysFont('comicsansms', 50)
    bigfont = pygame.font.SysFont('comicsansms', 80)

    # Colours
    white = (255, 255, 255)
    black = (0, 0, 0)

    red = (255, 0, 0)
    green = (85,107,47)
    blue = (0, 0, 175)

    magenta = (255, 0, 255)
    yellow = (255, 255, 0)
    cyan = (0, 115, 115)

# functions


    def display_msg(msg, col=white, y_displace=0, size= 'small'): # colour will be background
        #clean(gameDisplay, col)
        textSurface, textRect = text_object(msg, col, size)
        textRect.center = win_width/2, (win_height/2) + y_displace
        gameDisplay.blit(textSurface, textRect)

    def text_object(text, col, size):
        if size == 'small':
            textSurface = smallfont.render(text, True, col)

        elif size == 'medium':
            textSurface = medfont.render(text, True, col)

        elif size == 'big':
            textSurface = bigfont.render(text, True, col)

        return textSurface, textSurface.get_rect()

    def clean(display, col):
        display.fill(col)

    def draw_snake(snakelist, snake_width, snake_length):

        if direction == 'right':
            head = pygame.transform.rotate(img, 270)
        elif direction == 'left':
            head = pygame.transform.rotate(img, 90)
        elif direction == 'up':
            head = pygame.transform.rotate(img, 0)
        elif direction == 'down':
            head = pygame.transform.rotate(img, 180)


        gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
        for XnY in snakelist[:-2]:
            pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], snake_width, snake_length])

    def pause():
        p_pressed = True
        while p_pressed:
            clean(gameDisplay, cyan)
            display_msg('The Game is PAUSED', white, y_displace=-50, size='medium')
            display_msg('Press <P> to UNPAUSE game.',y_displace=50,  size='small')
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        p_pressed = False
                    elif event.key == pygame.K_q:
                        p_pressed = True
                        pygame.quit()
                        quit()
                elif event.type == pygame.QUIT:
                    p_pressed = True
                    pygame.quit()
                    quit()
    def pause_no_clear():
        l_pressed = True
        while l_pressed:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_l:
                        l_pressed = False
                    elif event.key == pygame.K_q:
                        l_pressed = True
                        pygame.quit()
                        quit()
                elif event.type == pygame.QUIT:
                    l_pressed = True
                    pygame.quit()
                    quit()

    def score(score):

        global highscore

        if score > int(highscore) and score < 71:
            with open('Highscore.dat', 'r+') as data:
                data.truncate()
            with open('Highscore.dat', 'w') as data:
                highscore = data.write(str(real_score))
            text = smallfont.render('Highscore: '+str(real_score), True, magenta)
            gameDisplay.blit(text, [win_width-260, win_height-550])
            textSurface, textRect = text_object('Score: '+str(score), magenta, 'small')
            textRect.center = (win_width*6)/8, (win_height*1)/20
            gameDisplay.blit(textSurface, textRect)

        else:
            data = open('Highscore.dat', 'r')
            highscore = data.read()
            text = smallfont.render('Highscore: ' + str(highscore), True, magenta)
            gameDisplay.blit(text, [win_width - 260, win_height - 550])
            textSurface, textRect = text_object('Score: ' + str(score), magenta, 'small')
            textRect.center = (win_width * 6) / 8, (win_height * 1) / 20
            gameDisplay.blit(textSurface, textRect)
            data.close()


    def start():
        intro = True

        while intro:
            clean(gameDisplay, white)
            display_msg('Welcome to Snake Game!', col=green, y_displace=-130, size='medium')
            display_msg('The objective is to eat RED apples', col=red, y_displace=-50)
            display_msg('The more apples you eat, the longer you get!', col=red, y_displace=-10)
            display_msg('If you run into the edges you die!', col=red, y_displace=30)
            display_msg('<Q> - Quit', col=red, y_displace=70)
            display_msg('<P> - Pause', col=red, y_displace=110)
            display_msg('<L> - Static Pause', col=red, y_displace=150)
            display_msg('Press <S> to start game', col=magenta, y_displace=210)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        intro = False
                    elif event.key == pygame.K_q:
                        intro = True
                        pygame.quit()
                        quit()
                elif event.type == pygame.QUIT:
                    intro = True
                    pygame.quit()
                    quit()

            clock.tick(5)
            pygame.display.update()
    start()
    while not gameExit:

        # Border
        gameDisplay.fill(red)
        pygame.draw.rect(gameDisplay,
                         white,
                         [border_thickness,
                          border_thickness,
                          win_width-(2*border_thickness),
                          win_height-(2*border_thickness)
                          ]
                         )



        while gameOver == True:
            clean(gameDisplay, yellow)
            data = open('Highscore.dat', 'r+')
            highscore = data.read()
            data.close()
            display_msg('Game Over!', red, -140, size='big')
            if real_score > 75:
                display_msg('I hope you\'re happy, CHEATER.', red, -10, size='medium')
                display_msg('Your \'hacked\' score was: '+ str(real_score), red, 60, size='small')
                display_msg('The highscore is: '+ str(highscore), red, 90, size='small')
                display_msg('Press <R> to replay or <Q> to quit!', red, 170, size='medium')
            elif int(highscore) > 75:
            #     display_msg('I hope you\'re happy, CHEATER.', red, -10, size='medium')
            #     display_msg('You \'hacked\' score was: '+ str(real_score), red, 60, size='small')
            #     display_msg('The \'hacked\' highscore is: '+ str(highscore), red, 90, size='small')
            #     display_msg('Press <R> to replay or <Q> to quit!', red, 170, size='medium')
                time.sleep(3)
                clean(gameDisplay, yellow)
                display_msg("The saves are being reset in 3 seconds.", red, size='small')
                pygame.display.update()
                time.sleep(1)
                clean(gameDisplay, yellow)
                display_msg("The saves are being reset in 2 seconds.", red, size='small')
                pygame.display.update()
                time.sleep(1)
                clean(gameDisplay, yellow)
                display_msg("The saves are being reset in 1 second.", red, size='small')
                pygame.display.update()
                time.sleep(1)
                data = open('Highscore.dat', 'r+')
                data.truncate()
                data.close()
                data = open('Highscore.dat', 'w')
                data.write('0')
                data.close()
            else:
                display_msg('Well Done, your end score was: '+ str(real_score), red, 10, size='small')
                display_msg('The highscore is: '+ str(highscore), red, 60, size='small')
                display_msg('Press <R> to replay or <Q> to quit!', red, 130, size='medium')

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    elif event.key == pygame.K_r:
                        gameloop()
                elif event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    gameExit = True
                    gameOver = False

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            elif event.type == pygame.KEYDOWN : # Pressed
                if event.key == pygame.K_LEFT:
                    lead_x_change -= difficulty # Move by 10 left <-
                    lead_y_change = 0
                    direction = 'left'
                elif event.key == pygame.K_RIGHT:
                    lead_x_change += difficulty # move by 10 right ->
                    lead_y_change = 0
                    direction = 'right'
                elif event.key == pygame.K_UP:
                    lead_y_change -= difficulty # Move by 10 up ^
                    lead_x_change = 0
                    direction = 'up'
                elif event.key == pygame.K_DOWN:
                    lead_y_change += difficulty # move by 10 down √
                    lead_x_change = 0
                    direction = 'down'
                elif event.key == pygame.K_p:
                    pause()
                elif event.key == pygame.K_q:
                    gameOver = True
                elif event.key == pygame.K_l:
                    pause_no_clear()
                elif event.key == pygame.K_8:
                    real_score = 1000

    # logicr
        lead_x += lead_x_change
        lead_y += lead_y_change

        if lead_x >= win_width-snake_width or lead_x <= 0 or lead_y >= win_height-snake_length or lead_y <= 0:
            gameOver = True

        if lead_x_change >= max_change:
            lead_x_change = max_change
        elif lead_x_change <= min_change:
            lead_x_change = min_change
        elif lead_y_change >= max_change:
            lead_y_change = max_change
        elif lead_y_change <= min_change:
            lead_y_change = min_change

        if len(snakelist) > snake_score:
            del snakelist[0]

        for eachSegement in snakelist[:-1]:
            if eachSegement == snakehead:
                gameOver = True

    # rendering
        #clean(outlineDisplay, black)

        #apple
        #pygame.draw.rect(gameDisplay, red, [apple_x, apple_y, apple_width, apple_height])
        gameDisplay.blit(appleimg, (apple_x, apple_y))
        #snake
        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        draw_snake(snakelist, snake_width, snake_length)


        # so users sees after crash
        # V 1.0
        #     if lead_x == apple_x and lead_y == apple_y:
        #         apple_x = int(random.randrange(0, win_width - apple_width) / apple_width) * apple_width
        #         apple_y = int(random.randrange(0, win_height - apple_height) / apple_height) * apple_height
        #         snake_score += 2
        # This code fixes the collision detection
        #V 2.0
        # if lead_x >= apple_x and lead_x <= apple_x+apple_width:
        #     if lead_y >= apple_y and lead_y <= apple_y+apple_height:
        #         apple_x = int(random.randrange(0, win_width - apple_width)) # / apple_width) * apple_width
        #         apple_y = int(random.randrange(0, win_height - apple_height)) # / apple_height) * apple_height
        #         snake_score += 2
        #This code perfects the crossover / collision ( right side fixed) and apple function fixed
        #V 3.0
        if lead_x > apple_x and lead_x < apple_x + apple_width or lead_x + snake_width > apple_x and lead_x + snake_width < apple_x+apple_width:
            if lead_y > apple_y and lead_y < apple_y + apple_height or lead_y + snake_length > apple_y and lead_y < apple_y + apple_height:
                apple_x, apple_y = draw_apple()
                snake_score += 2
                real_score += 1

        if real_score > 9:
            fps = 21
        elif real_score > 19:
            fps = 28
        elif real_score > 29:
            fps = 35
        elif real_score > 39:
            fps = 37
        elif real_score > 49:
            fps = 37
        elif real_score > 59:
            fps = 39
        elif real_score > 69:
            fps = 61
        elif real_score > 79:
            fps += 1
        elif real_score > 89:
            fps += 1
        elif real_score > 99:
            fps += 100
        score(real_score)

        # FPS
        clock.tick(fps)
        # Render to screen
        pygame.display.update()


    pygame.quit()
    quit()



gameloop()
