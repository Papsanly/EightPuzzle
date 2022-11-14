from __future__ import annotations
from dataclasses import dataclass
from Grid import Grid, Direction
from SearchAlgorithm import SearchAlgorithm
import heapq as hq


@dataclass
class SolutionNode:

    grid: Grid
    depth: int
    direction: Direction = None
    parent: SolutionNode = None

    def calc_heuristic(self) -> int:
        wrong_values_count = 0
        for value, correct_value in zip(self.grid, list(range(1, self.grid.size ** 2)) + [None]):
            if value is not correct_value:
                wrong_values_count += 1
        return self.depth + wrong_values_count

    def __lt__(self, other: SolutionNode) -> bool:
        return self.calc_heuristic() < other.calc_heuristic()


class AStar(SearchAlgorithm):

    def __init__(
            self,
            grid: Grid,
            time_limit: float = 1800,
            memory_limit: int = 1024 ** 3,
            stats: bool = True
    ) -> None:
        super().__init__(grid, time_limit, memory_limit, stats)
        self.grid = SolutionNode(grid, 0)
        self._states_in_memory['visited'] = {grid}
        self._states_in_memory['open'] = []
        self._solution_node = self.grid

    def _heap_pop(self) -> SolutionNode:
        return hq.heappop(self._states_in_memory['open'])

    def _use_solution(self):
        self.stats.max_states_in_memory = len(self.stats.all_generated_states)
        open_nodes_parents = set()
        for node in self._states_in_memory['open']:
            open_nodes_parents.add(node.parent.grid)
        self.stats.dead_ends += len(open_nodes_parents)

        while self._solution_node.parent is not None:
            self.solution.append(self._solution_node.direction)
            self._solution_node = self._solution_node.parent
        self.solution.reverse()

    def _solve_internal(self, node: SolutionNode, depth: int):
        while True:
            grid = node.grid
            self._solution_node = node
            super()._solve_internal(grid, depth)

            child_count = 0
            for new_grid, direction in self._get_extensions(grid):
                hq.heappush(
                    self._states_in_memory['open'],
                    SolutionNode(new_grid, node.depth + 1, direction, node),
                )
                self.stats.all_generated_states.add(new_grid)
                child_count += 1

            if self.stats and child_count == 0:
                self.stats.dead_ends += 1

            node = self._heap_pop()
