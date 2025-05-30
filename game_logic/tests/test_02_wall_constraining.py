# Feature: Wall Constraining
#
#   The worker should constrained by walls, not being able
#   to pass through them when moving.
#
#   In each case the worker is already next to a wall. Attempting
#   to move past it should fail. The worker should remain in the
#   starting position.

from support.setup_helpers import game_with_level
from support.custom_assertions import assert_game_looks_like
from game_logic.game_controller import (
  LEFT_ARROW_KEY,
  DOWN_ARROW_KEY,
  RIGHT_ARROW_KEY,
  UP_ARROW_KEY,
)


def test_worker_moves_right():
  # GIVEN
  game = game_with_level("""
    #####
    #   #
    #  @#
    #   #
    #####
    """)
  # WHEN
  game.process_key(key_name=RIGHT_ARROW_KEY)
  # THEN
  assert_game_looks_like(game, """
    #####
    #   #
    #  @#
    #   #
    #####
    """)


def test_worker_moves_left():
  # GIVEN
  game = game_with_level("""
    #####
    #   #
    #@  #
    #   #
    #####
    """)
  # WHEN
  game.process_key(key_name=LEFT_ARROW_KEY)
  # THEN
  assert_game_looks_like(game, """
    #####
    #   #
    #@  #
    #   #
    #####
    """)


def test_worker_moves_up():
  # GIVEN
  game = game_with_level("""
    #####
    # @ #
    #   #
    #   #
    #####
    """)
  # WHEN
  game.process_key(key_name=UP_ARROW_KEY)
  # THEN
  assert_game_looks_like(game, """
    #####
    # @ #
    #   #
    #   #
    #####
    """)


def test_worker_moves_down():
  # GIVEN
  game = game_with_level("""
    #####
    #   #
    #   #
    # @ #
    #####
    """)
  # WHEN
  game.process_key(key_name=DOWN_ARROW_KEY)
  # THEN
  assert_game_looks_like(game, """
    #####
    #   #
    #   #
    # @ #
    #####
    """)
