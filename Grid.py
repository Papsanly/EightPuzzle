from enum import Enum
from random import shuffle
from typing import Self, Iterable, Sequence


class ImpossibleMove(Exception):
    pass


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


class Grid(list[int | None]):
    size = 3

    @classmethod
    def generate_random(cls) -> Self:
        length = cls.size * cls.size
        values = [None] + list(range(1, length))
        shuffle(values)
        return Grid(values)

    @classmethod
    def _index_to_position(cls, index: int) -> Sequence[int]:
        return index // cls.size, index % cls.size

    @classmethod
    def _position_to_index(cls, row: int, column: int) -> int:
        return cls.size * row + column

    def __init__(self, values: Iterable[int | None]) -> None:
        super().__init__()
        for value in values:
            self.append(value)
        self.empty_position = self._index_to_position(self.index(None))

    def __setitem__(self, key: Iterable[int] | GridPosition, value: int | None) -> None:
        setitem = super(Grid, self).__setitem__
        if isinstance(key, GridPosition):
            setitem(self._position_to_index(key.value[0], key.value[1]), value)
        setitem(self._position_to_index(*key), value)

    def __getitem__(self, key: Iterable[int] | GridPosition | slice) -> int | Sequence[int]:
        getitem = super(Grid, self).__getitem__
        if isinstance(key, slice):
            return getitem(key)
        if isinstance(key, GridPosition):
            return getitem(self._position_to_index(key.value[0], key.value[1]))
        return getitem(self._position_to_index(*key))

    def __str__(self) -> str:
        result = ''
        for i in range(self.size):
            row = map(
                lambda x: " " if x is None else str(x),
                self[self.size * i:self.size * (i + 1)]
            )
            result += f'|{" ".join(row)}|\n'
        return result

    def move(self, direction: Direction) -> None:
        new_empty_position = [
            self.empty_position[i] - direction.value[i]
            for i in range(2)
        ]
        if -1 in new_empty_position or 3 in new_empty_position:
            raise ImpossibleMove('Cannot move in this direction')
        move_value = self[new_empty_position]
        self[self.empty_position] = move_value
        self[new_empty_position] = None
        self.empty_position = new_empty_position
