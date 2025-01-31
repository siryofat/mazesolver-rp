from dataclasses import dataclass

from maze_solver.models.maze import Maze
from maze_solver.models.solution import Solution

@dataclass(frozen=True)
class SVG:
    xml_content: str


@dataclass(frozen=True)
class SVGRenderer:
    square_size: int = 100
    line_width: int = 6

    @property
    def offset(self):
        self.line_width // 2

    def render(self, maze: Maze, solution: Solution | None = None) -> SVG:
        ...