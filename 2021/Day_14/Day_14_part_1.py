file_path = './input_day14'

with open(file_path, 'r') as f:
    data = f.read().split('\n\n')

template = data[0].strip()
pairs = [item.split(' -> ') for item in data[1].split('\n') if item.split(' -> ')[0]]
template2 = template

for i in range(1, 2):
    for pair in pairs:
        switch = True
        if pair[0] in template and pair[0] in template2:
            while switch:
                idx = template2.find(pair[0])
                if idx == -1:
                    switch = False
                    continue
                template2 = template2[:idx+1] + pair[1].lower() + template2[idx+1:]

    template2 = template2.upper()
    template = template2

counter = []
for char in template:
    counter.append(template.count(char))

counter = sorted(counter)
print(counter[-1] - counter[0])
