import numpy as np

path = './input_day9'

with open(path, 'r') as f:
    data = f.read().strip().split()

array = []
for line in data:
    array.append(list(map(int, list(line))))

array = np.array(array)


def find_connected_points(area, x, y):
    connected_points = []
    length_x = area.shape[0]
    length_y = area.shape[1]

    if 0 <= x - 1 <= length_x-1:
        connected_points.append(area[x-1, y])
    if 0 <= x + 1 <= length_x-1:
        connected_points.append(area[x+1, y])
    if 0 <= y - 1 <= length_y-1:
        connected_points.append(area[x, y-1])
    if 0 <= y + 1 <= length_y-1:
        connected_points.append(area[x, y+1])

    return connected_points


def check_low_point(area, x, y):
    connected_points = find_connected_points(area, x, y)
    if min(connected_points) > area[x, y]:
        return True
    else:
        return False


summation = 0

for i, row in enumerate(array):
    for j, val in enumerate(row):
        if check_low_point(array, i, j):
            summation += array[i, j] + 1

print(summation)
