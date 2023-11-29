import pygame
import random
import math

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
enemyImage = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_enemies = 6

for i in range(num_enemies):
    enemyImage.append(pygame.image.load("gato_foilhao2.png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(100, 150))
    enemyX_change.append(0.2)
    enemyY_change.append(4)

# Bullets 
bulletImage = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 0.7
bullet_state = "ready"  # ready to shoot but cannot be seeing yet

score = 0

def player(x, y):
    screen.blit(playerImage, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImage[i], (x, y))


def bullet(x,y):
    global bullet_state
    bullet_state = "fire"  # now can be seeing
    screen.blit(bulletImage, (x + 16, y + 10))


def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


    

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

    
        # Enemy mov
    for i in range(num_enemies):
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 0.3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 740:
            enemyX_change[i] = -0.3
            enemyY[i] += enemyY_change[i]

        # Collision to kill
        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0, 736)
            enemyY[i] = random.randint(50,150)

        enemy(enemyX[i], enemyY[i], i)

    # Bullet mov and shoot
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    
    player(playerX, playerY)
    pygame.display.update()
