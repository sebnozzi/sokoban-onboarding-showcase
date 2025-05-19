
from game_logic.level import Level
from common.models.direction import Direction
from common.models.position import Pos


class Worker:
  """
  The worker inside of a level
  
  Can move inside a level and push boxes.
  """

  def __init__(self, level: Level, initial_pos: Pos):
    self.pos = initial_pos
    self.level = level

  def move(self, direction: Direction):
    """
    Tries to perform a move in the given direction
    
    It only succeeds if the target-position is empty or, if 
    containing a box, the box can be pushed.

    Otherwise the worker stays where it is.
    """
    level: Level = self.level
    target_pos = self.pos.neighbour_at(direction)
    # Try to push box if on target-position
    if level.has_pushable_box_at(target_pos, direction):
      level.perform_box_push(target_pos, direction)
    # At this point the target-position is either free or (still) occupied
    if level.has_free_space_at(target_pos):
      self.pos = target_pos