
Feature: Basic Movement

  The worker should be able to be moved within free 
  spaces using the arrow keys.

  Scenario: Worker moves right
    Given the game is showing this level:
    """
    #####
    #   #
    # @ #
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

  Scenario: Worker moves left
    Given the game is showing this level:
    """
    #####
    #   #
    # @ #
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

  Scenario: Worker moves down
    Given the game is showing this level:
    """
    #####
    #   #
    # @ #
    #   #
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

  Scenario: Worker moves up
    Given the game is showing this level:
    """
    #####
    #   #
    # @ #
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
