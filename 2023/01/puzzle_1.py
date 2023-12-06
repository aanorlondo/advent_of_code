import os, datetime


def read_input(debug: bool) -> str:
    filename = "debug.txt" if debug else "input.txt"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f"{current_dir}/{filename}", "r") as f:
        return f.readlines()


def get_first_digit(line: str) -> str:
    for index in line:
        if index.isdigit():
            return index


def get_last_digit(line: str) -> str:
    reversed_line = line[::-1]
    return get_first_digit(reversed_line)


def main(debug=False) -> None:
    inputs = read_input(debug)
    numbers = []
    for input in inputs:
        extracted_digits = "{first}{last}".format(
            first=get_first_digit(input),
            last=get_last_digit(input),
        )
        numbers.append(int(extracted_digits))
    print(sum(numbers))


if __name__ == "__main__":
    start = datetime.datetime.now()
    # main(debug=True)
    main()
    end = datetime.datetime.now()
    print("Process time: ", end - start)

## 1ST TRY: 55208 CORRECT
