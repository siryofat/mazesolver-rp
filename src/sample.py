from pathlib import Path

from maze_solver.models.border import Border
from maze_solver.models.role import Role
from maze_solver.models.maze import Maze
from maze_solver.models.solution import Solution
from maze_solver.models.solution import Square
from maze_solver.view.renderer import SVGRenderer

maze = Maze(
    squares=(
        Square(0, 0, 0, Border.TOP | Border.LEFT),
        Square(1, 0, 1, Border.TOP | Border.RIGHT),
        Square(2, 0, 2, Border.LEFT | Border.RIGHT, Role.EXIT),
        Square(3, 0, 3, Border.TOP | Border.LEFT | Border.RIGHT),
        Square(4, 1, 0, Border.BOTTOM | Border.LEFT | Border.RIGHT),
        Square(5, 1, 1, Border.LEFT | Border.RIGHT),
        Square(6, 1, 2, Border.BOTTOM | Border.LEFT),
        Square(7, 1, 3, Border.RIGHT),
        Square(8, 2, 0, Border.TOP | Border.LEFT, Role.ENTRANCE),
        Square(9, 2, 1, Border.BOTTOM),
        Square(10, 2, 2, Border.TOP | Border.BOTTOM),
        Square(11, 2, 3, Border.BOTTOM | Border.RIGHT),
    )
)

solution = Solution(squares=tuple(maze[i] for i in (8, 11, 7, 6, 2)))
svg = SVGRenderer().render(maze)

with Path("maze.svg").open(mode="w", encoding="utf-8") as file:
    file.write(svg.xml_content)