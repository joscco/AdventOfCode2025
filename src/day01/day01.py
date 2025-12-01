with open("input.txt") as f:
    direction_mapping = {"L": -1, "R": 1}
    val, part_1_counter, part_2_counter = 50, 0, 0
    for line in f.readlines():
        direction, dist = line[0], line[1:]
        offset = direction_mapping[direction] * int(dist)
        next_val = val + offset
        if next_val <= 0:
            part_2_counter += abs(next_val // 100)
            if next_val % 100 == 0:
                part_2_counter += 1
            if val == 0:
                part_2_counter -= 1
        elif next_val >= 100:
            part_2_counter += next_val // 100
        val = next_val % 100
        if val == 0:
            part_1_counter += 1

    print(part_1_counter)
    print(part_2_counter)
