path = './input_day10'

with open(path, 'r') as f:
    data = [line.strip() for line in f.readlines()]

char_dict = {
    '[': ']',
    '(': ')',
    '{': '}',
    '<': '>',
}

char_penalty = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}

penalty_list = []

for line in data:
    penalty = 0
    switch = 1
    open_char = ''
    open_chars = []
    for char in line:
        if char in char_dict.keys():
            open_char = char
            open_chars.append(char)
        elif char == char_dict.get(open_char, ''):
            open_chars = open_chars[:-1]
            open_char = open_chars[-1] if open_chars else ''
        else:
            switch = 0
            break

    if open_chars and switch:
        for open_character in list(reversed(open_chars)):
            penalty = penalty * 5
            penalty += char_penalty[char_dict[open_character]]

        penalty_list.append(penalty)

penalty_list = sorted(penalty_list)

middle_idx = int((len(penalty_list)-1)/2)

print(penalty_list[middle_idx])
