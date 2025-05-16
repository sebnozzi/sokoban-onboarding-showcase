from common.models.direction import LEFT, RIGHT, UP, DOWN
from game_logic.level import Level


class Game:
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
    if key_name == "right-arrow":
      worker.move(RIGHT)
    elif key_name == "left-arrow":
      worker.move(LEFT)
    elif key_name == "up-arrow":
      worker.move(UP)
    elif key_name == "down-arrow":
      worker.move(DOWN)
    