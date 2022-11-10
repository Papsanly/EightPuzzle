from Grid import Grid
from noninformative_search import LDFS


def main():
    grid = Grid.generate_solvable(400)
    print('Generated grid:\n')
    print(grid, '\n')
    print('Solving...')
    ldfs = LDFS(grid, 22)
    solution = ldfs.solve()
    if solution is not None:
        print(f'\nSolving time: {round(ldfs.execution_time, 3)}s')
        print(f'Solution depth: {len(solution)}')
        print(f'Iterations:', ldfs.iterations)
        print(f'Dead ends:', ldfs.dead_ends)
        print(f'Visited states:', len(ldfs.unique_visited_states), '\n')
        print('Solution:\n')
        for direction in solution:
            grid.move(direction)
            print(f'Move: {direction.name.lower()}')
            print(grid, '\n')


if __name__ == '__main__':
    main()
