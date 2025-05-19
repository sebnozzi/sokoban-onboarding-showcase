
Feature: Basic Box pushing

  The worker can push a box only into a free position. That is: it cannot
  be pushed into another box, or into a wall. Chain-reaction-pushes are not
  allowed.

  The worker itself can also not move into an unmovable box.

  Scenario: The worker pushes a box into a free position.
    Given the game is showing this level:
    """
    #####
    #   #
    #@$ #
    #   #
    #####
    """
    When I press the "right-arrow" key
    Then the level should now look like this:
    """
    #####
    #   #
    # @$#
    #   #
    #####
    """

  Scenario: A box cannot be pushed into a wall
    Given the game is showing this level:
    """
    #####
    #   #
    #$@ #
    #   #
    #####
    """
    When I press the "left-arrow" key
    Then the level should still look the same


  Scenario: A box cannot push another box
    Given the game is showing this level:
    """
    #######
    #     #
    # @$$ #
    #     #
    #######
    """
    When I press the "right-arrow" key
    Then the level should still look the same
