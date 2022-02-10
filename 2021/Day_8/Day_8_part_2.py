from difflib import SequenceMatcher

input_path = './input_day8'

with open(input_path, 'r') as f:
    data = f.read().strip()

unique_numbers = [entry.split('|')[0].split() for entry in data.split('\n')]

output_digits = [entry.split('|')[-1].split() for entry in data.split('\n')]


def fill_positions(ref, pos, letter):
    if pos == 0:
        ref[0, 1:5] = letter
    elif pos == 1:
        ref[1:3, 0] = letter
    elif pos == 2:
        ref[1:3, -1] = letter
    elif pos == 3:
        ref[3, 1:5] = letter
    elif pos == 4:
        ref[4:6, 0] = letter
    elif pos == 5:
        ref[4:6, -1] = letter
    elif pos == 6:
        ref[-1, 1:5] = letter

    return ref


def by_size(words, size):
    return [word for word in words if len(word) == size]


def find_letter(sev, onn):
    for i in sev:
        if i not in onn:
            return i


def find_six(sixes, onn):
    for six in sixes:
        for i in onn:
            if i not in six:
                return six


def find_three(fives, onn):
    for five in fives:
        switch = True
        for i in onn:
            if i not in five:
                switch = False

        if switch:
            return five


def find_nine(sixes, fourr):
    for nine in sixes:
        switch = True
        for i in fourr:
            if i not in nine:
                switch = False

        if switch:
            return nine


def find_five(fives, fourr):
    for five in fives:
        counter = 0
        for i in fourr:
            if i not in five:
                counter += 1

        if counter == 1:
            return five


def similar(a, b):
    if len(a) == len(b):
        for i in a:
            if i not in b:
                return False
        return True
    else:
        return False


summation = 0

for idx, (un, od) in enumerate(zip(unique_numbers, output_digits)):
    digits = {}
    four_digit = ''
    five_letters = by_size(un, 5)
    six_letters = by_size(un, 6)
    digits['7'] = by_size(un, 3)[0]
    digits['1'] = by_size(un, 2)[0]
    digits['4'] = by_size(un, 4)[0]
    digits['8'] = by_size(un, 7)[0]
    digits['6'] = find_six(six_letters, digits['1'])
    digits['9'] = find_nine(six_letters, digits['4'])
    six_letters.remove(digits['6'])
    six_letters.remove(digits['9'])
    digits['0'] = six_letters[0]
    digits['3'] = find_three(five_letters, digits['1'])
    five_letters.remove(digits['3'])
    digits['5'] = find_five(five_letters, digits['4'])
    five_letters.remove(digits['5'])
    digits['2'] = five_letters[0]

    reverse_digits = {v: int(k) for k, v in digits.items()}
    for d in od:
        for key in reverse_digits.keys():
            if similar(d, key) == 1:
                four_digit += str(reverse_digits[key])
                break
    summation += int(four_digit)

print(summation)
