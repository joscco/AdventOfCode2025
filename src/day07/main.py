with open("input.txt") as f:
    grid = f.read().splitlines()
    paths = {grid[0].index('S'): 1}
    splits = 0

    for row in grid[1:]:
        next_paths = {}
        for pos_x, leading_paths in paths.items():
            if row[pos_x] == '^':
                splits += 1
                next_paths[pos_x - 1] = next_paths.get(pos_x - 1, 0) + leading_paths
                next_paths[pos_x + 1] = next_paths.get(pos_x + 1, 0) + leading_paths
            else:
                next_paths[pos_x] = next_paths.get(pos_x, 0) + leading_paths
        paths = next_paths

    print("Part 1:", splits)
    print("Part 2:", sum(paths.values()))
