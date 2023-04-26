import pygame, controls
import sys

from doodle import Doodle
from alien import Alien
from platforms import Platform
from pygame.sprite import Group
from gameover import Gameover
from globals_val import oX, oY

def run():
  """game launch"""
  pygame.init()
  screen = pygame.display.set_mode((oX, oY), pygame.SRCALPHA)
  pygame.display.set_caption("My Doodle Jump")
  bg_color = (200, 230, 220)
  doodle = Doodle(screen)
  alien = Alien(screen)
  bullets = Group()
  platforms = Group()
  moving_platforms = Group()
  crack_platforms = Group()
  springs = Group() 
  gameover = Gameover(screen)
  controls.create_platforms(screen, platforms) 
  screen.fill(bg_color)
  while True:
    controls.events(screen, doodle, bullets)
    controls.update(bg_color, screen, doodle, bullets, platforms,\
      moving_platforms, crack_platforms, alien, gameover, springs)
    controls.touch_platform(doodle, platforms)
    controls.touch_platform(doodle, moving_platforms)
    controls.touch_platform(doodle, crack_platforms)
    controls.move_screen(screen, doodle, platforms, moving_platforms, crack_platforms, alien, springs)
    controls.touch_spring(doodle, springs)
    controls.touch_alien(doodle, alien)
    controls.crack_platforms_crash(crack_platforms)
    if doodle.finish:
      for i in range(100):
        controls.stop_game(screen, gameover)
      run() 

run()