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
        number = item[1:].strip()
        if item.startswith("R"):
            total += int(number)
        else:
            total -= int(number)

        if not total % 100:
            num_zeros += 1


    print(total)
    print(num_zeros)


if __name__ == "__main__":
    main()
