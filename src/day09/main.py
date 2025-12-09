import itertools as it

def sort_tuples(point_pairs):
    return [(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)) for (x1, y1), (x2, y2) in point_pairs]

with open("input.txt") as f:

    red = list(map(eval, open('input.txt')))
    green_sides = sort_tuples(it.pairwise(red))
    red_rects = sort_tuples(it.combinations(red, 2))

    part_1 = part_2 = 0

    for r_x1, r_y1, r_x2, r_y2 in red_rects:
        size = (r_x2 - r_x1 + 1) * (r_y2 - r_y1 + 1)

        if size > part_2:
            # I don't know how to figure out if the red rectangle is "contained" in the union of green rectangles
            # BUT we can check the opposite: if the red rectangle "cuts" any green side, it's not contained
            # (since the green sides always "touch" the outside world)
            for g_x1, g_y1, g_x2, g_y2 in green_sides:
                # It's always either g_x1 == g_x2 or g_y1 == g_y2
                if r_x1 < g_x2 and g_x1 < r_x2 and r_y1 < g_y2 and g_y1 < r_y2:
                    break
            else:
                # The red rectangle does NOT cut any green side
                part_2 = max(part_2, size)

        part_1 = max(part_1, size)

    print("Part 1:", part_1)
    print("Part 2:", part_2)
