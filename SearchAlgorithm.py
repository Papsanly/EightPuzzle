import sys
import time
from dataclasses import dataclass

from Grid import Grid, Direction
from exceptions import TimeOut, OutOfMemory, SolutionFound, ImpossibleMove


@dataclass
class AlgortithmStats:
    all_generated_states: set[Grid]
    iterations: int = 0
    dead_ends: int = 0
    execution_time: int = None
    max_states_in_memory: int = 1


class SearchAlgorithm:

    def __init__(self, grid: Grid, time_limit: float, memory_limit: int, stats: bool):
        self.grid = grid
        self.time_limit = time_limit
        self.memory_limit = memory_limit
        self._states_in_memory = {}
        self.solution = []
        self._execution_time_start = None
        self.stats = None
        if stats:
            self.stats = AlgortithmStats({grid})

    def solve(self):
        self._execution_time_start = time.time()
        try:
            self._solve_internal(self.grid, 0)
        except TimeOut:
            print(f'Execution time exceeded {self.time_limit} second(s).')
        except OutOfMemory:
            print(f'Exceeded memory limit of {self.memory_limit} byte(s)')
        except SolutionFound:
            print('Solution found')
            if self.stats:
                self.stats.execution_time = time.time() - self._execution_time_start
            return self.solution
        else:
            print('Solution not found')

    def _get_extensions(self, grid: Grid) -> tuple[Grid, Direction]:
        for direction in Direction:
            try:
                new_grid = grid.move(direction)
            except ImpossibleMove:
                continue
            if new_grid in self._states_in_memory['visited']:
                continue
            yield new_grid, direction

    def _use_solution(self):
        pass

    def _solve_internal(self, grid: Grid, depth: int):
        if sys.getsizeof(self._states_in_memory) > self.memory_limit:
            raise OutOfMemory
        if time.time() - self._execution_time_start > self.time_limit:
            raise TimeOut
        if grid.is_solved():
            self._use_solution()
            raise SolutionFound
        if self.stats:
            self.stats.iterations += 1
            self.stats.all_generated_states.add(grid)
        self._states_in_memory['visited'].add(grid)
