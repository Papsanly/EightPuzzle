from __future__ import annotations
from enum import Enum
from random import shuffle, choice, randint
from typing import Sequence
from exceptions import ImpossibleMove


class GridPosition(Enum):
    TOPLEFT = (0, 0)
    MIDTOP = (0, 1)
    TOPRIGHT = (0, 2)
    MIDLEFT = (1, 0)
    CENTER = (1, 1)
    MIDRIGHT = (1, 2)
    BOTTOMLEFT = (2, 0)
    MIDBOTTOM = (2, 1)
    BOTTOMRIGHT = (2, 2)


class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


class Grid(tuple[int | None]):
    size = 3

    def __new__(cls, *values: int | None):
        return super().__new__(cls, tuple(values))

    def __init__(self, *values: int | None) -> None:
        self.empty_position = self._index_to_position(self.index(None))

    @classmethod
    def generate_random(cls) -> Grid:
        values = [None] + list(range(1, cls.size * cls.size))
        shuffle(values)
        return Grid(*values)

    @classmethod
    def generate_solvable(cls, min_depth: int = 200, max_depth: int = 400) -> Grid:
        depth = randint(min_depth, max_depth)
        grid = Grid(*range(1, cls.size * cls.size), None)
        i = 0
        while i < depth:
            direction = choice(tuple(Direction))
            try:
                grid = grid.move(direction)
            except ImpossibleMove:
                pass
            else:
                i += 1
        return grid

    @classmethod
    def _index_to_position(cls, index: int) -> Sequence[int]:
        return index // cls.size, index % cls.size

    @classmethod
    def _position_to_index(cls, position: Sequence[int]) -> int:
        return cls.size * position[0] + position[1]

    def __getitem__(self, key: Sequence[int] | GridPosition | slice | int) -> int | Sequence[int]:
        getitem = super(Grid, self).__getitem__
        if isinstance(key, slice | int):
            return getitem(key)
        if isinstance(key, GridPosition):
            return getitem(self._position_to_index((key.value[0], key.value[1])))
        return getitem(self._position_to_index(key))

    def __str__(self) -> str:
        result = ''
        for i in range(self.size):
            result += '|'
            row = map(
                lambda x: " " if x is None else str(x),
                self[self.size * i:self.size * (i + 1)]
            )
            for j, value in enumerate(row):
                justify = len(str(self.size ** 2))
                if j != 0:
                    justify += 1
                result += str(value).rjust(justify)
            result += '|'
            if i != self.size - 1:
                result += '\n'
        return result

    def move(self, direction: Direction) -> Grid:
        result = list(self)
        new_empty_position = [
            self.empty_position[i] + direction.value[i]
            for i in range(2)
        ]
        if -1 in new_empty_position or self.size in new_empty_position:
            raise ImpossibleMove('Cannot move in this direction')
        move_value = self[new_empty_position]
        result[self._position_to_index(self.empty_position)] = move_value
        result[self._position_to_index(new_empty_position)] = None
        return Grid(*result)

    def is_solved(self) -> bool:
        return tuple(self) == tuple(range(1, self.size * self.size)) + (None,)
