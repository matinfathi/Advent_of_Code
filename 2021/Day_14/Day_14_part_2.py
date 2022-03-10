file_path = './input_day14'

with open(file_path, 'r') as f:
    data = f.read().split('\n\n')

template = data[0].strip()
pairs = [item.split(' -> ') for item in data[1].split('\n') if item.split(' -> ')[0]]
pairs_counter = {item.split(' -> ')[0]: 0 for item in data[1].split('\n') if item.split(' -> ')[0]}

for i in range(len(template)-1):
    couple = template[i:i+2]
    pairs_counter[couple] += 1

pairs_counter2 = pairs_counter.copy()

chars = list(set([pair[1] for pair in pairs]))
char_counter = {char: template.count(char) for char in chars}

for i in range(1, 41):
    for pair in pairs:
        couple = pair[0]
        middle = pair[1]
        if couple == 'OO':
            print()
        if pairs_counter2[couple]:
            val = pairs_counter2[couple]
            pairs_counter[couple] -= pairs_counter2[couple]
            pairs_counter[couple[0]+middle] += val
            pairs_counter[middle + couple[1]] += val
            char_counter[middle] += val

    pairs_counter2 = pairs_counter.copy()

sort_list = char_counter.values()
print(max(sort_list) - min(sort_list))
