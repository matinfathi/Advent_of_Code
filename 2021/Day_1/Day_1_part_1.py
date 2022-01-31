input_path = "./input_day1"

with open (input_path, 'r') as f:
    data = f.read().split('\n')

counter, perv_item = 0, 0

for idx, item in enumerate(data):
    if item and idx:
        if int(item) > int(perv_item):
            counter += 1
    perv_item = item

print(counter)
