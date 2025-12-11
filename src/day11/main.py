import itertools as it


def count_paths(graph, start, goal, memo=None):
    if memo is None:
        memo = {}

    key = (start, goal)
    if key in memo:
        return memo[key]

    if start == goal:
        return 1

    if start not in graph:
        return 0

    total = 0
    for neighbor in graph[start]:
        total += count_paths(graph, neighbor, goal, memo)

    memo[key] = total
    return total


def count_paths_via(graph, start, goal, via):
    memo = {}

    def count(u, v):
        return count_paths(graph, u, v, memo)

    total = 0
    for perm in it.permutations(via):
        sub_total = count(start, perm[0])
        for i in range(len(perm) - 1):
            sub_total *= count(perm[i], perm[i + 1])
        sub_total *= count(perm[-1], goal)
        total += sub_total

    return total


with open("input.txt") as f:
    lines = [line.split() for line in f.read().splitlines()]
    connections = {line[0].rstrip(":"): line[1:] for line in lines}

    print("Part 1:", count_paths(connections, 'you', 'out'))
    print("Part 2:", count_paths_via(connections, 'svr', 'out', ['dac', 'fft']))
