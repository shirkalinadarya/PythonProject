import pygame, sys, random

from spring import Spring
from globals_val import *
from bullet import Bullet
from platforms import Platform
from moving_platforms import MovingPlatform
from crack_platforms import CrackPlatform
from gameover import Gameover


def events(screen, doodle, bullets):
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        doodle.mright = True
      if event.key == pygame.K_LEFT:
        doodle.mleft = True
        
      if event.key == pygame.K_UP:
        new_bullet = Bullet(screen, doodle)
        bullets.add(new_bullet)

    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_RIGHT:
        doodle.mright = False
      if event.key == pygame.K_LEFT:
        doodle.mleft = False

def stop_game(screen, gameover):
  screen.fill((white, white, white))
  gameover.output()
  pygame.display.flip()

def create_alien(alien):
  global alien_height
  if alien_height > alien_appear:
    if alien.shown == False:
      alien.set_coord()
    alien.shown = True
    alien.draw()
    if (alien_height > alien_fall):
      alien.shown = False
      alien.rect.y = y_appear
      alien_height = -alien_repeat

def update_score(screen, score_text, score_rect):
    screen.blit(score_text, score_rect)
    pygame.display.flip()

def update(bg_color, screen, doodle, bullets, platforms,\
           moving_platforms, crack_platforms, alien, gameover, springs):
  screen.fill(bg_color)
  global step
  if doodle.turbo:
    step = min(step + acceleration, step_acceleration)
  else:
    step = step_x_doodle
  global spring_appearing
  doodle.update(step)
  screen.set_alpha(0)
  if alien.shown:
    alien.moving()
  for bullet in bullets.sprites():
    bullet.output()
  for platform in moving_platforms:
    platform.update_moving_platform()
  doodle.output()
  create_alien(alien)
  platforms.draw(screen)
  moving_platforms.draw(screen)
  crack_platforms.draw(screen)
  springs.draw(screen)
  pygame.display.flip()

def touch_platform(doodle, platforms):
  for platform in platforms:
    if doodle.rect.centerx + doodle_touch_platform >= platform.rect.centerx and \
      doodle.rect.centerx - doodle_touch_platform <= platform.rect.centerx \
        and doodle.rect[1] + doodle.rect[3] - step_x_doodle <= platform.rect[1] and \
          doodle.rect[1] + doodle.rect[3] + step_x_doodle >= platform.rect[1] and doodle.mdown:
      doodle.touch(step)
      if isinstance(platform, CrackPlatform):
        platform.crashing = True

def touch_spring(doodle, springs):
  for spring in springs:
    if doodle.rect.centerx + doodle_touch_spring >= spring.rect.centerx and \
      doodle.rect.centerx - doodle_touch_spring <= spring.rect.centerx \
    and doodle.rect[1] + doodle.rect[3] - step_x_doodle <= spring.rect[1] and \
      doodle.rect[1] + doodle.rect[3] + step_x_doodle >= spring.rect[1] \
    and doodle.mdown:
      doodle.turbo = True
      doodle.touch(step)
    
def crack_platforms_crash(platforms):
  for platform in platforms:
    if platform.crash:
      platform.crash()

def update_bullets(bullets, alien):
  bullets.update()
  global alien_height
  for bullet in bullets.copy():
    if pygame.Rect.colliderect(bullet.rect, alien.rect):
      alien.shown = False  
      alien_height = -alien_repeat
      alien.rect.y = -alien_appear
      bullets.remove(bullet)
    elif bullet.rect.bottom <= 0:
      bullets.remove(bullet)

def touch_alien(doodle, alien):
  if pygame.Rect.colliderect(doodle.rect, alien.rect) and \
    alien.shown and not doodle.turbo:
    doodle.finish = True

def move_and_remove(things):
   for thing in things:
    thing.rect.y += step
    if thing.rect.y > disappear_y:
      things.remove(thing)

def platforms_move_down(screen, doodle, platforms, moving_platforms, \
                        crack_platforms, alien, springs):
  global biggest_platform_y
  global step
  global spring_appearing
  spring_appearing += step
  if doodle.rect.y > doodle_max_y and doodle.turbo:
    doodle.rect.y -= step
  doodle.rect.y += step
  alien.rect.y += step
  global height
  global alien_height
  height += step
  alien_height += step
  biggest_platform_y += step
  global biggest_moving_platform_y
  global biggest_crack_platform_y
  biggest_crack_platform_y += step
  biggest_moving_platform_y += step
  move_and_remove(platforms)
  move_and_remove(moving_platforms)
  move_and_remove(crack_platforms)
  move_and_remove(springs)
  if biggest_platform_y > usual_platform_appear:
    add_platform(screen, platforms, springs)
  if biggest_moving_platform_y > moving_platform_appear:
    add_moving_platform(screen, moving_platforms)
  if biggest_crack_platform_y > crack_platform_appear:
    add_crack_platforms(screen, crack_platforms)

def move_screen(screen, doodle, platforms, moving_platforms, crack_platforms, alien, springs):
  if (doodle.rect.y < doodle_move * 2 and doodle.last_touched - doodle.rect.y < doodle_move or doodle.turbo):
    platforms_move_down(screen, doodle, platforms, moving_platforms, crack_platforms, alien, springs)
  elif doodle.last_touched - doodle.rect.y >= doodle_move:
    doodle.last_touched = doodle_no_touch

def add_platform(screen, platforms, springs):
  global biggest_platform_y
  platform = Platform(screen)
  platform.rect.x = random.randint(0, oX)
  platform.rect.y = biggest_platform_y + \
    random.randint(usual_platform_appear1_y, usual_platform_appear2_y)
  biggest_platform_y = min(biggest_platform_y, platform.rect.y)
  global spring_appearing
  if spring_appearing > spring_often:
    spring = Spring(screen)
    spring.rect.x = platform.rect.x + random.randint(0, spring_random_x)
    spring.rect.y = platform.rect.y - spring_place_y
    spring_appearing = 0
    spring.draw()
    springs.add(spring)
  platform.draw()
  platforms.add(platform)

def add_moving_platform(screen, moving_platforms):
  global biggest_moving_platform_y
  platform = MovingPlatform(screen)
  platform.moving_platform()
  platform.rect.x = (random.randint(0, oX)) % platform_right_x
  platform.rect.y = (biggest_moving_platform_y + \
                     random.randint(crack_platform_appear1_y, crack_platform_appear2_y))
  biggest_moving_platform_y = min(biggest_moving_platform_y, platform.rect.y)
  platform.draw()
  moving_platforms.add(platform)

def add_crack_platforms(screen, crack_platforms):
  global biggest_crack_platform_y
  platform = CrackPlatform(screen)
  platform.rect.x = (random.randint(0, oX)) % platform_right_x
  platform.rect.y = (biggest_crack_platform_y + \
                     random.randint(crack_platform_appear1_y, crack_platform_appear2_y))
  biggest_crack_platform_y = min(biggest_crack_platform_y, platform.rect.y)
  platform.draw()
  crack_platforms.add(platform)

def create_platforms(screen, platforms):
  platform = Platform(screen)
  prev_x = platform.rect.x
  prev_y = platform.rect.y
  platforms.add(platform)
  for platform_number in range(num_of_start_platforms):
    platform = Platform(screen)
    platform.x = (prev_x + random.randint(-oX, oX) + oX) % platform_right_x 
    platform.rect.x = platform.x
    platform.y = (prev_y + random.randint(start_platform_rand1_y, start_platform_rand2_y))
    platform.rect.y = platform.y
    prev_x = platform.x
    prev_y = platform.y
    global biggest_platform_y
    biggest_platform_y = min(biggest_platform_y, prev_y)
    platforms.add(platform)
