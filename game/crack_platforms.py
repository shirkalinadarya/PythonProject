import pygame
import random
from platforms import Platform
from globals_val import step, oX

class CrackPlatform(Platform):
  """class for funclions for object CrackPlatform"""
  
  def __init__(self, screen):
    """fields of the object CrackPlatform"""
    super(Platform, self).__init__()
    self.screen = screen
    self.image = pygame.image.load('game/images/crack_platform.png')
    self.rect = self.image.get_rect()
    self.rect.x = random.randint(0, oX)
    self.rect.y = 0
    self.x = float(self.rect.x)
    self.y = float(self.rect.y)
    self.mleft = False
    self.mright = True
    self.dist = 0   
    self.crashing = False

  def crash(self):
    """platform moves down if it is crashed"""
    if (self.crashing):
      self.rect.y += step