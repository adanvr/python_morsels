from dataclasses import dataclass, astuple

@dataclass(frozen=True)
class Point:
    x: float
    y: float
    z: float
    def __iter__(self):
        yield from astuple(self)