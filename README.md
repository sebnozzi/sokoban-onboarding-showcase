
# Sokoban (PyGame)

This project showcases a [Sokoban game][sokoban-link] game using PyGame.

The goal of this project is not so much to implement a Sokoban game in Python, 
but to explore ideas and techniques for **"codebase onboarding"**. That is: to make the codebase as approachable as possible for an hypothetical member of an hypothetical development team.

See ["Ideas Explored"](#ideas-explored) section below for more details.

[sokoban-link]: https://en.wikipedia.org/wiki/Sokoban

## Assumed Knowledge

This project makes use of the following libraries / tools:

* [PyGame](https://www.pygame.org) - for implementing the game
* [PyTest](https://pytest.org) - for testing
* [AssertPy](https://assertpy.github.io) - for test assertions

It is recommended that the developer becomes familiar with these technologies (in order to better understand and contribute to the codebase).

## Project Stucture

Important files and folders:

- [main.py](main.py) - This is the entry-point for the PyGame implementation
- [game_logic/](./game_logic/) - The model / game-logic is implemented here (see [game.py](./game_logic/game.py) and [level.py](./game_logic/level.py))

  - [tests/](./tests/) - The test-files which cover the game-logic

- [common/](./common/) - Common classes and models for the whole program

    - [level_io/](./common/level_io/) - Level formatting / parsing
    - [models/](./common/models/) - Common models like `Pos(ition)` or `Direction`

- [pygame_specific/](./pygame_specific/) - PyGame-specific aspects go here (e.g. rendering)

- [requirements.txt](requirements.txt) - Lists the required packages (see [Setup](#setup) below)

## Setup

To setup this project, be sure to follow these guides:

* [Create and activate a virtual environment][setup-1]
* [Install dependencies using `requirements.txt`][setup-2]

[setup-1]: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments

[setup-2]: https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#using-a-requirements-file

> IMPORTANT: do not attempt to run / test this project before completing the setup!

## Running

Run the game using:

```
python main.py
```

This should open a window, in which you can move the worker using the arrow keys.

## Testing

Run the tests using:

```
python -m pytest
```

---

## Ideas Explored

Ideas and techniques explored for "codebase onboarding" are:

* Have a useful starting point (i.e. this file)
* Explaining the project structure, providing further starting points
  * Linking to files / folders from Markdown, to leverage navigation features
* Not over-documenting, keeping documentation short and to the point
  * Encourage reading and getting out of the way
  * Use existing guides if possible (delegate / stay up-to-date)
* Mention assumed / required knowledge
* Separating code into meaningul modules
  * Separating model from implementation
* Documenting classes at least at the class-level
* Write long-lived comments
  * Don't write docstrings that are too specific and can become outdated
* Evaluating and discarding cucumber in favor to equally readable but more
  explorable in-code test files (using PyTest)
* Writing de-coupled, succint tests
  * Have short tests in general
  * Have readable tests
  * Only include what is relevant in the test
  * Structure a test in GIVEN / WHEN / THEN sections
  * Use custom setup / assertion helpers
  * Listing features numerically
  * Inherit from cucumber: describe feature on top of tile
* De-coupling tests from implementation
  * So that re-designs are encouraged and tests don't become liabilities
* Using good abstractions where it makes sense
* Keeping functions / methods short and focused

## PENDING FEATURES

- Reset the level
- Undo movement
- Worker orientation (initial, when moving, when undo)
