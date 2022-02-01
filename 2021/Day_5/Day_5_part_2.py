import numpy as np

path = './input_day5'

with open(path, 'r') as f:
    data = f.read().replace(' ', '').split()

data = [list(map(int, item.replace('->', ',').split(','))) for item in data]
data = np.array(data)
vents = np.zeros((1000, 1000))

for x1, y1, x2, y2 in data:
    if x1 == x2:
        vents[x1, min(y1, y2):max(y1, y2)+1] += 1
    elif y1 == y2:
        vents[min(x1, x2):max(x1, x2)+1, y1] += 1
    else:
        distance = max(x1, x2) - min(x1, x2)
        argmax = np.argmax([x1, x2])
        argmin = np.argmin([x1, x2])
        direction = 'pos' if [y1, y2][argmin] - [y1, y2][argmax] > 0 else 'neg'
        for i in range(distance+1):
            if direction == 'pos':
                vents[min(x1, x2) + i, [y1, y2][argmin] - i] += 1
            else:
                vents[min(x1, x2) + i, [y1, y2][argmin] + i] += 1

answer = len(np.where(vents >= 2)[0])

print(answer)
