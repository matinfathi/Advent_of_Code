input_path = './input_day3'

with open(input_path, 'r') as f:
    data = f.read().split('\n')[:-1]

gama, epsilon = '', ''

for idx in range(12):
    count1 = 0
    count0 = 0

    for item in data:
        if item[idx] == '0':
            count0 += 1
        else:
            count1 += 1

    if count0 > count1:
        gama += '0'
        epsilon += '1'
    else:
        gama += '1'
        epsilon += '0'

print(int(gama, 2) * int(epsilon, 2))
