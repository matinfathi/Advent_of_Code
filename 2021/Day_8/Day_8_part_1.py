input_path = './input_day8'

with open(input_path, 'r') as f:
    data = f.read().strip()

data = [entry.split('|')[-1].split() for entry in data.split('\n')]


def return_len(digits):
    return [len(digit) for digit in digits]


counter = 0

for outputs in data:
    len_list = return_len(outputs)
    one_counter = len_list.count(2)
    four_counter = len_list.count(4)
    seven_counter = len_list.count(3)
    eight_counter = len_list.count(7)
    summation = one_counter + four_counter + seven_counter + eight_counter
    counter += summation

print(counter)
