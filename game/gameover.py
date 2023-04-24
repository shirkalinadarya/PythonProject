import pygame, time
from globals_val import oX_gameover, oY_gameover

class Gameover():
  def __init__(self, screen):
    self.screen = screen
    self.image = pygame.image.load('game/images/gameover.png')
    self.image = pygame.transform.scale(self.image, (oX_gameover, oY_gameover))
    self.rect = self.image.get_rect()
    self.rect.centerx = screen.get_rect().centerx
    self.rect.centery = screen.get_rect().centery
    
  def output(self):
    self.screen.blit(self.image, self.rect)

