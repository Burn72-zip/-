import pygame

pygame.init()
win = pygame.display.set_mode((1100, 650))
pygame.display.update()

pygame.display.set_caption("xam ispep")

walkRight = [pygame.image.load('kiss.png')]

walkLeft = [pygame.image.load('kiss.png')]

playerStanb = pygame.image.load('kiss.png')

x = 50
y = 575
width = 60
heiht = 71
speed = 15

isJupm = False
jumpCount = 10

left = False
right = False
animCount = 0

run = True
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed 
    if keys[pygame.K_RIGHT] and x < 1100 - width - 5:
        x += speed
    if not(isJupm):
        if keys[pygame.K_SPACE]:
            isJupm = True
    else:
        if jumpCount >= -10:
            if jumpCount < 0:
                y += (jumpCount ** 2) / 2
            else:
                y -= (jumpCount **2) / 2
            jumpCount -= 1
        else:
            isJupm = False
            jumpCount = 10

    win.fill((0,0,0))

    pygame.draw.rect(win, (0,0,255), (x, y, width, heiht))
    pygame.display.update()

pygame.quit()            