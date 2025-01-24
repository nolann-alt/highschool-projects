import time
import random
import pygame

pygame.init()
width, height = 800, 450
backgroundColor = 50, 100, 150

screen = pygame.display.set_mode((width, height))
colorBall = 255, 255, 255
radius = 50
decalX1 = 10
decalY1 = 10
centerY1 = 0
colorRect = 0, 0, 50
decalX2 = 10
decalY2 = 10
centerX2 = 0
centerY2 = 410
centerX1 = random.randint(0, width)


while True:
  screen.fill(backgroundColor)
  center = centerX1, centerY1
  pygame.draw.circle(screen, colorBall, center, radius)
  centerY1 = centerY1 + decalY1
  pygame.draw.rect(screen, colorRect, (centerX2, centerY2, 100, 20))
  pygame.display.flip()
  time.sleep(0.04)
  if centerY1 > height:
    centerY1 = 0
  centerY2 = centerY2
  if centerX1-radius > centerX2 + centerY2 + radius:
    centerY1 = 0
  for event in pygame.event.get():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        centerY2 -= decalY2
    if keys[pygame.K_DOWN]:
        centerY2 += decalY2
    if keys[pygame.K_LEFT]:
        centerX2 -= decalX2
    if keys[pygame.K_RIGHT]:
        centerX2 += decalX2