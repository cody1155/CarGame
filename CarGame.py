import pygame
import random
vel = 5
coney = 15

black = (0, 0, 0)
green = (0, 128, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)

car_image = pygame.image.load('car2.png')
cone_image = pygame.image.load('traffic_cone.png')


vel = 5
coney = 15


class player(object):
    def __init__ (self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.hitbox = (self.x + 8, self.y - 3, self.width + 12, self.height+ 40)

    def draw(self, screen):
        screen.blit(car_image, (self.x, self.y))
        self.hitbox = (self.x + 8, self.y - 3, self.width + 12, self.height + 40)
        pygame.draw.rect(screen, (255, 0, 0,), self.hitbox, 2)

class obstacle(object):
    def __init__(self, x, y, width, height, velocity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity
        self.hitbox = (self.x + 1, self.y - 2, self.width + 8, self.height+ 16)

    def draw(self, screen):
        screen.blit(cone_image, (self.x, self.y))
        self.hitbox = (self.x + 1, self.y - 2, self.width + 8, self.height+ 16)
        pygame.draw.rect(screen, (255, 0, 0,), self.hitbox, 2)
        if self.y > 580:
            self.y = -80    
        else:
            self.y += self.velocity





def draw_screen():
    screen.fill(yellow)
    pygame.draw.rect(screen, green, (0, 0, 75, 600))
    pygame.draw.rect(screen, green, (425, 0, 75, 600))
    pygame.draw.rect(screen, black, (80, 0, 110, 600))
    pygame.draw.rect(screen, black, (195, 0, 110, 600))
    pygame.draw.rect(screen, black, (310, 0, 110, 600))
    car.draw(screen)
    cone.draw(screen)
    pygame.display.update()


def execute_game():

    global vel
    global coney

    game = True
    while game:

        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and car.x >= 100:
            car.x -= 117

        if keys[pygame.K_RIGHT] and car.x < 300:
            car.x += 117

        draw_screen()


def game_init():
    global size
    global screen
    global car
    global cone
    pygame.init()
    size = (500, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Car Game")
    car = player(85, 470, 64, 64)
    cone = obstacle(95, -80, 64, 64, 10)


def main():
    game_init()
    execute_game()
    pygame.quit()

if __name__ == '__main__':
    main()



