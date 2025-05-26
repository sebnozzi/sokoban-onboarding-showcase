
Feature: Box placing / unplacing

  A box can be pushed into a "goal" position. It then becomes "placed".

  If already "placed" and pushed away to a normal "free space" it then 
  becomes "unplaced".

  Scenario: The worker pushes a box into a "goal" position.
    Given the game is showing this level:
    """
    #####
    #  .#
    #@$.#
    #   #
    #####
    """
    When I press the "right-arrow" key
    Then the level should now look like this:
    """
    #####
    #  .#
    # @*#
    #   #
    #####
    """
