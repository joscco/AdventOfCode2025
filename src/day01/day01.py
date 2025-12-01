from math import ceil, floor

def count_mults_of_100(a, b):
    low, high = sorted((a, b))
    return len(set(range(ceil(low / 100), floor(high / 100) + 1)))


with open("input.txt") as f:
    direction_mapping = {"L": -1, "R": 1}
    prev_val, part_1_counter, part_2_counter = 50, 0, 0
    for line in f.readlines():
        direction, dist = line[0], line[1:]
        offset = direction_mapping[direction] * int(dist)
        new_val = prev_val + offset

        # Part 1
        if new_val % 100 == 0:
            part_1_counter += 1

        # Part 2
        part_2_counter += count_mults_of_100(prev_val, new_val)
        # We want to count the new value only once
        if prev_val % 100 == 0:
            part_2_counter -= 1
        prev_val = new_val

    print(part_1_counter)
    print(part_2_counter)
