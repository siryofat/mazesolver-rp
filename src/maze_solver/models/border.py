from enum import IntFlag, auto

class Border(IntFlag):
    EMPY = 0
    TOP = auto()
    BOTTOM = auto()
    LEFT = auto()
    RIGHT = auto()

    @property
    def corner(self) -> bool:
        """bool: Returns if a square is a corner.

        If a square has either combination of Top-Left/Right or Bottom-Left/Right,
        it means it is a corner.
        """
        return self in (
            self.TOP | self.LEFT,
            self.TOP | self.RIGHT,
            self.BOTTOM | self.LEFT,
            self.BOTTOM | self.RIGHT,
        )

    @property
    def dead_end(self) -> bool:
        return self.bit_count() == 3

    @property
    def intersection(self) -> bool:
        return self.bit_count() < 2

border = Border(1)
print(border.intersection)