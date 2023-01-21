import pygame
import random
import time

pygame.mixer.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()


scr = 0
velocity = 0
roadx = 0
roady = 0
display = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
grey = (100,100,100)
purple = (255,0,255)
black = (0,0,0)
light_green = (0,230,0)
introbg = pygame.image.load("road.jpg")
background = pygame.image.load("bg(intro).jpg")
car_img = pygame.image.load("car.png")
enemy_img = pygame.image.load("enemy_car.png")
score_img = pygame.image.load("score(bg).jpg")
enemy_img = pygame.transform.scale(enemy_img,(270,200))
car_img = pygame.transform.scale(car_img,(270,200))
introsd = pygame.mixer.Sound('intro.mp3')
ingame = pygame.mixer.Sound('ingame.mp3')
crash = pygame.mixer.Sound('crash.mp3')
start = pygame.mixer.Sound('crash.mp3')

def game_intro():
    global scr
    scr = 0
    intro = False
    while intro == False:
        pygame.mixer.Sound.stop(crash)
        pygame.mixer.Sound.play(introsd)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.blit(background, (0,0))
        button(300, 300, "START")
        button(700, 300, "QUIT")
        message(80 , "Welcome to Impossible 50", 100 , 30, white)
        pygame.display.update()

def thank():
    thank1 = False
    while thank1 == False:
        # pygame.mixer.Sound.stop(crash)
        # pygame.mixer.Sound.play(introsd)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        # display.blit(background, (0,0))
        display.fill(grey)
        message(120 , "Thank You For Playing", 80 , 150, black)
        pygame.display.update()
        time.sleep(1)
        pygame.quit()
        quit()


def score_count():
    score_screen = False
    while score_screen == False:
        display.blit(score_img, (0,0))
        message(150 , "Your Score:"+ str(scr), 170, 330, white)
        button(250 , 500 , "Play Again")
        button(500 , 500 , "QUIT")
        pygame.mixer.Sound.stop(crash)
        # pygame.mixer.Sound.play(introsd)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                score_screen = True
            
        pygame.display.update()

def message(size, mess, x_pos, y_pos, color):
    font = pygame.font.SysFont(None, size)
    render = font.render(mess , True, color)
    display.blit(render, (x_pos, y_pos))

def score(scr):
    font = pygame.font.SysFont(None, 50)
    render = font.render("Score:"+str(scr), True, white)
    display.blit(render, (70, 60))


def enemy_car(x,y):
    display.blit(enemy_img,(x,y))
    
def car_crash(x_r,x,y_r,y):
    global scr
    if x_r<x<x_r+80 and y_r<y+120<y_r+162  or x_r<x+80<x_r+80 and y_r<y+120<y_r+162:
        pygame.mixer.Sound.stop(ingame)
        pygame.mixer.Sound.play(crash)
        message(100,"Crashed",300, 300, red)
        pygame.display.update()
        time.sleep(1)
        score_count()
        game_intro()

def car(x,y):
    global scr
    display.blit(car_img,(x,y))
    if 0<x<67 or 1000<x+370 or 0<y<20 or 1000<y+350:
        message(180,"Game Over",160, 300, red)
        pygame.mixer.Sound.stop(ingame)
        pygame.mixer.Sound.play(crash)
        pygame.display.update()
        clock.tick(0.70)
        score_count()


def button(x_button, y_button,mess_b):
    global scr
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    isHovering = (mouse[0]>x_button and mouse[0]<x_button+100) and (mouse[1]>y_button and mouse[1]<y_button+30)
    if isHovering:
        pygame.draw.rect(display, black, [x_button, y_button, 100, 30])
        message(30,mess_b, x_button, y_button, white)
    else:
        pygame.draw.rect(display, black, [x_button, y_button, 100, 30])
        message(30,mess_b, x_button, y_button, white)
    # print(mouse)
    # print(click)
    if x_button<mouse[0]<x_button+100 and y_button<mouse[1]<y_button+30:
        pygame.draw.rect(display, grey, [x_button, y_button, 100, 30])
        if click==(True,False,False) and mess_b == "START":
            pygame.mixer.Sound.play(start)
            pygame.mixer.Sound.set_volume(start,10.0)
            pygame.mixer.Sound.stop(introsd)
            ready()
        elif click == (True, False, False) and mess_b == "Play Again":
            ready()
        elif click==(True,False,False) and mess_b == "QUIT":
            pygame.mixer.Sound.stop(ingame)
            pygame.mixer.Sound.play(introsd)
            scr = 0
            thank()
    # pygame.display.update()

def ready():
    x = 350
    y = 600
    t = 0 
    exit_to_intro = False
    while exit_to_intro == False:
        display.blit(introbg,(0,0))
        car(x,y)
        pygame.mixer.Sound.play(ingame)
        if t == 0:
            message(150, "Ready!", 350, 300, red)
            pygame.display.update()
            clock.tick(0.5)
            t += 2
        if t == 2:
            display.blit(introbg,(0,0))
            car(x,y)
            message(150, "Set!", 350, 300, red)
            pygame.display.update()
            clock.tick(0.5)
            t += 2
        if t == 4:
            display.blit(introbg,(0,0))
            car(x,y)
            message(150, "Go!", 350, 300, red)
            pygame.display.update()
            clock.tick(0.5)
            t += 2
        if t == 6:
            game_loop()
            t += 4
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_to_intro = True

        # game_loop()
        pygame.display.update()
    # clock.tick(0.1)


def game_loop():
    global scr
    global velocity
    global roadx
    global roady
    scr = 0
    x = 350
    x_r = random.randrange(100, 600)
    y = 600
    y_r = 0
    x_change = 0
    y_change = 0
    velocity = 10
    game_over = False
    while game_over == False:
        pygame.mixer.Sound.play(ingame)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                scr = 0
                pygame.mixer.Sound.stop(ingame)
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change =+ 10
                elif event.key == pygame.K_RIGHT:
                    x_change =- 10
                elif event.key == pygame.K_UP:
                    y_change =+ 10
                elif event.key == pygame.K_DOWN:
                    y_change =- 10
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change=0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    y_change=0


        roady = roady + velocity

        if roady == 1000:
            roady = 0

        display.blit(introbg,(roadx,roady - 1000))
        display.blit(introbg,(roadx,roady))
        car(x,y)
        enemy_car(x_r,y_r)
        car_crash(x_r,x,y_r,y)
        score(scr)

        y_r+=10

        if y_r>1000:
            scr +=1
            x_r = random.randrange(100,600)
            y_r = 0
        if 3<scr<40:
            y_r += 5
        if scr > 40:
            y_r += 10

        x = x - x_change
        y = y - y_change
        clock.tick(50)
        pygame.display.update()

game_intro()
pygame.quit()
quit()