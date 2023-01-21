import pygame
import random
import time
pygame.init()

screen = pygame.display.set_mode((1500,1000))
clock = pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
spaceship = pygame.image.load('spaceship.png')
background = pygame.image.load('space(bg).jpg')
big_enemy_ship = pygame.image.load('enemy.png')
enemy_ship = pygame.image.load('enemy1.png')
bullet = pygame.image.load('bullet.png')
spaceship = pygame.transform.scale(spaceship, (160, 180))
big_enemy_ship = pygame.transform.scale(big_enemy_ship, (150, 170))
enemy_ship = pygame.transform.scale(enemy_ship, (180, 120))
bullet = pygame.transform.scale(bullet, (70, 60))


def intro():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(white)
        message(50 , 100, 300 ,"Start", black)
        button(300, 300 ,"Hello")
        pygame.display.update()

def big_enemy(x_big, y_big):
    screen.blit(big_enemy_ship, (x_big,y_big))


def enemy(x_en, y_en):
    screen.blit(enemy_ship, (x_en,y_en))

def spaceshuttle(x_space, y_space):
    screen.blit(spaceship, (x_space,y_space))

def bullet_func(x_bullet, y_bullet):
    screen.blit(bullet, (x_bullet,y_bullet))


def message(size, x_mess, y_mess, mess, color):
    font = pygame.font.SysFont(None, size)
    render = font.render(mess,True, color)
    screen.blit(render, (x_mess, y_mess))    



def button(x_pos_b, y_pos_b,mess_b):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pygame.draw.rect(screen, black , [x_pos_b, y_pos_b, 100, 30])
    message(30 , x_pos_b+20, y_pos_b+5, mess_b, white)
    if x_pos_b<mouse[0]<x_pos_b+100 and y_pos_b<mouse[1]<y_pos_b+30:
        if click == (True, False, False) and mess_b == "Hello":
            game_loop() 


def game_loop():
    x = 100
    y = 600
    fires = 0
    x_space = 0
    y_space = 0
    bullet_fire = False
    x_bullet = x + 47
    y_bullet = y + 60
    x_big = random.randrange(100, 1000)
    x_en = random.randrange(100, 1000)
    y_en = random.randrange(100 , 500)
    y_big = random.randrange(100 , 500)
    game = False
    while game == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_space += 5
                elif event.key == pygame.K_DOWN:
                    y_space -= 5
                elif event.key == pygame.K_RIGHT:
                    x_space -= 5
                elif event.key == pygame.K_LEFT:
                    x_space += 5
                elif event.key == pygame.K_SPACE:
                    bullet_fire = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    x_space = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_space = 0
        
        

        x = x - x_space
        y = y - y_space
        if fires >= 0 and y_bullet<=10:
            x_bullet = x + 47
            y_bullet = y 
            bullet_fire = False


        if y_big == 600:
            x_big = random.randrange(100, 1000)
            y_big = random.randrange(100 , 500)
        if y_en == 600:
            x_en = random.randrange(100, 1000)
            y_en = random.randrange(100 , 500)
        if x <= 0:
            x = 0
        elif x >= 1340:
            x = 1340
        if y <= 0:
            y = 0
        elif y >= 670:
            y = 670
        y_big += 1
        y_en += 1
        y_bullet -= 3
        screen.blit(background, (0,0))
        spaceshuttle(x, y)
        enemy(x_en, y_en)
        big_enemy(x_big, y_big)

        if bullet_fire == True:
            bullet_func(x_bullet, y_bullet)
            fires += 1
        pygame.display.update()


intro()