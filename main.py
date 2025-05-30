from game_logic.level import Level
from common.level_io.parsing import parse_level
from game_logic.game_controller import (
  GameController,
  UP_ARROW_KEY,
  DOWN_ARROW_KEY,
  LEFT_ARROW_KEY,
  RIGHT_ARROW_KEY,
)
from pygame_specific.rendering import render_level
import pygame


LEVEL_DATA = """
    #####
    #   # 
    #   # 
  ###   ##
  #      #
### # ## #   ######
#   # ## ##### $. # 
#             $ . #
##### ### #@##    # 
    #     ######### 
    #######
"""

FPS=30
SCREEN_RESOLUTION=(800,600)
QUIT_KEYS=[pygame.K_ESCAPE, pygame.K_q]


def main():
  level = parse_level(LEVEL_DATA)
  game = GameController()
  game.set_level(level=level)
  play_game(game)


def play_game(game: GameController):
  pygame.init()
  screen = pygame.display.set_mode(SCREEN_RESOLUTION)
  # Disable key-repeats
  pygame.key.set_repeat(0)
  run_game_loop(screen, game)


def run_game_loop(screen: pygame.Surface, game: GameController):
  clock = pygame.time.Clock()
  running = True
  while running:
    running = process_events(game)
    render(screen, game)
    clock.tick(FPS)
  pygame.quit()


def process_events(game: GameController) -> bool:
  """
  Processes events, advancing game if necessary.
  
  Returns wether it should keep running or not.
  """
  for event in pygame.event.get():
    if should_quit(event):
      return False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        game.process_key(RIGHT_ARROW_KEY)
      if event.key == pygame.K_LEFT:
        game.process_key(LEFT_ARROW_KEY)
      if event.key == pygame.K_DOWN:
        game.process_key(DOWN_ARROW_KEY)
      if event.key == pygame.K_UP:
        game.process_key(UP_ARROW_KEY)
  return True


def should_quit(event) -> bool:
  """Returns True if the event signals that the program should quit"""
  # pygame.QUIT event means the user clicked X to close your window
  return event.type == pygame.QUIT or (
    event.type == pygame.KEYDOWN and event.key in QUIT_KEYS)


def render(screen: pygame.Surface, game: GameController):
  screen.fill("black")
  render_level(screen, game.level)
  pygame.display.flip()


if __name__ == '__main__':
  main()
