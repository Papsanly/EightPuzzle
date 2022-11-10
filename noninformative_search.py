import sys
import time
from copy import copy
from Grid import Grid, Direction, ImpossibleMove


class TimeOut(Exception):
    pass


class OutOfMemory(Exception):
    pass


class SolutionFound(Exception):
    pass


class LDFS:

    def __init__(
            self,
            grid: Grid,
            depth_limit: int,
            time_limit: float = 1800,
            memory_limit: int = 1024 ** 3
    ) -> None:
        self.grid = grid
        self.depth_limit = depth_limit
        self.time_limit = time_limit
        self.memory_limit = memory_limit
        self.visited_states = {tuple(grid): 0}
        self.iterations = -1
        self.dead_ends = 0
        self.execution_time_start = None
        self.solution = []

    def is_in_visited_states(self, grid: Grid, depth: int):
        visited_depth = self.visited_states.get(tuple(grid))
        return visited_depth is not None and depth >= visited_depth

    @property
    def unique_visited_states(self):
        result = set()
        for state, _ in self.visited_states.items():
            result.add(state)
        return result

    def solve(self) -> list[Direction] | None:
        self.execution_time_start = time.time()
        try:
            self._solve_recursive(self.grid, 0)
        except TimeOut:
            print(f'Execution time exceeded {self.time_limit} second(s).')
        except OutOfMemory:
            print(f'Exceeded memory limit of {self.memory_limit} byte(s)')
        except SolutionFound:
            print('Solution found')
            return self.solution
        else:
            print('Solution not found')

    def _solve_recursive(self, grid: Grid, depth: int) -> None:
        self.iterations += 1
        if sys.getsizeof(self.visited_states) > self.memory_limit:
            raise OutOfMemory
        if time.time() - self.execution_time_start > self.time_limit:
            raise TimeOut
        if depth > self.depth_limit:
            self.dead_ends += 1
            return
        if grid.check_correct_position():
            self.execution_time = time.time() - self.execution_time_start
            raise SolutionFound
        child_count = 0
        for direction in Direction:
            try:
                grid_copy = copy(grid)
                grid_copy.move(direction)
            except ImpossibleMove:
                pass
            else:
                if self.is_in_visited_states(grid_copy, depth):
                    continue
                child_count += 1
                self.visited_states[tuple(grid_copy)] = depth
                self.solution.append(direction)
                self._solve_recursive(grid_copy, depth + 1)
                self.solution.pop()
        if child_count == 0:
            self.dead_ends += 1
