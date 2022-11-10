from Grid import Grid
from LDFS import LDFS
from AStar import AStar


def main():
    grid = Grid((8, 4, 5, 2, 3, 7, 6, 1, None))
    print('\nGenerated grid:\n')
    print(grid, '\n')
    print('Solving...')
    algorithm = LDFS(grid, 30)
    solution = algorithm.solve()
    if solution is not None:
        if algorithm.stats:
            print(f'\nSolving time: {round(algorithm.stats.execution_time, 3)}s')
            print(f'Solution depth: {len(solution)}')
            print(f'Iterations:', algorithm.stats.iterations)
            print(f'Dead ends:', algorithm.stats.dead_ends)
            print(f'Total visited states:', len(algorithm.stats.total_visited_states))
            print(f'States in memory:', algorithm.stats.max_states_in_memory)
        print('\nSolution:\n')
        for direction in solution:
            grid = grid.move(direction)
            print(f'Move: {direction.name.lower()}')
            print(grid, '\n')


if __name__ == '__main__':
    main()
