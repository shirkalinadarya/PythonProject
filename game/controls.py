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
  screen.fill((255, 255, 255))
  gameover.output()
  pygame.display.flip()

def create_alien(alien):
  global alien_height
  if alien_height > -300:
    if alien.shown == False:
      alien.set_coord()
    alien.shown = True
    alien.draw()
    if (alien_height > 2500):
      alien.shown = False
      alien.rect.y = -300
      alien_height = -9000

def update_score(screen, score_text, score_rect):
    screen.blit(score_text, score_rect)
    pygame.display.flip()

def update(bg_color, screen, doodle, bullets, platforms,\
           moving_platforms, crack_platforms, alien, gameover, springs):
  screen.fill(bg_color)
  global step
  if doodle.turbo:
    step = min (step + 0.1, 15)
  else:
    step = 3
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
    if doodle.rect.centerx + 120 >= platform.rect.centerx and doodle.rect.centerx - 120 <= platform.rect.centerx \
    and doodle.rect[1] + doodle.rect[3] - 3 <= platform.rect[1] and doodle.rect[1] + doodle.rect[3] + 3 >= platform.rect[1] \
    and doodle.mdown:
      doodle.touch(step)
      if isinstance(platform, CrackPlatform):
        platform.crashing = True

def touch_spring(doodle, springs):
  for spring in springs:
    if doodle.rect.centerx + 60 >= spring.rect.centerx and doodle.rect.centerx - 600 <= spring.rect.centerx \
    and doodle.rect[1] + doodle.rect[3] - 3 <= spring.rect[1] and doodle.rect[1] + doodle.rect[3] + 3 >= spring.rect[1] \
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
      alien_height = -9000
      alien.rect.y = -300
      bullets.remove(bullet)
    elif bullet.rect.bottom <= 0:
      bullets.remove(bullet)

def touch_alien(doodle, alien):
  if pygame.Rect.colliderect(doodle.rect, alien.rect) and alien.shown and not doodle.turbo:
    doodle.finish = True

def move_and_remove(things):
   for thing in things:
    thing.rect.y += step
    if thing.rect.y > 1200:
      things.remove(thing)

def platforms_move_down(screen, doodle, platforms, moving_platforms, crack_platforms, alien, score, springs):
  global biggest_platform_y
  global step
  global spring_appearing
  spring_appearing += step
  if doodle.rect.y > 500 and doodle.turbo:
    doodle.rect.y -= step
  doodle.rect.y += step
  alien.rect.y += step
  score += step
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
  if biggest_platform_y > 110:
    add_platform(screen, platforms, springs)
  if biggest_moving_platform_y > 300:
    add_moving_platform(screen, moving_platforms)
  if biggest_crack_platform_y > 200:
    add_crack_platforms(screen, crack_platforms)

def move_screen(screen, doodle, platforms, moving_platforms, crack_platforms, alien, score, springs):
  if (doodle.rect.y < 400 and doodle.last_touched - doodle.rect.y < 200 or doodle.turbo):
    platforms_move_down(screen, doodle, platforms, moving_platforms, crack_platforms, alien, score, springs)
  elif doodle.last_touched - doodle.rect.y >= 200:
    doodle.last_touched = 2000

def add_platform(screen, platforms, springs):
  global biggest_platform_y
  platform = Platform(screen)
  platform.rect.x = (random.randint(0, 580)) % 650
  platform.rect.y = biggest_platform_y + random.randint(-350, -100)
  biggest_platform_y = min(biggest_platform_y, platform.rect.y)
  global spring_appearing
  if spring_appearing > 1000:
    spring = Spring(screen)
    spring.rect.x = platform.rect.x + random.randint(0, 100)
    spring.rect.y = platform.rect.y - 30
    spring_appearing = 0
    spring.draw()
    springs.add(spring)
  platform.draw()
  platforms.add(platform)

def add_moving_platform(screen, moving_platforms):
  global biggest_moving_platform_y
  platform = MovingPlatform(screen)
  platform.moving_platform()
  platform.rect.x = (random.randint(0, 650)) % 550
  platform.rect.y = (biggest_moving_platform_y + random.randint(-700, -300))
  biggest_moving_platform_y = min(biggest_moving_platform_y, platform.rect.y)
  platform.draw()
  moving_platforms.add(platform)

def add_crack_platforms(screen, crack_platforms):
  global biggest_crack_platform_y
  platform = CrackPlatform(screen)
  platform.rect.x = (random.randint(0, 650)) % 550
  platform.rect.y = (biggest_crack_platform_y + random.randint(-600, -200))
  biggest_crack_platform_y = min(biggest_crack_platform_y, platform.rect.y)
  platform.draw()
  crack_platforms.add(platform)

def create_platforms(screen, platforms):
  platform = Platform(screen)
  prev_x = platform.rect.x
  prev_y = platform.rect.y
  platforms.add(platform)
  for platform_number in range(6):
    platform = Platform(screen)
    platform.x = (prev_x + random.randint(0, 650)) % 400 
    platform.rect.x = platform.x
    platform.y = (prev_y + random.randint(-270, -230))
    platform.rect.y = platform.y
    prev_x = platform.x
    prev_y = platform.y
    global biggest_platform_y
    biggest_platform_y = min(biggest_platform_y, prev_y)
    platforms.add(platform)
