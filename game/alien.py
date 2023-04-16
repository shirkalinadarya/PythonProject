import pygame, random

class Alien():
  def __init__(self, screen):
    self.screen = screen
    self.image = pygame.image.load('game/images/alien.png')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()
    self.rect.centerx = random.randint(0, 650)
    self.rect.y = -1000
    self.shown = False
    self.mright = True
    self.mleft = False
    self.pick = 0

  def set_coord(self):
    self.rect.y = -300
        
  def draw(self):
    self.shown = True
    self.screen.blit(self.image, self.rect)

  def moving(self):
    if self.mright:
      self.pick += 1
      self.rect.x += 1
      if self.pick > 170:
        self.mright = False
        self.mleft = True
    if self.mleft:
      self.pick -= 1
      self.rect.x -= 1
      if self.pick < 0:
        self.mright = True
        self.mleft = False