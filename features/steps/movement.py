from behave import *
from assertpy import assert_that
from common.level_io.formatting import format_level
from common.level_io.parsing import parse_level
from game_logic.game import Game


@given(u'the game is showing this level')
def step_impl(context):
  level = parse_level(context.text)
  game = Game()
  game.set_level(level=level)
  context.game = game


@when(u'I press the "{key_name}" key')
def step_impl(context, key_name):
  game: Game = context.game
  game.process_key(key_name=key_name)


@then(u'the level should look like this')
def step_impl(context):
  game: Game = context.game
  actual_level = game.level
  actual_level_repr = format_level(actual_level)
  expected_level_repr = context.text
  # Prepend '\n' so that the assertion is easier to read in case of error
  assert_that('\n' + actual_level_repr).described_as("level state").is_equal_to('\n' + expected_level_repr)
