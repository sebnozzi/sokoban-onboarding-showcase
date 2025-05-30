from textwrap import dedent
from assertpy import assert_that
from common.level_io.formatting import format_level
from game_logic.game_controller import GameController


def assert_game_looks_like(game: GameController, expected_level_state: str):
  expected_level_state = dedent(expected_level_state).strip()
  actual_level = game.level
  actual_level_repr = format_level(actual_level)
  # Prepend '\n' so that the assertion is easier to read in case of error
  assert_that('\n' + actual_level_repr).described_as("level state").is_equal_to('\n' + expected_level_state)


def assert_all_boxes_are_placed(game: GameController):
  assert_that(game.level.boxes).is_not_empty()
  for box in game.level.boxes:
    assert_that(box.is_placed, f"box at {box.pos} should have been placed, but was not").is_true()


def assert_NO_box_is_placed(game: GameController):
  assert_that(game.level.boxes).is_not_empty()
  for box in game.level.boxes:
    assert_that(box.is_placed, f"box at {box.pos} should not be placed, but it was").is_false()
