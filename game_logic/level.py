from common.models.position import Pos
from typing import List


class Level:
  """
  Model of a Sokoban level
  
  Contains level entities like walls and the worker.
  """

  def __init__(self):
    from game_logic.worker import Worker
    self.walls: List[Pos] = []
    self.worker: Worker = Worker(level=self)
    self.row_count = 0
    self.col_count = 0

  def add_wall(self, pos: Pos):
    self.walls.append(pos)
    self._update_counts(pos)

  def place_worker(self, pos: Pos):
    self.worker.set_position(pos)

  def has_free_space_at(self, pos: Pos) -> bool:
    return not self.has_wall_at(pos)

  def has_wall_at(self, pos: Pos) -> bool:
    for wall in self.walls:
      if wall == pos:
        return True
    return False

  def _update_counts(self, pos: Pos):
    self.col_count = max(self.col_count, pos.col + 1)
    self.row_count = max(self.row_count, pos.row + 1)