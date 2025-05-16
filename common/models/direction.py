
from typing import Tuple


class Direction:
  """
  A direction in which objects could be moving
  """

  def __init__(self, offset: Tuple[int, int]):
    self.offset = offset

# == Pre-defined constants for possible directions

LEFT  = Direction(offset=(-1,  0))
RIGHT = Direction(offset=( 1,  0))
UP    = Direction(offset=( 0, -1))
DOWN  = Direction(offset=( 0,  1))
