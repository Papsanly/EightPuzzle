import sys
import time
from Grid import Grid
from exceptions import TimeOut, OutOfMemory, SolutionFound


class AlgortithmStats:
    iterations: int = 0
    dead_ends: int = 0
    execution_time_start: int = None
    execution_time: int = None
    total_visited_states: int = 1


class SearchAlgorithm:

    def __init__(self, grid: Grid, time_limit: float, memory_limit: int = 1024 ** 3):
        self.grid = grid
        self.time_limit = time_limit
        self.memory_limit = memory_limit
        self.states_in_memory = {'visited': {tuple(grid): 0}}
        self.solution = []
        self.stats = AlgortithmStats()

    def _is_in_visited_states(self, grid: Grid, depth: int):
        visited_depth = self.states_in_memory['visited'].get(tuple(grid))
        return visited_depth is not None and depth >= visited_depth

    def solve(self):
        self.stats.execution_time_start = time.time()
        try:
            self._solve_recursive(self.grid, 0)
        except TimeOut:
            print(f'Execution time exceeded {self.time_limit} second(s).')
        except OutOfMemory:
            print(f'Exceeded memory limit of {self.memory_limit} byte(s)')
        except SolutionFound:
            print('Solution found')
            self.stats.execution_time = time.time() - self.stats.execution_time_start
            return self.solution
        else:
            print('Solution not found')

    def _solve_recursive(self, grid: Grid, depth: int):
        if sys.getsizeof(self.states_in_memory) > self.memory_limit:
            raise OutOfMemory
        if time.time() - self.stats.execution_time_start > self.time_limit:
            raise TimeOut
        if grid.check_correct_position():
            raise SolutionFound
        self.stats.iterations += 1
