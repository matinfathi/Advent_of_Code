from collections import defaultdict
from heapq import heappop, heappush
import numpy as np
import math


def find_neighbors(point, arr):
    found_neighbors = []
    x, y = point[0], point[1]
    shape_x, shape_y = arr.shape[0], arr.shape[1]
    if x < shape_x - 1:
        found_neighbors.append((x + 1, y))
    if x > 0:
        found_neighbors.append((x - 1, y))
    if y < shape_y - 1:
        found_neighbors.append((x, y + 1))
    if y > 0:
        found_neighbors.append((x, y - 1))

    return found_neighbors


def reconstruct_path(came_from, c):
    f_p = [c]
    while c in came_from:
        c = came_from[c]
        f_p.append(c)
    return f_p


def dijkstra(arr, s, e):
    cost_dict = defaultdict(lambda: math.inf)
    cost_dict[s] = 0
    visit_queue = []
    heappush(visit_queue, (0, (0, 0)))

    unvisited_cells = set()
    for y, row in enumerate(arr):
        for x, cell in enumerate(row):
            unvisited_cells.add((x, y))

    while e in unvisited_cells:

        min_val, min_node = heappop(visit_queue)

        if min_node not in unvisited_cells:
            continue

        neighbors = find_neighbors(min_node, arr)
        for n in neighbors:
            if n not in unvisited_cells:
                continue

            neighbour_risk = int(min(
                cost_dict[n],
                cost_dict[min_node] + arr[n[1]][n[0]]
            ))

            cost_dict[n] = neighbour_risk
            heappush(visit_queue, (neighbour_risk, n))

        unvisited_cells.remove(min_node)

    return cost_dict[e]


file_path = './input_day15'

with open(file_path, 'r') as f:
    data = np.array([list(line.strip()) for line in f.readlines()]).astype(int)

new_data = data.copy()

for i in range(1, 5):
    new_data += 1
    tens = np.where(new_data == 10)
    new_data[tens] = 1
    data = np.concatenate((data, new_data), axis=0)

new_data = data.copy()

for j in range(4):
    new_data += 1
    tens = np.where(new_data == 10)
    new_data[tens] = 1
    data = np.concatenate((data, new_data), axis=1)

start = (0, 0)
end = (len(data)-1, len(data)-1)

shortest_path_cost = dijkstra(data, start, end)

print(shortest_path_cost)
