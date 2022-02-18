import numpy as np

path = './input_day9'

with open(path, 'r') as f:
    data = f.read().strip().split()

array = []
for line in data:
    array.append(list(map(int, list(line))))

array = np.array(array)

array = np.pad(array, (1, 1), constant_values=9)


def find_connected_points(area, x, y):
    connected_points = []
    length_x = area.shape[0]
    length_y = area.shape[1]

    if 0 <= x - 1 <= length_x - 1:
        connected_points.append(area[x - 1, y])
    if 0 <= x + 1 <= length_x - 1:
        connected_points.append(area[x + 1, y])
    if 0 <= y - 1 <= length_y - 1:
        connected_points.append(area[x, y - 1])
    if 0 <= y + 1 <= length_y - 1:
        connected_points.append(area[x, y + 1])

    return connected_points


def check_low_point(area, x, y):
    connected_points = find_connected_points(area, x, y)
    if min(connected_points) > area[x, y]:
        return True
    else:
        return False


def move_point(p_m):
    [p1, p2] = p_m.pop(0)
    return p1, p2, p_m


def point_in_basin(area, p1, p2, basin_points):
    if area[p1, p2] == 1 and [p1, p2] not in basin_points:
        return True
    else:
        return False


def extract_possible_moves(area, p1, p2, p_m, u_m):
    for ii in range(4):
        pp1 = p1
        pp2 = p2
        if ii == 0:
            pp1 += 1
        elif ii == 1:
            pp1 -= 1
        elif ii == 2:
            pp2 += 1
        elif ii == 3:
            pp2 -= 1
        if area[pp1, pp2] == 1 and [pp1, pp2] not in u_m and [pp1, pp2] not in p_m:
            p_m.append([pp1, pp2])

    return p_m


def find_basin_points(area, x, y):
    switch = True
    possible_moves = []
    used_moves = []
    point1, point2 = x, y
    possible_moves = extract_possible_moves(area, point1, point2, possible_moves, used_moves)
    used_moves.append([point1, point2])
    while switch:
        point1, point2, possible_moves = move_point(possible_moves)
        used_moves.append([point1, point2])
        possible_moves = extract_possible_moves(area, point1, point2, possible_moves, used_moves)
        if not possible_moves:
            switch = False
            continue

    return used_moves


def count_basin(area, x, y):
    basin_points = find_basin_points(area, x, y)
    return len(basin_points)


low_points = []

for i, row in enumerate(array):
    for j, val in enumerate(row):
        if check_low_point(array, i, j):
            low_points.append((i, j))

nines = np.where(array == 9)
not_nines = np.where(array != 9)
array[nines] = 0
array[not_nines] = 1

size_basins = []

for idx, point in enumerate(low_points):
    [x, y] = point
    basin = count_basin(array, x, y)
    size_basins.append(basin)

if len(size_basins) > 3:
    a1, a2, a3 = sorted(size_basins, reverse=True)[:3]
answer = a1 * a2 * a3

print(answer)

