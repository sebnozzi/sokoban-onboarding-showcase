from common.models import direction
from game_logic.level import Level

# == Arrow-key constants
RIGHT_ARROW_KEY = "right-arrow"
LEFT_ARROW_KEY  = "left-arrow"
UP_ARROW_KEY    = "up-arrow"
DOWN_ARROW_KEY  = "down-arrow"


class GameController:
  """
  Game controller

  Interactions with the model go through this class.
  
  Processes events and moves the worker inside the level.
  """

  def __init__(self):
    self.level = None

  def set_level(self, level: Level):
    self.level = level

  def process_key(self, key_name: str):
    worker = self.level.worker
    if key_name == RIGHT_ARROW_KEY:
      worker.move(direction.RIGHT)
    elif key_name == LEFT_ARROW_KEY:
      worker.move(direction.LEFT)
    elif key_name == UP_ARROW_KEY:
      worker.move(direction.UP)
    elif key_name == DOWN_ARROW_KEY:
      worker.move(direction.DOWN)
    else:
      raise f"Unrecognized key-name: {key_name}"
    