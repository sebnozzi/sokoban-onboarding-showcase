from game_logic.level import Level
from common.models.direction import Direction
from common.models.position import Pos


class Box:
  """
  A box inside of a level
  
  Boxes can be pushed. If they land on a "goal" space, they are "placed"
  """

  def __init__(self, level: Level, initial_pos: Pos):
    self.pos = initial_pos
    self.level = level

  @property
  def is_placed(self) -> bool:
    return self.level.has_goal_at(self.pos)

  def try_performing_push_in(self, direction: Direction):
    target_pos = self.pos.neighbour_at(direction)
    if self.level.has_free_space_at(target_pos):
      self.pos = target_pos
