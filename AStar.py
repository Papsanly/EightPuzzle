from Grid import Grid
from SearchAlgorithm import SearchAlgorithm
import heapq as hq


class AStar(SearchAlgorithm):

    def __init__(
            self,
            grid: Grid,
            time_limit: float = 1800,
            memory_limit: int = 1024 ** 3
    ) -> None:
        super().__init__(grid, time_limit, memory_limit)
        self.open_states = []

    def _solve_recursive(self, grid: Grid, depth: int):
        super()._solve_recursive(grid, depth)
