# from itertools import product
from enum import Enum
from random import shuffle
from typing import Self, Iterable, Literal


class GridPosition(Enum):
    TOPLEFT = 'topleft'
    MIDTOP = 'midtop'
    TOPRIGHT = 'topright'
    MIDLEFT = 'midleft'
    CENTER = 'center'
    MIDRIGHT = 'midright'
    BOTTOMLEFT = 'bottomleft'
    MIDBOTTOM = 'midbottom'
    BOTTOMRIGHT = 'bottomright'


class Direction(Enum):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'


class Grid(list[int | None]):

    size = 3

    @classmethod
    def generate_random(cls) -> Self:
        length = cls.size * cls.size
        values = [None] + list(range(1, length))
        shuffle(values)
        return Grid(values)

    def __init__(self, values: Iterable) -> None:
        super().__init__()
        for value in values:
            self.append(value)

    def __setitem__(self, key: tuple[int, int] | GridPosition, value: int) -> None:
        super(Grid, self).__setitem__(self.size * key[0] + key[1], value)

    def __getitem__(self, key: tuple[int, int] | GridPosition | slice) -> int | list[int]:
        if isinstance(key, slice):
            return super(Grid, self).__getitem__(key)
        if isinstance(key, GridPosition):

        return super(Grid, self).__getitem__(self.size * key[0] + key[1])

    def __str__(self) -> str:
        result = ''
        for i in range(self.size):
            row = map(
                lambda x: " " if x is None else str(x),
                self[self.size * i:self.size * i + 3]
            )
            result += f'|{" ".join(row)}|\n'
        return result

    def move(self, direction: Direction) -> None:


if __name__ == '__main__':
    grid = Grid.generate_random()
    print(grid)
    print(grid[1, 2])
