import pygame
import random

# Initialize the pygame

pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background image
background = pygame.image.load("background.png")

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# Player
playerImage = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0 

# Enemy
enemyImage = pygame.image.load("gato_foilhao2.png")
enemyX = random.randint(0,800)
enemyY = random.randint(100, 150)
enemyX_change = 0.3
enemyY_change = 5

# Bullets 
bulletImage = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.7
bullet_state = "ready"  # ready to shoot but cannot be seeing yet



def player(x, y):
    screen.blit(playerImage, (x, y))


def enemy(x, y):
    screen.blit(enemyImage, (x, y))


def bullet(x,y):
    global bullet_state
    bullet_state = "fire"  # now can be seeing
    screen.blit(bulletImage, (x, y))


# game loop
running = True
while running:
    screen.fill((0, 0, 0))

    screen.blit(background, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # checking if any keystroke is being pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.3
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletX = playerX
                    bullet(bulletX, bulletY)
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 740:
        playerX = 740

    # Bullet mov
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    # Enemy mov
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 740:
        enemyX_change = -0.3
        enemyY += enemyY_change


    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
