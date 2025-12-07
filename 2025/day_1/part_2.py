FILE_ADDRESS = "2025/day_1/input_day_1.txt"


def open_file(file_address: str) -> list[str]:
    with open(file_address, mode="r") as f:
        lines = f.read().strip().split("\n")
    
    return lines


def main():
    total = 50
    num_zeros = 0

    lines = open_file(file_address=FILE_ADDRESS)

    for item in lines:
        number = int(item[1:].strip())
        to_100 = 100 - total

        num_zeros += number // 100
        extra = number % 100

        if item.startswith("R"):
            if extra < to_100:
                total += extra
            else:
                num_zeros += 1
                total = extra - to_100

        else:
            if total == 0:
                total = 100 - extra
            elif extra < total:
                total -= extra
            elif extra == total:
                num_zeros += 1
                total = 0
            else:
                num_zeros += 1
                total = 100 - (extra - total)

    return num_zeros


if __name__ == "__main__":
    main()
