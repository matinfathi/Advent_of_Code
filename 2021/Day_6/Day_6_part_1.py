import numpy as np

input_path = './input_day6'

with open(input_path, 'r') as f:
    data = f.read().strip().split(',')

data = np.array(list(map(int, data)))

coordinates = np.array([[]])

for i in range(81):

    num_zeros = coordinates[0].shape[0]
    if num_zeros:
        data[coordinates] = 6
        data = np.append(data, np.array([8] * num_zeros))
    coordinates = np.where(data == 0)
    data -= 1

print(data.shape[0])
