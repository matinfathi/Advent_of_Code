import numpy as np

path = './input_day13'

with open(path, 'r') as f:
    folds = [item.strip().split()[-1] for item in f.readlines() if item.startswith('fold')]
with open(path, 'r') as f:
    data = np.array([item.split(',') for item in f.read().split('\n\n')[0].split()]).T.astype(int)

grid = np.zeros((np.max(np.unique(data[0]))+1, np.max(np.unique(data[1]))+1)).astype(int)
data = tuple([np.array(item) for item in data])
grid[data] = 1
grid = grid.T

for fold in folds:
    split_number = int(fold.split('=')[-1])
    if fold.startswith('y'):
        matrix_a = grid[:split_number, :]
        matrix_b = grid[split_number+1:, :]
        matrix_b = np.flip(matrix_b, axis=0)
    else:
        matrix_a = grid[:, :split_number]
        matrix_b = grid[:, split_number+1:]
        matrix_b = np.flip(matrix_b, axis=1)

    points = np.where(matrix_b == 1)
    matrix_a[points] = 1
    grid = matrix_a

print(grid)
