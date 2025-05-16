
Feature: Wall Constraining

  The worker should constrained by walls, not being able
  to pass through them when moving.

  In each case the worker is already next to a wall. Attempting
  to move past it should fail. The worker should remain in the
  starting position.

  Scenario: Worker cannot get past a wall moving right
    Given the game is showing this level:
    """
    #####
    #   #
    #  @#
    #   #
    #####
    """
    When I press the "right-arrow" key
    Then the level should look like this:
    """
    #####
    #   #
    #  @#
    #   #
    #####
    """

  Scenario: Worker cannot get past a wall moving left
    Given the game is showing this level:
    """
    #####
    #   #
    #@  #
    #   #
    #####
    """
    When I press the "left-arrow" key
    Then the level should look like this:
    """
    #####
    #   #
    #@  #
    #   #
    #####
      """

  Scenario: Worker cannot get past a wall moving down
    Given the game is showing this level:
    """
    #####
    #   #
    #   #
    # @ #
    #####
    """
    When I press the "down-arrow" key
    Then the level should look like this:
    """
    #####
    #   #
    #   #
    # @ #
    #####
    """

  Scenario: Worker cannot get past a wall moving up
    Given the game is showing this level:
    """
    #####
    # @ #
    #   #
    #   #
    #####
    """
    When I press the "up-arrow" key
    Then the level should look like this:
    """
    #####
    # @ #
    #   #
    #   #
    #####
    """
