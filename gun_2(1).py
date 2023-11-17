import math
from random import choice, randint
import numpy as np
import pygame

FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = 0x000000
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600

class Ball:
    def __init__(self, screen: pygame.Surface, x1, y1, x2, y2):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x01 = x1
        self.y01 = y1
        self.x02 = x2
        self.y02 = y2
        self.r = 10
        self.vx = 10
        self.vy = 10
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # FIXME
        'Done?'
        self.vx = 30
        self.vy = 0
        self.x01 += self.vx
        self.y01 -= self.vy
        self.x02 -= self.vx
        self.y02 -= self.vy
        pygame.display.update()

    def draw_1(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x01, self.y01),
            self.r
        )
        
    def draw_2(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x02, self.y02),
            self.r
        )

class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = BLACK
        self.x01 = 40
        self.y01 = 450
        self.x02 = 760
        self.y02 = 150

    def fire1(self):
        global balls1, bullet
        bullet += 1
        new_ball = Ball(self.screen, self.x01, self.y01, self.x02, self.y02)
        new_ball.r += 5
        balls1.append(new_ball)

    def fire2(self):
        global balls2, bullet
        bullet += 1
        new_ball = Ball(self.screen, self.x01, self.y01, self.x02, self.y02)
        new_ball.r += 5
        balls2.append(new_ball)

    def draw_1(self):
        surf = pygame.image.load('танк1.jpeg').convert_alpha()
        surf = pygame.transform.scale(surf, (162, 50))
        surf.set_colorkey((255, 255, 255))
        screen.blit(surf, (self.x01-81, self.y01-25))
        #pygame.display.update()

    def draw_2(self):
        surf = pygame.image.load('танк2.jpg').convert_alpha()
        surf = pygame.transform.scale(surf, (162, 50))
        surf.set_colorkey((255, 255, 255))
        screen.blit(surf, (self.x02-81, self.y02-25))
        #pygame.display.update()

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls1 = []
balls2 = []

clock = pygame.time.Clock()
gun = Gun(screen)
#target = Target(screen)
finished = False

while not finished:
    screen.fill(WHITE)
    surf = pygame.image.load('поле.jpeg')
    surf = pygame.transform.scale(surf, (WIDTH, HEIGHT))
    screen.blit(surf, (0, 0))
    #pygame.display.update()
    #target.draw()
    gun.draw_1()
    gun.draw_2()
    #target.move_1()
    #target.move_2()
    for b in balls1:
        b.draw_1()
    for b in balls2:
        b.draw_2()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        '''
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)
        '''
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                gun.fire1()
            if event.key == pygame.K_x:
                gun.fire2()
            if event.key == pygame.K_LEFT:
                gun.x01 -= 5
                gun.draw_1()
            if event.key == pygame.K_RIGHT:
                gun.x01 += 5
                gun.draw_1()
            if event.key == pygame.K_UP:
                gun.y01 -= 5
                gun.draw_1()
            if event.key == pygame.K_DOWN:
                gun.y01 += 5
                gun.draw_1()
            if event.key == pygame.K_a:
                gun.x02 -= 5
                gun.draw_2()
            if event.key == pygame.K_d:
                gun.x02 += 5
                gun.draw_2()
            if event.key == pygame.K_w:
                gun.y02 -= 5
                gun.draw_2()
            if event.key == pygame.K_s:
                gun.y02 += 5
                gun.draw_2()
            
            
    for b in balls1:
        b.move()
    for b in balls2:
        b.move()

pygame.quit()
