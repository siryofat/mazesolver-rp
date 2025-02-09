import array
import pathlib

from maze_solver.models.maze import Maze
from maze_solver.models.square import Square
from maze_solver.persistence.file_format import FileBody, FileHeader

FORMAT_VERSION: int = 1

def dump(maze: Maze, path: pathlib.Path) -> None:
    header, body = serialize(maze)
    with path.open(mode='wb') as file:
        header.write(file)
        body.write(file)

def serialize(maze: Maze) -> tuple[FileHeader, FileBody]:
    header = FileHeader(FORMAT_VERSION, maze.width, maze.height)
    body = FileBody(array.array('B', map(compress, maze)))
    return header, body

def compress(square: Square) -> int:
    return (square.role << 4) | square.border.value