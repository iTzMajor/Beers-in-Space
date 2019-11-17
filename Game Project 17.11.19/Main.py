import pygame
import random
import math

# intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800,600))

#Background
background = pygame.image.load("background.jpg")

#title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

#Player Settings
playerImg = pygame.image.load("player.png")
playerX = 370
playerY = 480
playerX_change = 0

#Enemy Settings
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0,735)
enemyY = random.randint(50,150)
enemyX_change = 0.3
enemyY_change = 40

#Bullet Settings
#ready - you can;t see the bullet is currently moving
#fire - the bullet is currently moving
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

score = 0

def player(x,y):
    screen.blit(playerImg,(x, y))

def enemy(x,y):
    screen.blit(enemyImg,(x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))
    if distance < 27:
        return True
    else:
        return False


# GAME LOOP 
running = True
while running:
    
    # RGB = Red, Blue, Green
    screen.fill((0, 0, 0))
    #background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    # Get the currect x cordinate of spaceship
                    bulletX = playerX
                    fire_bullet(playerX,bulletY)



                #take down lines 43-45 for no breaks mode 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    


#fix right side // fix: playerIMG size is 64px therefore 64-800=736 
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736


# check the border, NO MEHICO AMIGO 
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    #bullet movement
    if bulletY <=0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    # collision
    collision = isCollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY = 480
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0,735)
        enemyY = random.randint(50,150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)

    pygame.display.update()
