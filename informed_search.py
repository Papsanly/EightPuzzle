from Grid import Grid
from SearchAlgorithm import SearchAlgorithm


class AStar(SearchAlgorithm):

    def __init__(
            self,
            grid: Grid,
            time_limit: float = 1800,
            memory_limit: int = 1024 ** 3
    ) -> None:
        super().__init__(grid, time_limit, memory_limit)

    def _solve_recursive(self, grid: Grid, depth: int):
        ...
