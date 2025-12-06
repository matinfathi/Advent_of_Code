FILE_ADDRESS = "2025/day_1/test.txt"


def open_file(file_address: str) -> list[str]:
    with open(file_address, mode="r") as f:
        lines = f.read().strip().split("\n")
    
    return lines


def get_hundred_digit(number: int) -> int:
    number_str = str(abs(number))
    if len(number_str) >= 3:
        hundreds_digit = int(number_str[-3])
        return hundreds_digit
    else:
        return 0


def main():
    total = 50
    num_zeros = 0

    lines = open_file(file_address=FILE_ADDRESS)
    for item in lines:
        number = int(item[1:].strip())

        old_total = total

        if item.startswith("R"):
            total += number
        else:
            total -= number

        change_in_hundreds = abs(get_hundred_digit(total) - get_hundred_digit(old_total))

        if total == 0:
            # print(item)
            num_zeros += 1

        if change_in_hundreds:
            num_zeros += change_in_hundreds
        else:
            if total * old_total < 0:
                num_zeros += change_in_hundreds

        print(total)


    print(total)
    print(num_zeros)


if __name__ == "__main__":
    main()
