import pygame

class Platform(pygame.sprite.Sprite):
  """class for funclions for object Platform"""

  def __init__(self, screen):
    """fields of the object Platform"""
    super(Platform, self).__init__()
    self.screen = screen
    self.image = pygame.image.load('game/images/green_platform.png')
    self.rect = self.image.get_rect()
    self.rect.x = 325
    self.rect.y = 900
    self.x = float(self.rect.x)
    self.mleft = False
    self.mright = True
    self.dist = 0
  
  def draw(self):
    """draw the object Platform on the screen"""
    self.screen.blit(self.image, self.rect) 