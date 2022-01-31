input_path = "./input_day1"

with open(input_path, 'r') as f:
    data = f.read().split('\n')[:-1]

counter, perv_sum = 0, 0

for idx, item in enumerate(data):
    if idx < len(data) - 2:
        sum = int(item) + int(data[idx + 1]) + int(data[idx + 2])
        if idx:
            if sum > perv_sum:
                counter += 1
            perv_sum = sum

print(counter)
