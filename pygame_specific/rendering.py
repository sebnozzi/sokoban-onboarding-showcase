from pygame import Surface, Rect
from common.models.position import Pos
from game_logic.box import Box
from game_logic.level import Level
from game_logic.worker import Worker

CELL_SIZE = 40
WALL_COLOR = "red"
WORKER_COLOR = "blue"
UNPLACED_BOX_COLOR = "orange3"
PLACED_BOX_COLOR = "orange1"
GOAL_SPACE = "olivedrab3"


def render_level(screen: Surface, level: Level):
  _render_walls(screen, level)
  _render_goals(screen, level)
  _render_boxes(screen, level)
  _render_worker(screen, level.worker)


def _render_walls(screen, level):
    for wall_pos in level.walls:
      wall_pos: Pos
      _render_cell(screen, wall_pos, WALL_COLOR)


def _render_goals(screen, level):
    for goal_pos in level.goals:
      goal_pos: Pos
      _render_cell(screen, goal_pos, GOAL_SPACE)


def _render_boxes(screen, level):
    for box in level.boxes:
      box: Box
      box_pos: Pos = box.pos
      if box.is_placed:
         box_color = PLACED_BOX_COLOR
      else:
         box_color = UNPLACED_BOX_COLOR
      _render_cell(screen, box_pos, box_color)


def _render_worker(screen, worker: Worker):
    _render_cell(screen, worker.pos, WORKER_COLOR)


def _render_cell(screen: Surface, pos: Pos, color):
  left = pos.col * CELL_SIZE
  top = pos.row * CELL_SIZE
  screen.fill(color, rect=Rect(left, top, CELL_SIZE, CELL_SIZE))
