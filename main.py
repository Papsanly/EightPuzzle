from Grid import Grid, Direction, ImpossibleMove


def main():
    grid = Grid.generate_random()
    print(grid)
    while True:
        direction = input('Enter direction\nu - up, d - down, l - left ,r - right\n').lower()
        try:
            match direction:
                case 'u':
                    grid.move(Direction.UP)
                case 'd':
                    grid.move(Direction.DOWN)
                case 'l':
                    grid.move(Direction.LEFT)
                case 'r':
                    grid.move(Direction.RIGHT)
        except ImpossibleMove:
            print('Cannot move in this direction')
        else:
            print(grid)


if __name__ == '__main__':
    main()
