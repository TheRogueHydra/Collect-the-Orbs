#Imports
import pygame
import random
pygame.init()

#Game System Variables
WINDOW_WIDTH = 350
WINDOW_HEIGHT = 600
gameWindow = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Collect the Orbs")
gameIsRunning = True
gameClock = pygame.time.Clock()
gravityModif = 2
text_font = pygame.font.SysFont("Arial",30)
loss_text = text_font.render("Game Over",True,(255,255,255))
loss_textRect = loss_text.get_rect()
gameLost = False

#Game Play Variables
playerScore = 0
playerLocationX = 150
playerLocationY = 350
orbLocationY = 100
deadZonePositionY = 550
deadZonePositionYSet = 550

while gameIsRunning == True:
    scoreText = text_font.render("Charge: "+str(playerScore),True,(255,255,255))
    scoreTextRect = scoreText.get_rect()
    player = pygame.Rect((playerLocationX,playerLocationY),(50,50))
    orbPoint = pygame.Rect((150,orbLocationY),(50,50))
    deadZone = pygame.Rect((0,deadZonePositionY),(350,600-deadZonePositionY))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameIsRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and playerLocationY >= 0:
                playerLocationY -= 75
            if event.key == pygame.K_DOWN and playerLocationY <= 500:
                playerLocationY += 75
            if event.key == pygame.K_x:
                orbLocationY = random.randint(0, 400)

    if playerLocationY <= 500:
        playerLocationY += gravityModif

    #Collision Detection
    if player.colliderect(orbPoint) == True:
        playerScore += 10
        print(playerScore)
        orbLocationY = random.randint(0,400)
        deadZonePositionYSet = random.randint(50,350)

    if player.colliderect(deadZone) == True:
        playerScore -=5

    if deadZonePositionY > deadZonePositionYSet:
        deadZonePositionY -= 1
    elif deadZonePositionY < deadZonePositionYSet:
        deadZonePositionY += 1

    if playerScore < 0:
        gameLost = True

    gameWindow.fill((135,206,235))
    gameWindow.blit(scoreText, scoreTextRect)
    pygame.draw.rect(gameWindow,(255,0,0),deadZone)
    pygame.draw.rect(gameWindow,(255,0,255),orbPoint)
    pygame.draw.rect(gameWindow,(0,255,0),player)
    if gameLost:
        gameWindow.fill((0,0,0))
        gameWindow.blit(loss_text,loss_textRect)
        orbLocationY = 0
        playerLocationY = 10000
        deadZonePositionY = 50000
        deadZonePositionYSet = 50000
    pygame.display.update()
    gameClock.tick(60)