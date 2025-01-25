from dataclasses import dataclass
from typing import Iterator
from functools import cached_property

from maze_solver.models.square import Square

@dataclass(frozen=True)
class Maze:
    squares: tuple[Square, ...] #It's a tuple and not a list to allow cacheing.

    def __post_init__(self) -> None:
        validate_indices(self)
        validate_rows_columns(self)

    def __iter__(self) -> Iterator[Square]:
        return iter(self.squares)

    def __getitem__(self, index: int) -> Square:
        return self.squares[index]

    @cached_property
    def width(self):
        return max(square.column for square in self) + 1

    @cached_property
    def height(self):
        return max(square.row for square in self) + 1


def validate_indices(maze: Maze) -> None:
    """Checks if index is a sequence of numbers up to the length of the Maze.
    """
    assert [square.index for square in maze ] == list(range(len(maze.squares))), "Wrong square.index"


def validate_rows_columns(maze: Maze) -> None:
    """Checks if each square has a valid row and column that matches an index.
    """
    for y in range(maze.height):
        for x in range(maze.width):
            square = maze[y * maze.width + x]
            assert square.row == y, "Wrong square.row"
            assert square.column == x, "Wrong square.column"