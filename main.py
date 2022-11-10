from Grid import Grid
from LDFS import LDFS
from AStar import AStar


def main():
    grid = Grid((1, 5, None, 7, 8, 6, 2, 3, 4))
    print('\nGenerated grid:\n')
    print(grid, '\n')
    print('Solving...')
    algorithm = LDFS(grid, 30)
    solution = algorithm.solve()
    if solution is not None:
        print(f'\nSolving time: {round(algorithm.stats.execution_time, 3)}s')
        print(f'Solution depth: {len(solution)}')
        print(f'Iterations:', algorithm.stats.iterations)
        print(f'Dead ends:', algorithm.stats.dead_ends)
        print(f'Visited states:', algorithm.stats.total_visited_states, '\n')
        print('Solution:\n')
        for direction in solution:
            grid = grid.move(direction)
            print(f'Move: {direction.name.lower()}')
            print(grid, '\n')


if __name__ == '__main__':
    main()
