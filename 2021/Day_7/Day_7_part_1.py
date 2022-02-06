input_path = './input_day7'

with open(input_path, 'r') as f:
    data = list(map(int, f.read().strip().split(',')))

final_cost = 10 ** 7

for i in range(max(data)):
    cost = 0
    for idx2, j in enumerate(data):
        cost += abs(i - j)

    if cost < final_cost:
        final_cost = cost

print(final_cost)
