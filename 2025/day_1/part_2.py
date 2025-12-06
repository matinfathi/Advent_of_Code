FILE_ADDRESS = "2025/day_1/input_day_1.txt"


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
        number = abs(int(item[1:].strip()))
        to_99 = 100 - total

        num_zeros += number // 100
        extra = number % 100

        if item.startswith("R"):
            if extra <= to_99:
                total += extra
            else:
                num_zeros += 1
                total = extra - to_99

        else:
            if extra < total:
                total -= extra
            else:
                num_zeros += 1
                total = 100 - (extra - total)

            


    print(total)
    print(num_zeros)


if __name__ == "__main__":
    main()
