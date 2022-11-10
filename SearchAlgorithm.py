import sys
import time

from Grid import Grid
from exceptions import TimeOut, OutOfMemory, SolutionFound


class SearchAlgorithm:

    def __init__(self, grid: Grid, time_limit: float, memory_limit: int = 1024 ** 3):
        self.grid = grid
        self.time_limit = time_limit
        self.memory_limit = memory_limit
        self.visited_states = {tuple(grid): 0}
        self.iterations = -1
        self.dead_ends = 0
        self.execution_time_start = None
        self.execution_time = None
        self.solution = []

    @property
    def unique_visited_states(self):
        result = set()
        for state, _ in self.visited_states.items():
            result.add(state)
        return result

    def _is_in_visited_states(self, grid: Grid, depth: int):
        visited_depth = self.visited_states.get(tuple(grid))
        return visited_depth is not None and depth >= visited_depth

    def solve(self):
        self.execution_time_start = time.time()
        try:
            self._solve_recursive(self.grid, 0)
        except TimeOut:
            print(f'Execution time exceeded {self.time_limit} second(s).')
        except OutOfMemory:
            print(f'Exceeded memory limit of {self.memory_limit} byte(s)')
        except SolutionFound:
            print('Solution found')
            self.execution_time = time.time() - self.execution_time_start
            return self.solution
        else:
            print('Solution not found')

    def _solve_recursive(self, grid: Grid, depth: int):
        self.iterations += 1
        if sys.getsizeof(self.visited_states) > self.memory_limit:
            raise OutOfMemory
        if time.time() - self.execution_time_start > self.time_limit:
            raise TimeOut
        if grid.check_correct_position():
            raise SolutionFound
