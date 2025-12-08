from functools import reduce
from math import dist

def build_distances(points):
    n = len(points)
    dist_list = [(i, j, dist(points[i], points[j])) for i in range(n) for j in range(i + 1, n)]
    dist_list.sort(key=lambda x: x[2])
    return dist_list


def build_clusters(distances):
    clusters = []
    index_to_cluster = {}
    last_pair = None

    for x, y, d in distances:
        cx = index_to_cluster.get(x)
        cy = index_to_cluster.get(y)

        if cx is None and cy is None:
            new_cluster = {x, y}
            clusters.append(new_cluster)
            index_to_cluster[x] = new_cluster
            index_to_cluster[y] = new_cluster
        elif cy is None:
            cx.add(y)
            index_to_cluster[y] = cx
        elif cx is None:
            cy.add(x)
            index_to_cluster[x] = cy
        else:
            if cx is cy:
                # Already in the same cluster, nothing to do
                # Continuing also prevents setting last_pair
                continue
            # clusters should be merged
            if len(cx) < len(cy):
                cx, cy = cy, cx
            cx.update(cy)
            for idx in cy:
                index_to_cluster[idx] = cx
            if cy in clusters:
                clusters.remove(cy)

        last_pair = (x, y)

    return clusters, last_pair


with open("input.txt") as f:
    points = [list(map(int, line.split(","))) for line in f.read().splitlines()]

    distances = build_distances(points)
    # For the test file, limit would be first 10 instead of first 1000
    clusters, _ = build_clusters(distances[:1000])

    cluster_sizes = sorted((len(c) for c in clusters), reverse=True)
    largest_three = cluster_sizes[:3]
    result = reduce(lambda a, b: a * b, largest_three, 1)
    print("Part 1:", result)

    _, last_pair = build_clusters(distances)
    x_1, x_2 = [points[i][0] for i in last_pair]
    print("Part 2:", x_1 * x_2)

