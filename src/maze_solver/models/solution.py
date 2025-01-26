from dataclasses import dataclass
from typing import Iterator

from maze_solver.models.square import Square

@dataclass(frozen=True)
class Solution:
    squares: tuple[Square, ...]

    def __iter__(self) -> Iterator[Square]:
        return iter(self.squares)

    def __getitem__(self, index:int) -> Square:
        return self.squares[index]

    def __len__(self) -> int:
        return len(self.squares)
