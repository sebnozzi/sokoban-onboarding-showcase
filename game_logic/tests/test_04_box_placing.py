# Feature: Box placing / unplacing
#
#   A box can be pushed into a "goal" position. It then becomes "placed".
#
#   If already "placed" and pushed away to a normal "free space" it then 
#   becomes "unplaced".

from support.setup_helpers import game_with_level
from support.custom_assertions import (
  assert_game_looks_like,
  assert_NO_box_is_placed,
  assert_all_boxes_are_placed,
)
from game_logic.game_controller import (
  LEFT_ARROW_KEY,
  DOWN_ARROW_KEY,
  RIGHT_ARROW_KEY,
  UP_ARROW_KEY,
)


def test_box_placing_into_goal_position():
  # GIVEN: game with worker about to push/place a box
  game = game_with_level("""
    #####
    #  .#
    #@$.#
    #   #
    #####
    """)
  # WHEN: worker pushes and places box
  game.process_key(key_name=RIGHT_ARROW_KEY)
  # THEN: level should show box being placed
  assert_all_boxes_are_placed(game)
  assert_game_looks_like(game, """
    #####
    #  .#
    # @*#
    #   #
    #####
    """)


def test_unplacing_box_from_goal_position():
  # GIVEN: worker in position to push a placed box out of goal
  game = game_with_level("""
    #####
    # @.#
    # *.#
    #   #
    #####
    """)
  # WHEN: worker pushes and un-places box
  game.process_key(key_name=DOWN_ARROW_KEY)
  # THEN: level should show box NOT placed
  assert_NO_box_is_placed(game)
  assert_game_looks_like(game, """
    #####
    #  .#
    # @.#
    # $ #
    #####
    """)
