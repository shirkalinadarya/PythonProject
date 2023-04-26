import pygame
import random
from platforms import Platform
from globals_val import oX, step_x

class MovingPlatform(Platform):
  """class for funclions for object MovingPlatform"""

  def __init__(self, screen):
    """fields of the object MovingPlatform"""
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
 
  def update_moving_platform(self):
    """update coordinates of the object MovingPlatform"""
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