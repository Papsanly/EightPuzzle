from typing import TypedDict

from Grid import Grid, Direction
from SearchAlgorithm import SearchAlgorithm


class LDFS(SearchAlgorithm):

    def __init__(
            self,
            grid: Grid,
            depth_limit: int,
            time_limit: float = 1800,
            memory_limit: int = 1024 ** 3,
            stats: bool = True
    ) -> None:
        super().__init__(grid, time_limit, memory_limit, stats)
        self.depth_limit = depth_limit
        self._states_in_memory['visited'] = {grid}

    def _solve_internal(self, grid: Grid, depth: int) -> None:
        super()._solve_internal(grid, depth)
        if depth >= self.depth_limit:
            if self.stats:
                self.stats.dead_ends += 1
            return

        child_count = 0
        for new_grid, direction in self._get_extensions(grid):
            self.solution.append(direction)
            self._solve_internal(new_grid, depth + 1)

            self.solution.pop()
            self._states_in_memory['visited'].remove(new_grid)
            child_count += 1

        if self.stats:
            if child_count == 0:
                self.stats.dead_ends += 1
            if self.stats.max_states_in_memory < len(self._states_in_memory['visited']):
                self.stats.max_states_in_memory = len(self._states_in_memory['visited'])
