from Grid import Grid, Direction
from SearchAlgorithm import SearchAlgorithm
from exceptions import ImpossibleMove


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
        self.states_in_memory['visited'] = {grid}

    def _solve_internal(self, grid: Grid, depth: int) -> None:
        super()._solve_internal(grid, depth)
        if depth >= self.depth_limit:
            if self.stats:
                self.stats.dead_ends += 1
            return

        if depth == 23:
            pass

        child_count = 0
        for direction in Direction:
            try:
                new_grid = grid.move(direction)
            except ImpossibleMove:
                continue
            if new_grid in self.states_in_memory['visited']:
                continue

            self.states_in_memory['visited'].add(new_grid)
            if self.stats:
                self.stats.total_visited_states.add(new_grid)
            self.solution.append(direction)
            self._solve_internal(new_grid, depth + 1)

            self.solution.pop()
            self.states_in_memory['visited'].remove(new_grid)
            child_count += 1

        if self.stats:
            if child_count == 0:
                self.stats.dead_ends += 1
            if self.stats.max_states_in_memory < len(self.states_in_memory['visited']):
                self.stats.max_states_in_memory = len(self.states_in_memory['visited'])
