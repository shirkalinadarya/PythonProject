import pygame

class Doodle():
  def __init__(self, screen):
    self.screen = screen
    self.image = pygame.image.load('images/doodle.png')
    self.rect = self.image.get_rect()
    self.rect.centery = 0
    self.screen_rect = screen.get_rect()
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = 500
    self.mright = False
    self.mleft = False
    self.mup = False
    self.mdown = True
    self.prev_y = 0
    self.touched = False
    self.last_touched = 0
    self.finish = False
    self.turbo = False

  def output(self):
    self.screen.blit(self.image, self.rect)

  def touch(self, step):
    self.touched = True
    self.last_touched = self.rect.y
    self.update(step)
    self.touched = False

  def update(self, step):
    if self.rect.centery > 1300:
      self.finish = True
    if self.touched:
      self.mup = True
      self.mdown = False
      self.prev_y = 0
    if self.mright:
      if self.rect.right >= self.screen_rect.right + 100:
        self.rect.left = -95
      else:
        self.rect.centerx += 3
    if self.mleft:
      if self.rect.left <= self.screen_rect.left - 100:
        self.rect.x = 745
      else:
        self.rect.centerx -= 3
    if self.mup:
      if (self.prev_y >= 400 and not self.turbo) or (self.prev_y >= 900 and self.turbo):
        self.prev_y = 0
        if self.turbo:
          step = 3
        self.turbo = False
        self.mup = False
        self.mdown = True
      else:
        self.prev_y += step
        self.rect.centery -= step
    if self.mdown:
      self.prev_y -= step
      self.rect.centery += step

