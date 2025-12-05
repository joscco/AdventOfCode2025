with open("input.txt") as f:
    lines = f.readlines()

    split_index = lines.index("\n")
    intervalls = []
    for line in lines[:split_index]:
        bounds = line.split("-")
        intervalls.append((int(bounds[0]), int(bounds[1])))
    ids = [int(line) for line in lines[split_index + 1:]]

    valid_ids = 0
    for id_ in ids:
        is_valid = False
        for intervall in intervalls:
            if intervall[0] <= id_ <= intervall[1]:
                is_valid = True
                break
        if is_valid:
            valid_ids += 1

    print("Part 1:", valid_ids)

    disjoint_intervalls = []
    for intervall in sorted(intervalls):
        if not disjoint_intervalls or disjoint_intervalls[-1][1] < intervall[0]:
            disjoint_intervalls.append(intervall)
        else:
            disjoint_intervalls[-1] = (disjoint_intervalls[-1][0], max(disjoint_intervalls[-1][1], intervall[1]))

    number_of_valid_ids = 0
    for intervall in disjoint_intervalls:
        number_of_valid_ids += intervall[1] - intervall[0] + 1
    print("Part 2:", number_of_valid_ids)