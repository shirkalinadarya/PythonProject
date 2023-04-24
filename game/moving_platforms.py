import pygame
import random
from platforms import Platform
from globals_val import oX, step_x

class MovingPlatform(Platform):
  def __init__(self, screen):
    super(Platform, self).__init__()
    self.screen = screen
    self.image = pygame.image.load('game/images/moving_platform.png')
    self.rect = self.image.get_rect()
    self.rect.x = random.randint(0, oX)
    self.rect.y = 0
    self.x = float(self.rect.x)
    self.y = float(self.rect.y)
    self.mleft = False
    self.mright = True
    self.dist = 0   

  def moving_platform(self):
    self.image = pygame.image.load('game/images/moving_platform.png')
    self.rect = self.image.get_rect()

  '''Moving platforms move, so it is the moving left and right'''
  def update_moving_platform(self):
    if self.mright:
      self.dist += step_x
      self.rect.x += step_x
      if self.rect.right > oX:
        self.mright = False
        self.mleft = True
    if self.mleft:
      self.dist -= step_x
      self.rect.x -= step_x
      if self.rect.left < 0: 
        self.mleft = False
        self.mright = True