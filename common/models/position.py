from typing import Tuple

from common.models.direction import Direction


class Pos:
  """A position. Used within a level."""

  def __init__(self, col, row):
    self.col = col
    self.row = row

  def __eq__(self, other):
      if isinstance(other, Pos):
          return (self.col, self.row) == (other.col, other.row)
      return NotImplemented

  def __repr__(self) -> str:
     return f"Pos(col={self.col},row={self.row})"

  def neighbour_at(self, direction: Direction) -> "Pos":
    offset = direction.offset
    return self.plus_offset(offset)

  def plus_offset(self, offset: Tuple[int, int]) -> "Pos":
    """Returns a new position with offset added"""
    new_pos = Pos(col=self.col, row=self.row)
    new_pos.col += offset[0]
    new_pos.row += offset[1]
    return new_pos