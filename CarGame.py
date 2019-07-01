import pygame
import random


pygame.init()
size = (500, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Car Game")


black = (0, 0, 0)
green = (0, 128, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)



car_image = pygame.image.load('car2.png')
cone_image = pygame.image.load('traffic_cone.png')

'''hollow_heart_image = pygame.image.load('hollow_heart.png')
full_heart_image = pygame.image.load('full_heart.png')


class life(object):
    def __init__(self, x, y, minus, lives):
        self.x = y
        self.y = y
        self.minus = True
        self.lives = 3

    def draw(self, screen):
        if self.minus == True:
            screen.blit(full_heart_image, (self.x + 17, self.y + 17))
        screen.blit(hollow_heart_image, (self.x, self.y))'''
        

class player(object):
    def __init__ (self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.collide = True
        self.hitbox = (self.x + 8, self.y - 3, self.width + 12, self.height+ 40)
        self.score = 0

    def draw(self, screen):
        screen.blit(car_image, (self.x, self.y))
        self.hitbox = (self.x + 8, self.y - 3, self.width + 12, self.height + 40)
        pygame.draw.rect(screen, (255, 0, 0,), self.hitbox, 2)

    def hit(self):
        print("hit")


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
        self.hitbox = (self.x - 2, self.y - 2, self.width + 8, self.height+ 16)
        pygame.draw.rect(screen, (255, 0, 0,), self.hitbox, 2)

    def move(self):
        if self.y > 580:
            self.y = -100
   
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
    cone1.draw(screen)
    

    font = pygame.font.SysFont("comicsans", 30, True)
    text = font.render("Score: " +str(car.score), 1, (255, 255, 255))
    screen.blit(text, (390, 10))

    pygame.display.update()




car = player(85, 470, 64, 64)
cone1 = obstacle(95, -80, 64, 64, 10)
cone2 = obstacle(210, -80, 64, 64, 10)



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

    cone1.move()

    if cone1.hitbox[0] == car.hitbox[0] and car.hitbox[1] <= (cone1.hitbox[1] + 90) and car.collide == True:
        car.hit()
        car.collide = False

    if cone1.y > 580:
        car.collide = True

        

    
    print(car.collide)
    draw_screen()






