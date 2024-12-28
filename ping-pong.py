import pygame
from pygame.locals import *
from pygame import*
import random

#create window
width = 700
height = 700
screen_size = (width, height)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Ping-Pong game")
background = transform.scale(image.load("fancy-court.png"),(screen_size))
right_paddle = transform.scale(image.load("fancy-paddle-blue.png"),(50, 150))
left_paddle = transform.scale(image.load("fancy-paddle-green.png"),(50, 150))
ball = transform.scale(image.load("fancy-ball.png"),(50, 50))



#game loop

clock = pygame.time.Clock()
FPS = 120
running = True
y1  = 0
y2 = 0

while running:
    clock.tick(FPS)
    screen.blit(background,(0, 0))
    screen.blit(right_paddle,(10, y1))
    screen.blit(left_paddle,(640, y2))
    screen.blit(ball,(300, 300))

    keys_pressed = key.get_pressed()

    if keys_pressed[K_UP] and y1 >5:
        y1 -= 10
    if keys_pressed[K_DOWN] and y1 <545:
        y1 += 10
    if keys_pressed[K_w] and y2 >5:
        y2 -= 10
    if keys_pressed[K_s] and y2 <545:
        y2 += 10

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    pygame.display.update()

pygame.quit()