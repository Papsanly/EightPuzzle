from Grid import Grid
from SearchAlgorithm import SearchAlgorithm
import heapq as hq


class AStar(SearchAlgorithm):

    def __init__(
            self,
            grid: Grid,
            time_limit: float = 1800,
            memory_limit: int = 1024 ** 3,
            stats: bool = True
    ) -> None:
        super().__init__(grid, time_limit, memory_limit, stats)
        self.states_in_memory['open'] = {grid}

    def _solve_internal(self, grid: Grid, depth: int = 0):
        super()._solve_internal(grid, 0)
