import os, datetime


def read_input(debug: bool) -> str:
    filename = "debug.txt" if debug else "input.txt"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f"{current_dir}/{filename}", "r") as f:
        return f.readlines()


def get_symbol_positions(lines: list[str]) -> list:
    symbol_positions = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if not char.isnumeric() and char not in ".\n":
                symbol_positions.append((x, y, char))
    return symbol_positions


def get_part_numbers(lines: list[str], symbol_positions: list) -> list:
    part_numbers = []
    for y, line in enumerate(lines):
        num_start = 0
        num_end = 0
        number = ""
        for x, char in enumerate(line):
            if char.isnumeric():
                if number == "":
                    num_start = x
                number += char
            else:
                if number != "":
                    num_end = x
                    symbols_surrounding = list(
                        filter(
                            lambda s: s[0] >= num_start - 1
                            and s[0] <= num_end
                            and s[1] >= y - 1
                            and s[1] <= y + 1,
                            symbol_positions,
                        )
                    )
                    if symbols_surrounding:
                        part_numbers.append(int(number))
                number = ""
    return part_numbers


def main(debug=False) -> None:
    lines = read_input(debug)
    symbol_positions = get_symbol_positions(lines)
    part_numbers = get_part_numbers(lines, symbol_positions)
    print(sum(part_numbers))


if __name__ == "__main__":
    start = datetime.datetime.now()
    # main(debug=True)
    main()
    end = datetime.datetime.now()
    print("Process time: ", end - start)

# 1ST TRY: 2392 INCORRECT (too low)
# 2ND TRY: 532428 CORRECT
