from typing import NamedTuple, Protocol

class Primitive(Protocol):
    def draw(self, **attributes) -> str:
        ...


class Point(NamedTuple):
    x: int
    y: int

    def draw(self, **attributes) -> str:
        return f'{self.x},{self.y}'

    def translate(self, x=0, y=0) -> 'Point':
        return Point(self.x + x, self.y + y)


class Line(NamedTuple):
    start: Point
    end: Point

    def draw(self, **attributes):
        return tag(
            'line',
            x1 = self.start.x,
            y1 = self.start.y,
            x2 = self.end.x,
            y2 = self.end.y,
            **attributes,
        )


class Polyline(tuple[Point, ...]):
    def draw(self, **attributes) -> str:
        points = ' '.join(point.draw() for point in self)
        return tag('polyline', points=points, **attributes)


class Polygon(tuple[Point, ...]):
    def draw(self, **attributes) -> str:
        points = ' '.join(point.draw() for point in self)
        return tag('polygon', points=points, **attributes)

def tag(name: str, value: str | None = None, **attributes) -> str:
    attrs = "" if not attributes else " " + " ".join(
        f'{key.replace("_", "-")}="{value}"' for key, value in attributes.items()
    )
    if value is None:
        return f'<{name}{attrs} />'
    return f'<{name}{attrs}>{value}</{name}>'