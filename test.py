import pygame
import random
random.seed()


def show_text(screen, text, position):
    text_font = pygame.font.SysFont('freesansbold.ttf', 50)
    textSurface = text_font.render(text, True, (255, 0, 0))
    screen.blit(textSurface, (position[0], position[1]))


class Spaceship:
    def __init__(self, screen):
        self.screen = screen
        self.ship_x = self.screen.get_width() // 2-30
        self.ship_y = self.screen.get_height()-70
        self.image = pygame.image.load('pictures/spaceship.png')
        self.x_change = 0
        self.gameover = False

    def move(self, bullet):
        if self.ship_x > self.screen.get_width()-self.image.get_width() or self.ship_x < 0:
            self.ship_x -= self.x_change
            bullet.bullet_x -= self.x_change
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.x_change = -1
                if event.key == pygame.K_RIGHT:
                    self.x_change = 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    self.x_change = 0
        self.ship_x += self.x_change
        bullet.bullet_x += self.x_change

    def show(self):
        self.screen.blit(self.image, (self.ship_x, self.ship_y))


class Enemy:
    def __init__(self, screen):
        self.screen = screen
        self.enemy_x = random.randint(0, self.screen.get_width()-70)
        self.enemy_y = 0
        self.y_change = 0.5
        self.image = pygame.image.load('pictures/enemy4.png')
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.crash = False

    def move(self):
        self.enemy_y += self.y_change
        if self.enemy_y > self.screen.get_height()+100 or self.crash == True:
            self.enemy_x = random.randint(0, self.screen.get_width()-70)
            self.enemy_y = random.randint(-400, -100)
            self.crash = False

    def score(self, score):

        return score+1

    def show(self):
        if self.crash == False:
            self.screen.blit(self.image, (self.enemy_x, self.enemy_y))


class Bullet:
    def __init__(self, screen, ship):
        self.screen = screen
        self.bullet_x = ship.ship_x+33
        self.bullet_y = self.screen.get_height()-120
        self.image = pygame.image.load('pictures/laser.png')
        self.y_change = -0.75
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def move(self, ship):
        self.bullet_x = ship.ship_x+33
        self.bullet_y += self.y_change
        if self.bullet_y+self.height < -10:
            self.bullet_x = ship.ship_x+33
            self.bullet_y = self.screen.get_height()-120

    def crash(self, enemy):
        if self.bullet_y < 0:
            return
        if self.bullet_x >= enemy.enemy_x and self.bullet_x+self.width <= enemy.enemy_x+enemy.width:
            if self.bullet_y <= enemy.enemy_y+enemy.height:
                enemy.crash = True

        elif self.bullet_x >= enemy.enemy_x and self.bullet_x < enemy.enemy_x+enemy.width:
            if self.bullet_y <= enemy.enemy_y+enemy.height:
                enemy.crash = True

        elif self.bullet_x <= enemy.enemy_x and self.bullet_x+self.width >= +enemy.enemy_x+enemy.width:
            if self.bullet_y <= enemy.enemy_y+enemy.height:
                enemy.crash = True

    def show(self):
        if self.bullet_y <= self.screen.get_height()-110:
            self.screen.blit(self.image, (self.bullet_x, self.bullet_y))
