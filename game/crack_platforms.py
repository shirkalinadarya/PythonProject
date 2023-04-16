import pygame
from platforms import Platform
from globals_val import *


class CrackPlatform(Platform):
  def __init__(self, screen):
    super(Platform, self).__init__()
    self.screen = screen
    self.image = pygame.image.load('images/crack_platform.png')
    self.rect = self.image.get_rect()
    self.rect.x = 325
    self.rect.y = 900
    self.x = float(self.rect.x)
    self.y = float(self.rect.y)
    self.mleft = False
    self.mright = True
    self.dist = 0   
    self.crashing = False
    
  def crash(self):
    if (self.crashing):
      self.rect.y += step