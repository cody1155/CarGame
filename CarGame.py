import pygame

pygame.init()
size = (500, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Game")

black = (0, 0, 0)
green = (0, 128, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)

screen.fill(yellow)
pygame.draw.rect(screen, green, (0, 0, 75, 600))
pygame.draw.rect(screen, green, (425, 0, 75, 600))
pygame.draw.rect(screen, black, (80, 0, 110, 600))
pygame.draw.rect(screen, black, (195, 0, 110, 600))
pygame.draw.rect(screen, black, (310, 0, 110, 600))

x = 0
y = 0
width = 64
height = 64
vel = 5

game = True

while game:
    screen.fill(yellow)
    pygame.draw.rect(screen, green, (0, 0, 75, 600))
    pygame.draw.rect(screen, green, (425, 0, 75, 600))
    pygame.draw.rect(screen, black, (80, 0, 110, 600))
    pygame.draw.rect(screen, black, (195, 0, 110, 600))
    pygame.draw.rect(screen, black, (310, 0, 110, 600))

    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x -= vel

    if keys[pygame.K_RIGHT] and x < 500 - width - vel:
        x += vel

    if keys[pygame.K_UP] and y > 0:
        y -= vel

    if keys[pygame.K_DOWN] and y < 600 - height - vel:
        y += vel

    pygame.draw.rect(screen, red, (x, y, width, height))
    pygame.display.update()


