from common.models.direction import Direction
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
    self.boxes: List[Pos] = []
    self.worker: Worker = None
    self.row_count = 0
    self.col_count = 0

  def add_wall(self, pos: Pos):
    self.walls.append(pos)
    self._update_dimensions(pos)

  def add_unplaced_box(self, pos: Pos):
    self.boxes.append(pos)

  def add_worker(self, pos: Pos):
    from game_logic.worker import Worker
    self.worker = Worker(level=self, initial_pos=pos)

  def has_free_space_at(self, pos: Pos) -> bool:
    return not (self.has_wall_at(pos) 
                or self.has_box_at(pos))

  def has_wall_at(self, pos: Pos) -> bool:
    return any(wall_pos == pos 
               for wall_pos in self.walls)
  
  def has_box_at(self, pos: Pos) -> bool:
    return any(box_pos == pos 
               for box_pos in self.boxes)
  
  def has_pushable_box_at(self, pos: Pos, direction: Direction) -> bool:
    return self.has_box_at(pos) and self._box_can_be_pushed(pos, direction)
  
  def perform_box_push(self, box_pos: Pos, direction: Direction):
    if self.has_pushable_box_at(box_pos, direction):
      # Remove box being pushed
      self.boxes = [box for box in self.boxes if box != box_pos]
      # Now add "pushed box"
      target_pos = box_pos.neighbour_at(direction)
      self.boxes.append(target_pos)

  def _box_can_be_pushed(self, box_pos: Pos, direction: Direction) -> bool:
    box_target_cell = box_pos.neighbour_at(direction)
    return self.has_free_space_at(box_target_cell)

  def _update_dimensions(self, pos: Pos):
    self.col_count = max(self.col_count, pos.col + 1)
    self.row_count = max(self.row_count, pos.row + 1)