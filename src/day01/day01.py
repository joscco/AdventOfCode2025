from math import ceil, floor

def mult_of_100(a, b):
    if a > b:
        a, b = b, a
    return len(set(range(ceil(a / 100), floor(b / 100) + 1)))


with open("input.txt") as f:
    direction_mapping = {"L": -1, "R": 1}
    val, part_1_counter, part_2_counter = 50, 0, 0
    for line in f.readlines():
        direction, dist = line[0], line[1:]
        offset = direction_mapping[direction] * int(dist)
        next_val = val + offset
        if next_val % 100 == 0:
            part_1_counter += 1
        part_2_counter += mult_of_100(val, next_val)

        # We want to count the new value only once
        if val % 100 == 0:
            part_2_counter -= 1
        val = next_val

    print(part_1_counter)
    print(part_2_counter)
