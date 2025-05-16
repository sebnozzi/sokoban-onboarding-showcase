from common.models.position import Pos
from game_logic.level import Level
from textwrap import dedent


def parse_level(level_block: str) -> Level:
  """
  Parses a level from a textual representation
  """
  level_block = dedent(level_block)
  lines = [line for line in level_block.split("\n") if line != '']
  level = Level()
  for row_nr, line in enumerate(lines):
    for col_nr, char in enumerate(line):
      pos = Pos(col=col_nr, row=row_nr)
      if char == '#':
          level.add_wall(pos)
      elif char == '@':
          level.add_worker(pos)
  return level
