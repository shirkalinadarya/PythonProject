import pygame

from globals_val import step_x_doodle, doodle_start_bottom, \
  doodle_fall, doodle_evasion, oX, doodle_jump, doodle_jump_turbo

class Doodle():
  """class for funclions for object Doodle"""

  def __init__(self, screen):
    """fields of the object Doodle"""
    self.screen = screen
    self.image = pygame.image.load('game/images/doodle.png')
    self.rect = self.image.get_rect()
    self.rect.centery = 0
    self.screen_rect = screen.get_rect()
    self.rect.centerx = self.screen_rect.centerx
    self.rect.bottom = doodle_start_bottom
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
    """draw the object Doodle on the screen"""
    self.screen.blit(self.image, self.rect)

  def touch(self, step):
    """set that Doodle touched"""
    self.touched = True
    self.last_touched = self.rect.y
    self.update(step)
    self.touched = False

  def update(self, step):
    """update coordinates of the object Doodle"""
    if self.rect.centery > doodle_fall:
      self.finish = True
    if self.touched:
      self.mup = True
      self.mdown = False
      self.prev_y = 0
    if self.mright:
      if self.rect.right >= self.screen_rect.right + doodle_evasion:
        self.rect.left = -doodle_evasion + 1 
      else:
        self.rect.centerx += step_x_doodle
    if self.mleft:
      if self.rect.left <= self.screen_rect.left - doodle_evasion:
        self.rect.x = oX + doodle_evasion - 1
      else:
        self.rect.centerx -= step_x_doodle
    if self.mup:
      if (self.prev_y >= doodle_jump and not self.turbo) or \
        (self.prev_y >= doodle_jump_turbo and self.turbo):
        self.prev_y = 0
        if self.turbo:
          step = step_x_doodle
        self.turbo = False
        self.mup = False
        self.mdown = True
      else:
        self.prev_y += step
        self.rect.centery -= step
    if self.mdown:
      self.prev_y -= step
      self.rect.centery += step