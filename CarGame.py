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

game = True

while game:

    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    pygame.display.update()


