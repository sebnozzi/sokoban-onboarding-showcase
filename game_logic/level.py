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
    self.worker: Worker = None
    self.row_count = 0
    self.col_count = 0

  def add_wall(self, pos: Pos):
    self.walls.append(pos)
    self._update_dimensions(pos)

  def add_worker(self, pos: Pos):
    from game_logic.worker import Worker
    self.worker = Worker(level=self, initial_pos=pos)

  def has_free_space_at(self, pos: Pos) -> bool:
    return not self.has_wall_at(pos)

  def has_wall_at(self, pos: Pos) -> bool:
    return any(wall_pos == pos 
               for wall_pos in self.walls)

  def _update_dimensions(self, pos: Pos):
    self.col_count = max(self.col_count, pos.col + 1)
    self.row_count = max(self.row_count, pos.row + 1)