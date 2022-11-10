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
        self.states_in_memory['visited'] = {tuple(grid)}

    def _solve_recursive(self, grid: Grid, depth: int) -> None:
        super()._solve_recursive(grid, depth)
        if depth > self.depth_limit:
            if self.stats:
                self.stats.dead_ends += 1
            return

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
            self._solve_recursive(new_grid, depth + 1)

            self.solution.pop()
            self.states_in_memory['visited'].remove(new_grid)
            child_count += 1

        if self.stats:
            if child_count == 0:
                self.stats.dead_ends += 1
            if self.stats.max_states_in_memory < len(self.states_in_memory['visited']):
                self.stats.max_states_in_memory = len(self.states_in_memory['visited'])
