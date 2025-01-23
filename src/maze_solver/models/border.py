from enum import IntFlag, auto

class Border(IntFlag):
    EMPY = 0
    TOP = auto()
    BOTTOM = auto()
    LEFT = auto()
    RIGHT = auto()