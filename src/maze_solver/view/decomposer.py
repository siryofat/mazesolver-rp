from maze_solver.models.border import Border
from maze_solver.view.primitives import(
    Point,
    Line,
    Primitive,
)

def decompose(border: Border, top_left: Point, square_size: int) -> Primitive:
    top_right: Point = top_left.translate(x=square_size)
    bottom_right: Point = top_left.translate(x=square_size, y=square_size)
    bottom_left: Point = top_left.translate(y=square_size)

    top = Line(top_left, top_right)
    bottom = Line(bottom_left, bottom_right)
    left = Line(top_left, bottom_left)
    right = Line(top_right, bottom_right)
