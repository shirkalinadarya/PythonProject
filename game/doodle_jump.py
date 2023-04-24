import pygame, controls
import sys

from doodle import Doodle
from alien import Alien
from platforms import Platform
from pygame.sprite import Group
from gameover import Gameover
from globals_val import oX, oY

'''Welcome to My Own Doodle Jump.
To manage doodle use arrows ← and →,
to shoot use arrow up ↑.
Avoid aliens and remember that the strongest survives'''

def run():
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
  '''Creating first platforms, which appear in the beginning'''
  controls.create_platforms(screen, platforms) 
  screen.fill(bg_color)
  while True:
    '''Track keystrokes'''
    controls.events(screen, doodle, bullets)
    '''Draw everything'''
    controls.update(bg_color, screen, doodle, bullets, platforms,\
      moving_platforms, crack_platforms, alien, gameover, springs)
    '''Track touching of all kinds of platforms'''
    controls.touch_platform(doodle, platforms)
    controls.touch_platform(doodle, moving_platforms)
    controls.touch_platform(doodle, crack_platforms)
    '''Move screen down if doodle is upper than the middle''' 
    controls.move_screen(screen, doodle, platforms, moving_platforms, crack_platforms, alien, springs)
    '''Track if doodle touches the spring'''
    controls.touch_spring(doodle, springs)
    '''Track if alien kills doodle'''
    controls.touch_alien(doodle, alien)
    '''Crash crack platforms if doodle jumps on it'''
    controls.crack_platforms_crash(crack_platforms)
    '''Finish the game if doodle fell'''
    if doodle.finish:
      for i in range(100):
        controls.stop_game(screen, gameover)
      run()
      

run()
