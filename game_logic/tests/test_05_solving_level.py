# Feature: Solving level
#
#   The level is solved when all boxes are placed.
#
#   Conversely, a level where NOT ALL boxes are placed is NOT 
#   solved (yet).

from support.setup_helpers import game_with_level
from support.custom_assertions import (
  assert_game_looks_like,
  assert_NO_box_is_placed,
  assert_all_boxes_are_placed,
)
from assertpy import assert_that
from game_logic.game_controller import (
  LEFT_ARROW_KEY,
  DOWN_ARROW_KEY,
  RIGHT_ARROW_KEY,
  UP_ARROW_KEY,
)


def test_level_not_solved_because_only_one_box_placed():
  # GIVEN: game where one box can be placed
  game = game_with_level("""
    #####
    # $.#
    #@$.#
    #   #
    #####
    """)
  # WHEN: worker pushes and places only one box
  game.process_key(key_name=RIGHT_ARROW_KEY)
  # THEN: level is not solved because one box is not placed
  assert_that(game.is_solved, "Level should NOT be solved").is_false()


def test_level_solved_because_all_boxes_are_placed():
  # GIVEN: game where last box can be placed
  game = game_with_level("""
    #####
    #  *#
    #@$.#
    #   #
    #####
    """)
  # WHEN: worker pushes and places last box
  game.process_key(key_name=RIGHT_ARROW_KEY)
  # THEN: level is solved because all boxes are placed
  assert_that(game.is_solved, "Level should be solved").is_true()
