from dataclasses import dataclass
from typing import Iterator
from functools import reduce

from maze_solver.models.square import Square
from maze_solver.models.role import Role

@dataclass(frozen=True)
class Solution:
    squares: tuple[Square, ...]

    def __post_init__(self) -> None:
        assert self.squares[0].role is Role.ENTRANCE, "First square is not entrance."
        assert self.squares[-1].role is Role.EXIT, "Last square is not exit."
        reduce(validate_corridor, self.squares)

    def __iter__(self) -> Iterator[Square]:
        return iter(self.squares)

    def __getitem__(self, index:int) -> Square:
        return self.squares[index]

    def __len__(self) -> int:
        return len(self.squares)


def validate_corridor(current: Square, following: Square) -> Square:
    assert any([
        current.row == following.row,
        current.column == following.column
    ]), "Secuencial squares must lie in the same row or column."
    return following