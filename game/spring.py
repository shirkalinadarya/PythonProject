import pygame

class Spring(pygame.sprite.Sprite):
  def __init__(self, screen):
    super(Spring, self).__init__()
    self.screen = screen
    self.image = pygame.image.load('game/images/spring.png')
    self.rect = self.image.get_rect()
    
  def draw(self):
    self.screen.blit(self.image, self.rect) 