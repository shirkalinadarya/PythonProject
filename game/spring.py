import pygame

class Spring(pygame.sprite.Sprite):
  """class for functions for the object Spring"""

  def __init__(self, screen):
    """fields of the object Spring"""
    super(Spring, self).__init__()
    self.screen = screen
    self.image = pygame.image.load('game/images/spring.png')
    self.rect = self.image.get_rect()
    
  def draw(self):
    """draw the object Spring on the screen"""
    self.screen.blit(self.image, self.rect) 