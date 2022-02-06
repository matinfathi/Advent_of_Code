input_path = './input_day7'

with open(input_path, 'r') as f:
    data = list(map(int, f.read().strip().split(',')))

final_cost = 10 ** 20

for i in range(max(data)):
    cost = 0
    for idx2, j in enumerate(data):

        n = abs(i - j)
        cost += (n ** 2 + n) / 2

    if cost < final_cost:
        final_cost = cost

print(final_cost)
