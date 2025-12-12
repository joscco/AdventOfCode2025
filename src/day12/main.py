def present_area(lines):
    return sum(line.count('#') for line in lines)


def region(line):
    size, need_line = line.split(': ')
    size = [int(i) for i in size.split('x')]
    needs = [int(i) for i in need_line.split(' ') if i != '']
    return size, needs


def fits(size, needs, areas):
    return size[0] * size[1] >= sum(needs[i] * areas[i] for i in range(6))


with open("input.txt") as f:
    data = [line.strip() for line in f.readlines()]
    areas = [present_area(data[5 * i:5 * (i + 1)]) for i in range(6)]
    regions = [region(line) for line in data[30:]]
    print(areas, regions)
    print("Part 1:", sum(1 if fits(*region, areas) else 0 for region in regions))
