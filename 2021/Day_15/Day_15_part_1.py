import numpy as np
import math


def array2graph(arr):
    g = {}
    for idx, line in enumerate(arr):
        for idy, item in enumerate(line):
            g[(idx, idy)] = []
            if idx < len(line) - 1:
                g[(idx, idy)] += [(idx + 1, idy)]
            if idx > 0:
                g[(idx, idy)] += [(idx - 1, idy)]
            if idy < arr.shape[1] - 1:
                g[(idx, idy)] += [(idx, idy + 1)]
            if idy > 0:
                g[(idx, idy)] += [(idx, idy - 1)]

    return g


def reconstruct_path(came_from, c):
    f_p = [c]
    while c in came_from:
        c = came_from[c]
        f_p.append(c)
    return f_p


def dijkstra(g, arr, start, end):
    cost_from_a = {}
    came_from = {}
    visited = []
    unvisited = [start]

    for key in g.keys():
        cost_from_a[key] = math.inf

    cost_from_a[start] = 0

    min_node = start

    while unvisited:

        min_val = math.inf

        for current in unvisited:
            if cost_from_a[current] < min_val:
                min_val = cost_from_a[current]
                min_node = current

        if min_node == end:
            return reconstruct_path(came_from, min_node), cost_from_a[current]

        visited.append(min_node)
        unvisited.remove(min_node)

        neighbors = g[min_node]
        for n in neighbors:
            if n in visited:  # ignore neighbor node if its already evaluated
                continue
            if n not in unvisited:
                unvisited.append(n)

            tentative_gscore = cost_from_a[min_node] + arr[n]

            # not a better path to reach neighbor
            if tentative_gscore >= cost_from_a[n]:
                continue
            came_from[n] = min_node  # record the best path until now
            cost_from_a[n] = tentative_gscore

    return False


file_path = './input_day15'

with open(file_path, 'r') as f:
    data = np.array([list(line.strip()) for line in f.readlines()]).astype(int)

graph = array2graph(data)
shortest_path, shortest_path_cost = dijkstra(graph, data, (0, 0), (99, 99))

shortest_path.reverse()

print(shortest_path)
print()
print(shortest_path_cost)
