from dataclasses import dataclass

@dataclass(frozen=True)
class SVGRenderer:
    square_size: int = 100
    line_width: int = 6

    @property
    def offset(self):
        self.line_width // 2