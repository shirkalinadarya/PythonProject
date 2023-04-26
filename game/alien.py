import pygame, random
from globals_val import y_appear, alien_start, alien_move, step_x, oX

class Alien():
  """class for funclions for object Alien"""

  def __init__(self, screen):
    """fields of object Alien"""
    self.screen = screen
    self.image = pygame.image.load('game/images/alien.png')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()
    self.rect.centerx = random.randint(0, oX)
    self.rect.y = alien_start
    self.shown = False
    self.mright = True
    self.mleft = False
    self.pick = 0

  def set_coord(self):
    """set coordinates of the object Alien"""
    self.rect.y = y_appear
        
  def draw(self):
    """draw the object Alien on the screen"""
    self.shown = True
    self.screen.blit(self.image, self.rect)

  def moving(self):
    """change coordinates of the object Alien"""
    if self.mright:
      self.pick += step_x
      self.rect.x += step_x
      if self.pick > alien_move:
        self.mright = False
        self.mleft = True
    if self.mleft:
      self.pick -= step_x
      self.rect.x -= step_x
      if self.pick < 0:
        self.mright = True
        self.mleft = False