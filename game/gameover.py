import pygame, time

class Gameover():
  def __init__(self, screen):
    self.screen = screen
    self.image = pygame.image.load('images/gameover.png')
    self.image = pygame.transform.scale(self.image, (550, 900))
    self.rect = self.image.get_rect()
    self.screen_rect = screen.get_rect()
    self.rect.centerx = 300
    self.rect.centery = 500
    
  def output(self):
    self.screen.blit(self.image, self.rect)

