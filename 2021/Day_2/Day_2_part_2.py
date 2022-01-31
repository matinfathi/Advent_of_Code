input_path = './input_day2'

with open(input_path, 'r') as f:
    data = f.read().split('\n')[:-1]

depth, h_pos, aim = 0, 0, 0

for item in data:
    if item.split()[0] == 'forward':
        h_pos += int(item.split()[1])
        depth += aim * int(item.split()[1])
    elif item.split()[0] == 'up':
        aim -= int(item.split()[1])
    elif item.split()[0] == 'down':
        aim += int(item.split()[1])

print(depth * h_pos)
