import time

ROLL = "@"
EMPTY = "."

NEIGHBOR_OFFSETS = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1),
]

def find_free_rolls(field):
    h = len(field)
    w = len(field[0])

    result = []
    for y in range(h):
        row = field[y]
        for x in range(w):
            if row[x] != ROLL:
                continue

            neighboring_rolls = 0
            for dy, dx in NEIGHBOR_OFFSETS:
                ny = y + dy
                nx = x + dx
                if 0 <= ny < h and 0 <= nx < w and field[ny][nx] == ROLL:
                    neighboring_rolls += 1
                    if neighboring_rolls >= 4:
                        break
            if neighboring_rolls < 4:
                result.append((x, y))

    return result


def remove_all_free_rolls(roll_field):
    number_removed_rolls = 0
    while True:
        free_rolls = find_free_rolls(roll_field)
        if not free_rolls:
            break
        for x, y in free_rolls:
            roll_field[y][x] = EMPTY
            number_removed_rolls += 1
    return number_removed_rolls


with open("input.txt") as f:
    field = [list(line.strip()) for line in f]

    start_part1 = time.perf_counter()
    all_free_rolls = find_free_rolls(field)
    end_part1 = time.perf_counter()
    print("Part 1:", len(all_free_rolls))
    print(f"Zeit Part 1: {end_part1 - start_part1:.6f} Sekunden")

    start_part2 = time.perf_counter()
    removed_rolls = remove_all_free_rolls(field)
    end_part2 = time.perf_counter()
    print("Part 2:", removed_rolls)
    print(f"Zeit Part 2: {end_part2 - start_part2:.6f} Sekunden")
