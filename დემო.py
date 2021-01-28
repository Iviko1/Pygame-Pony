import pygame

pygame.init()

screen = pygame.display.set_mode([800, 600])

zombieImg = pygame.image.load("Images/zombie.png")

running = True

while running:
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(zombieImg, (300, 400))
    pygame.display.update()