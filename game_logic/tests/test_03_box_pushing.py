# Feature: Basic Box pushing
#
#   The worker can push a box only into a free position. That is: it cannot
#   be pushed into another box, or into a wall. Chain-reaction-pushes are not
#   allowed.
#
#   The worker itself can also not move into an unmovable box.

from support.setup_helpers import game_with_level
from support.custom_assertions import assert_game_looks_like
from game_logic.game_controller import (
  LEFT_ARROW_KEY,
  DOWN_ARROW_KEY,
  RIGHT_ARROW_KEY,
  UP_ARROW_KEY,
)


def test_pushing_box_into_free_position():
  # GIVEN: worker is next to a pushable box
  game = game_with_level("""
    #####
    #   #
    #@$ #
    #   #
    #####
    """)
  # WHEN: worker moves / pushes
  game.process_key(key_name=RIGHT_ARROW_KEY)
  # THEN: box (and worker) has moved
  assert_game_looks_like(game, """
    #####
    #   #
    # @$#
    #   #
    #####
    """)


def test_box_cannot_be_pushed_into_wall():
  # GIVEN: a box next to a wall on the left
  game = game_with_level("""
    #####
    #   #
    #$@ #
    #   #
    #####
    """)
  # WHEN
  game.process_key(key_name=LEFT_ARROW_KEY)
  # THEN
  assert_game_looks_like(game, """
    #####
    #   #
    #$@ #
    #   #
    #####
    """)


def test_a_box_cannot_push_another_box():
  # GIVEN: worker next to two boxes next to each other
  game = game_with_level("""
    #######
    #     #
    # @$$ #
    #     #
    #######
    """)
  # WHEN: worker tries to push
  game.process_key(key_name=RIGHT_ARROW_KEY)
  # THEN: box has not moved
  assert_game_looks_like(game, """
    #######
    #     #
    # @$$ #
    #     #
    #######
    """)
