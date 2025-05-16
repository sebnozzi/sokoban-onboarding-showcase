from behave import *
from assertpy import assert_that
from common.level_io.formatting import format_level
from common.level_io.parsing import parse_level
from game_logic.game import (
  Game, 
  LEFT_ARROW_KEY,
  DOWN_ARROW_KEY,
  RIGHT_ARROW_KEY,
  UP_ARROW_KEY,
)

@given(u'the game is showing this level')
def step_impl(context):
  level = parse_level(context.text)
  game = Game()
  game.set_level(level=level)
  context.game = game


@when(u'I press the "{test_key_name}" key')
def step_impl(context, test_key_name):
  key_map = {
    "up-arrow": UP_ARROW_KEY,
    "down-arrow": DOWN_ARROW_KEY,
    "left-arrow": LEFT_ARROW_KEY,
    "right-arrow": RIGHT_ARROW_KEY,
  }
  game_key_name = key_map[test_key_name]
  game: Game = context.game
  game.process_key(key_name=game_key_name)


@then(u'the level should look like this')
def step_impl(context):
  game: Game = context.game
  actual_level = game.level
  actual_level_repr = format_level(actual_level)
  expected_level_repr = context.text
  # Prepend '\n' so that the assertion is easier to read in case of error
  assert_that('\n' + actual_level_repr).described_as("level state").is_equal_to('\n' + expected_level_repr)
