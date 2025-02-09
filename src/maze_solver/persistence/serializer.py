import array
import pathlib

from maze_solver.models.maze import Maze
from maze_solver.models.square import Square
from maze_solver.models.border import Border
from maze_solver.models.role import Role
from maze_solver.persistence.file_format import FileBody, FileHeader

FORMAT_VERSION: int = 1

def dump(maze: Maze, path: pathlib.Path) -> None:
    header, body = serialize(maze)
    with path.open(mode='wb') as file:
        header.write(file)
        body.write(file)

def load(path: pathlib.Path) -> Maze:
    with path.open(mode='rb') as file:
        header = FileHeader.read(file)
        if header.format_version != FORMAT_VERSION:
            raise ValueError("Unsupported format version")
        body = FileBody.read(header, file)
        return deserialize(header,body)

def serialize(maze: Maze) -> tuple[FileHeader, FileBody]:
    header = FileHeader(FORMAT_VERSION, maze.width, maze.height)
    body = FileBody(array.array('B', map(compress, maze)))
    return header, body

def deserialize(header: FileHeader, body: FileBody) -> Maze:
    squares: list[Square] = []
    for index, square_value in enumerate(body.square_values):
        row, column = divmod(index, header.width)
        border, role = decompress(square_value)
        squares.append(Square(index, row, column, border, role))
    return Maze(tuple(squares))

def compress(square: Square) -> int:
    return (square.role << 4) | square.border.value

def decompress(square_value: int) -> tuple[Border, Role]:
    return Border(square_value & 0xf), Role(square_value >> 4)