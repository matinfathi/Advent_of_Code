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
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

penalty = 0
errors = []

for line in data:
    open_char = ''
    open_chars = ['']
    for char in line:
        if char in char_dict.keys():
            open_char = char
            open_chars.append(char)
        elif char == char_dict.get(open_char, ''):
            open_chars = open_chars[:-1]

            open_char = open_chars[-1]
        else:
            penalty += char_penalty[char]
            errors.append(char)
            break

print(penalty)
