import pygame

black = (0, 0, 0)
green = (0, 128, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)

car = pygame.image.load('car2.png')
cone = pygame.image.load('traffic_cone.png')

x = 85
y = 470
width = 64
height = 64
vel = 5
coney = 15

def draw_screen():
    screen.fill(yellow)
    pygame.draw.rect(screen, green, (0, 0, 75, 600))
    pygame.draw.rect(screen, green, (425, 0, 75, 600))
    pygame.draw.rect(screen, black, (80, 0, 110, 600))
    pygame.draw.rect(screen, black, (195, 0, 110, 600))
    pygame.draw.rect(screen, black, (310, 0, 110, 600))
    screen.blit(car, (x, y))
    screen.blit(cone, (95, coney))
    screen.blit(cone, (215, coney))
    screen.blit(cone, (325, coney))
    pygame.display.update()

def execute_game():

    global x
    global y
    global coney
    global vel
    game = True

    while game:

        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x >= 100:
            x -= 117

        if keys[pygame.K_RIGHT] and x < 300:
            x += 117

        if coney > 500:
            coney = 15
        else:
            coney += vel

        draw_screen()


def game_init():
    global size
    global screen
    pygame.init()
    size = (500, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Car Game")


def main():
    game_init()
    execute_game()
    pygame.quit()

if __name__ == '__main__':
    main()



