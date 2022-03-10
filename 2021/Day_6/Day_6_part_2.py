from collections import Counter

input_path = './input_day6'

with open(input_path, 'r') as f:
    data = list(map(int, f.read().strip().split(',')))

lifes = dict(Counter(data))

for i in range(1, 257):
    lifes = {l: (0 if lifes.get(l + 1) is None else lifes.get(l + 1)) for l in range(-1, 8)}
    lifes[8] = lifes[-1]
    lifes[6] += lifes[-1]
    lifes[-1] = 0

print(sum(lifes.values()))
