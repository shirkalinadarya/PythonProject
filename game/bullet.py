import pygame
from globals_val import bullet_speed

class Bullet(pygame.sprite.Sprite):
  """class for functions for the object Bullet"""

  def __init__(self, screen, doodle):
    """fields of the object Bullet"""
    super(Bullet, self).__init__()
    self.screen = screen
    self.image = pygame.image.load('game/images/bullet.png')
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()
    self.speed = bullet_speed
    self.rect.centerx = doodle.rect.centerx
    self.rect.top = doodle.rect.top
    self.y = float(self.rect.y)

  def output(self):
    """draw the object Bullet on the screen"""
    self.screen.blit(self.image, self.rect)    

  def update(self):
    """change coordinates of the object Bullet"""
    self.y -= self.speed
    self.rect.y = self.y