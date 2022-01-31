import numpy as np

input_path = './input_day3'

with open(input_path, 'r') as f:
    data = f.read().split('\n')[:-1]

data = [list(item) for item in data]
data = np.array(data, dtype='int64')

data_o2 = data.copy()
data_co2 = data.copy()

for idx in range(12):
    count = np.bincount(data_o2[:, idx])
    if count[0] != count[1]:
        max_count = count.argmax()
    else:
        max_count = 1

    data_o2 = data_o2[data_o2[:, idx] == max_count]

for idx in range(12):
    count = np.bincount(data_co2[:, idx])

    if count[0] != count[1]:
        min_count = count.argmin()
    else:
        min_count = 0

    data_co2 = data_co2[data_co2[:, idx] == min_count]
    if data_co2.shape[0] == 1:
        break

co2 = "".join(map(str, data_co2[0].tolist()))
o2 = "".join(map(str, data_o2[0].tolist()))

print(int(o2, 2) * int(co2, 2))
