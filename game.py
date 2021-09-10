import pygame
import random
import math

pygame.init()
# Screen
screen = pygame.display.set_mode([800, 600])
# Background
background = pygame.image.load("Images/background.png").convert()
# Title and Icon
pygame.display.set_caption("Pony TD")
icon = pygame.image.load("Images/icon.png")
pygame.display.set_icon(icon)
# Towers
castleImg = pygame.image.load("Images/testcastle.png")
smallcastleImg = pygame.image.load("Images/smallcastle.png")
# Player
playerImg = pygame.image.load("Images/unicorn.png")
playerX = 356
playerY = 400
playerX_change = 0
# Zombie
zombieImg = []
zombieX = []
zombieY = []
zombieX_change = []
zombieY_change = []
num_of_zombies = 6
for i in range(num_of_zombies):
    zombieImg.append(pygame.image.load("Images/zombie.png"))
    zombieX.append(random.randint(0, 736))
    zombieY.append(random.randint(0, 100))
    zombieX_change.append(0.9)
    zombieY_change.append(30)
# Bullet
bulletImg = pygame.image.load("Images/bullet.png")
bulletX = 0
bulletY = 400
bulletX_change = 0
bulletY_change = 1.5
bullet_state = "ready"
# Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10


# Functions
def game_over_text():
    over_text = font.render("Game Over", True, (255, 0, 0))
    screen.blit(over_text, (300, 300))

def show_score(x, y):
    score = font.render("Score :" + str(score_value), True, (110, 36, 87))
    screen.blit(score, (x, y))

def player(x, y):
    screen.blit(playerImg, (playerX, playerY))
def zombie(x, y, i):
    screen.blit(zombieImg[i], (x, y))
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))
def isCollision(zombieX, zombieY, bulletX, bulletY):
    distance = math.sqrt((math.pow(zombieX - bulletX, 2)) + (math.pow(zombieY - bulletY, 2)))
    if distance < 35:
        return True
    else:
        return False

running = True
while running:

    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -1.2
            if event.key == pygame.K_d:
                playerX_change = 1.2
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

    # Player Movement
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    # Enemy Movement
    for i in range(num_of_zombies):
        zombieX[i] += zombieX_change[i]
        if zombieX[i] <= 0:
            zombieX_change[i] = 0.9
            zombieY[i] += zombieY_change[i]
        elif zombieX[i] >= 736:
            zombieX_change[i] = -0.9
            zombieY[i] += zombieY_change[i]
        if zombieY[i] >= 390:
            game_over_text()

        # Collision
        collision = isCollision(zombieX[i], zombieY[i], bulletX, bulletY)
        if collision:
            bulletY = 400
            bullet_state = "ready"
            score_value += 1
            zombieX[i] = random.randint(0, 768)
            zombieY[i] = random.randint(0, 150)

        zombie(zombieX[i], zombieY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    player(playerX, playerY)
    screen.blit(castleImg, (334, 472))
    screen.blit(smallcastleImg, (0, 534))
    screen.blit(smallcastleImg, (64, 534))
    screen.blit(smallcastleImg, (128, 534))
    screen.blit(smallcastleImg, (736, 534))
    screen.blit(smallcastleImg, (672, 534))
    screen.blit(smallcastleImg, (608, 534))
    screen.blit(smallcastleImg, (544, 534))
    screen.blit(smallcastleImg, (480, 534))
    screen.blit(smallcastleImg, (192, 534))
    screen.blit(smallcastleImg, (256, 534))

    show_score(textX, textY)

    pygame.display.update()
