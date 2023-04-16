import pygame
from platforms import Platform

class MovingPlatform(Platform):
  def __init__(self, screen):
    super(Platform, self).__init__()
    self.screen = screen
    self.image = pygame.image.load('images/moving_platform.png')
    self.rect = self.image.get_rect()
    self.rect.x = float(325)
    self.rect.y = float(900)
    self.x = float(self.rect.x)
    self.y = float(self.rect.y)
    self.mleft = False
    self.mright = True
    self.dist = 0   

  def moving_platform(self):
    self.image = pygame.image.load('images/moving_platform.png')
    self.rect = self.image.get_rect()

  def update_moving_platform(self):
    if self.mright:
      self.dist += 1
      self.rect.x += 1
      if self.rect.right > 650:
        self.mright = False
        self.mleft = True
    if self.mleft:
      self.dist -= 1
      self.rect.x -= 1
      if self.rect.left < 0: 
        self.mleft = False
        self.mright = True