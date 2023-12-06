import os, datetime

DIGITS_DICT = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e",
}


def read_input(debug: bool) -> str:
    filename = "debug.txt" if debug else "input.txt"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f"{current_dir}/{filename}", "r") as f:
        return f.readlines()


def normalize_digits(line: str) -> str:
    for key in DIGITS_DICT:
        line = line.replace(key, DIGITS_DICT[key])
    return line


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
    for line in inputs:
        normalized_line = normalize_digits(line)
        extracted_digits = "{first}{last}".format(
            first=get_first_digit(normalized_line),
            last=get_last_digit(normalized_line),
        )
        numbers.append(int(extracted_digits))
    print(sum(numbers))


if __name__ == "__main__":
    start = datetime.datetime.now()
    # main(debug=True)
    main()
    end = datetime.datetime.now()
    print("Process time: ", end - start)

## 1ST TRY: 54145 INCORRECT (too low)
## 2ND TRY: 54571 INCORRECT (too low)
## 3RD TRY: 55208 INCORRECT
## 4TH TRY: 54783 INCORRECT
## 5TH TRY: 55054 INCORRECT
## 6TH TRY: 54585 INCORRECT

## 7TH TRY: 54578 CORRECT
