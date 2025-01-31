from dataclasses import dataclass

from maze_solver.models.maze import Maze
from maze_solver.models.solution import Solution
from maze_solver.view.primitives import tag, Rect

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
        margins = 2 * (self.offset + self.line_width)
        width = margins + maze.width * self.square_size
        height = margins + maze.height * self.square_size
        return SVG(
            tag(
                'svg',
                self._get_body(maze, solution),
                xmlns="http.www.w3.org/2000/svg"
                stroke_linejoin="round",
                width=width,
                height=height,
                viewBox=f'0 0 {width} {height}',
            )
        )

    def _get_body(self, maze: Maze, solution: Solution | None = None) -> str:
        return "".join([
            arrow_marker(),
            background(),
            *map(self._draw_square, maze),
            self._draw_solution(solution) if solution else "",
        ])


def arrow_marker() -> str:
    return tag(
        "defs",
        tag(
            "marker",
            tag(
                "path",
                d="M 0,0 L 10,5 L 0,10 2,5 z",
                fill="red",
                fill_opacity="50%",
            ),
            id = "arrow",
            viewBox = "0 0 20 20",
            refX = "2",
            refY = "5",
            markerUnits = "strokeWidth",
            markerWidth = "10",
            markerHeight = "10",
            orient = "auto",
        )
    )


def background() -> str:
    return Rect().draw(width = "100%", heigth = "100%", fill = "white")