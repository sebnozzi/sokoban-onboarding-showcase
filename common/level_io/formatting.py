
from typing import List
from game_logic.level import Level


def format_level(level: Level) -> List[str]:
  """
  Gives back a textual representation of a level

  Opposite of parsing.
  """
  lines = []
  # Fill lines with empty spaces
  for _ in range(0, level.row_count):
    row_chars = []
    for _ in range(0, level.col_count):
      row_chars.append(' ')
    lines.append(row_chars)
  # Fill wall chars
  for wall_pos in level.walls:
    lines[wall_pos.row][wall_pos.col] = '#'
  # Fill goal chars
  for goal_pos in level.goals:
    lines[goal_pos.row][goal_pos.col] = '.'
  # Fill box chars
  for box in level.boxes:
    if box.is_placed:
      box_char = '*'
    else:
      box_char = '$'
    lines[box.pos.row][box.pos.col] = box_char
  # Fill worker char
  lines[level.worker.pos.row][level.worker.pos.col] = '@'
  # Now join char-array into a line (string)
  for i in range(0, len(lines)):
    lines[i] = ''.join(lines[i]).rstrip()
  # And finally join all lines
  lines = '\n'.join(lines)
  return lines