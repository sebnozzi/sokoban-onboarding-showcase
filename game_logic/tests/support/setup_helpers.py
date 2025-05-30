from common.level_io.parsing import parse_level
from game_logic.game_controller import GameController


def game_with_level(level_data: str) -> GameController:
  level = parse_level(level_data)
  game_controller = GameController()
  game_controller.set_level(level=level)
  return game_controller
