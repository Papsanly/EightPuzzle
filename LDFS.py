from copy import copy
from Grid import Grid, Direction
from SearchAlgorithm import SearchAlgorithm
from exceptions import ImpossibleMove


class LDFS(SearchAlgorithm):

    def __init__(
            self,
            grid: Grid,
            depth_limit: int,
            time_limit: float = 1800,
            memory_limit: int = 1024 ** 3
    ) -> None:
        super().__init__(grid, time_limit, memory_limit)
        self.depth_limit = depth_limit

    def _solve_recursive(self, grid: Grid, depth: int) -> None:
        super()._solve_recursive(grid, depth)
        if depth > self.depth_limit:
            self.dead_ends += 1
            return

        child_count = 0
        for direction in Direction:
            try:
                grid_copy = copy(grid)
                grid_copy.move(direction)
            except ImpossibleMove:
                continue
            if self._is_in_visited_states(grid_copy, depth):
                continue

            self.states_in_memory['visited'][tuple(grid_copy)] = depth
            self.solution.append(direction)
            self._solve_recursive(grid_copy, depth + 1)

            self.solution.pop()
            child_count += 1

        if child_count == 0:
            self.dead_ends += 1
