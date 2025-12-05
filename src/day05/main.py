def fresh_ids_within(intervals, ids):
    return [
        any(start <= id_ <= end for start, end in intervals)
        for id_ in ids
    ]


def total_number_of_possible_fresh_ids(raw_intervals):
    disjoint_intervals = []
    for interval in sorted(raw_intervals):
        # Because of the natural sorting and the intervals
        # in disjoint_intervals are already disjoint,
        # we only have to check for overlaps with the last interval
        if not disjoint_intervals or disjoint_intervals[-1][1] < interval[0]:
            disjoint_intervals.append(interval)
        else:
            start, end = disjoint_intervals[-1]
            disjoint_intervals[-1] = (start, max(end, interval[1]))

    return sum(
        end - start + 1 for start, end in disjoint_intervals
    )


with open("input.txt") as f:
    lines = f.readlines()

    split_index = lines.index("\n")
    intervals = [tuple(map(int, line.split("-"))) for line in lines[:split_index]]
    ids = [int(line) for line in lines[split_index + 1:]]

    fresh_ids = fresh_ids_within(intervals, ids)
    print("Part 1:", sum(fresh_ids))

    possible_fresh_ids = total_number_of_possible_fresh_ids(intervals)
    print("Part 2:", possible_fresh_ids)