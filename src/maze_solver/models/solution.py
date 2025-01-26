from dataclasses import dataclass

from maze_solver.models.square import Square

@dataclass(frozen=True)
class Solution:
    squares: tuple[Square, ...]