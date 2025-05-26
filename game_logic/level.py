from common.models.direction import Direction
from common.models.position import Pos
from typing import List, Optional


class Level:
  """
  Model of a Sokoban level
  
  Contains level entities like walls, boxes and the worker.
  """

  def __init__(self):
    from game_logic.worker import Worker
    from game_logic.box import Box
    self.walls: List[Pos] = []
    self.goals: List[Pos] = []
    self.boxes: List[Box] = []
    self.worker: Worker = None
    self.row_count = 0
    self.col_count = 0

  def add_wall(self, pos: Pos):
    self.walls.append(pos)
    self._update_dimensions(pos)

  def add_goal_position(self, pos: Pos):
    self.goals.append(pos)

  def add_box(self, pos: Pos):
    from game_logic.box import Box
    box = Box(level=self, initial_pos=pos)
    self.boxes.append(box)

  def add_worker(self, pos: Pos):
    from game_logic.worker import Worker
    self.worker = Worker(level=self, initial_pos=pos)

  def has_free_space_at(self, pos: Pos) -> bool:
    return not (self.has_wall_at(pos) 
                or self.has_box_at(pos))

  def has_wall_at(self, pos: Pos) -> bool:
    return any(wall_pos == pos 
               for wall_pos in self.walls)
  
  def has_goal_at(self, pos: Pos) -> bool:
     return any(goal_pos == pos 
               for goal_pos in self.goals)
   
  def has_box_at(self, pos: Pos) -> bool:
    return any(box.pos == pos 
               for box in self.boxes)
  
  def try_getting_box_at(self, pos: Pos) -> Optional["Box"]: # type: ignore
    for box in self.boxes:
      if box.pos == pos:
        return box
    return None
  
  def _update_dimensions(self, pos: Pos):
    self.col_count = max(self.col_count, pos.col + 1)
    self.row_count = max(self.row_count, pos.row + 1)