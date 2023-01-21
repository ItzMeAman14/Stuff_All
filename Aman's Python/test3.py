import pygame

white = (255,255,255)
screen = pygame.display.set_mode()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.draw.rect(screen , white, [200, 200,30, 50])
    pygame.display.update()