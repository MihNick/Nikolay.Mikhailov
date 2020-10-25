import pygame,sys
from pygame.draw import *
pygame.init()

screen = pygame.display.set_mode((500, 700))
running = True

rect(screen, (80, 120,100), (2,2, 500,700))
rect(screen, (240, 255,240), (2,2, 500,500))

surface0 = pygame.Surface((500,200))
surface0.set_colorkey((0, 0, 0))
ellipse(surface0, (255,255,255),(0, 0, 500, 200))

rect(screen, (220, 220, 220), (390, 20, 95, 510))
rect(screen, (75, 125, 125), (345, 90, 95, 480))
rect(screen, (112, 128, 144), (10, 20, 95, 500))
rect(screen, (150, 200, 150), (120, 50, 95, 470))
rect(screen, (211, 211, 211), (70, 100, 95, 450))
rect(screen, (0, 191, 255), (160, 630, 200, 40))
rect(screen, (0, 191, 255), (190, 600, 120, 40))
rect(screen, (255, 255, 255), (210, 610, 30, 20))
rect(screen, (255, 255, 255), (260, 610, 30, 20))

surface = pygame.Surface((250,190))
surface.set_colorkey((0, 0, 0))
ellipse(surface, (180, 200, 180), (0, 0, 300, 90))

surface1 = pygame.Surface((400, 160))
surface1.set_colorkey((0, 0, 0))
ellipse(surface1, (180,200,180), (0, 0,400, 80))

surface2 = pygame.Surface((220, 100))
surface2.set_colorkey((0, 0, 0))
ellipse(surface2, (30, 30, 30), (0, 0, 40, 40))

surface3 = pygame.Surface((220, 100))
surface3.set_colorkey((0, 0, 0))
ellipse(surface3, (30, 30, 30), (0, 0, 40, 40))

surface4 = pygame.Surface((320, 80))
surface4.set_colorkey((0, 0, 0))
ellipse(surface4, (180, 200, 180), (0, 0, 320, 80))

surface5 = pygame.Surface((220, 100))
surface5.set_colorkey((0, 0, 0))
ellipse(surface5, (180, 200, 180), (0, 0, 220, 80))

surface6 = pygame.Surface((120, 40))
surface6.set_colorkey((0, 0, 0))
ellipse(surface6, (180, 200, 180), (0, 0, 120, 40))

surface7 = pygame.Surface((120, 40))
surface7.set_colorkey((0, 0, 0))
ellipse(surface7, (180, 200, 180), (0, 0, 120, 40))

surface8 = pygame.Surface((120, 40))
surface8.set_colorkey((0, 0, 0))
ellipse(surface8, (180, 200, 180), (0, 0, 120, 40))

surface9 = pygame.Surface((30, 10))
surface9.set_colorkey((0, 0, 0))
ellipse(surface9, (30, 30, 30), (0, 0, 30, 10))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  screen.blit(surface0, (0, 590))
  screen.blit(surface, (280, 0))
  screen.blit(surface1, (160, 160))
  screen.blit(surface2, (175, 655))
  screen.blit(surface3, (310, 655))
  screen.blit(surface4, (0, 30))
  screen.blit(surface5, (0, 400))
  screen.blit(surface6, (0, 530))
  screen.blit(surface7, (20, 580))
  screen.blit(surface8, (10, 630))
  screen.blit(surface9, (145, 655))
  pygame.display.update()

pygame.quit()