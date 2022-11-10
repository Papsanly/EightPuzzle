from Grid import Grid
from noninformed_search import LDFS
from informed_search import AStar


def main():
    grid = Grid.generate_solvable(400)
    grid = Grid((4, 8, 2, 5, None, 1, 3, 6, 7))
    print('\nGenerated grid:\n')
    print(grid, '\n')
    print('Solving...')
    algorithm = LDFS(grid, 30)
    solution = algorithm.solve()
    if solution is not None:
        print(f'\nSolving time: {round(algorithm.execution_time, 3)}s')
        print(f'Solution depth: {len(solution)}')
        print(f'Iterations:', algorithm.iterations)
        print(f'Dead ends:', algorithm.dead_ends)
        print(f'Visited states:', len(algorithm.unique_visited_states), '\n')
        print('Solution:\n')
        for direction in solution:
            grid.move(direction)
            print(f'Move: {direction.name.lower()}')
            print(grid, '\n')


if __name__ == '__main__':
    main()
