import datetime, os


def read_input(debug: bool) -> str:
    filename = "debug.txt" if debug else "input.txt"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f"{current_dir}/{filename}", "r") as f:
        return f.readlines()


def get_star_positions(lines):
    star_positions = []
    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char == "*":
                star_positions.append((x, y, char))
    return star_positions


def get_parts_per_star(lines, star_positions):
    parts_per_star = {}
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
                            star_positions,
                        )
                    )
                    if symbols_surrounding:
                        for symbol in symbols_surrounding:
                            if symbol in parts_per_star.keys():
                                parts_per_star[symbol].append(int(number))
                            else:
                                parts_per_star[symbol] = [int(number)]
                number = ""
    return parts_per_star


def main(debug=False) -> None:
    lines = read_input(debug)
    star_positions = get_star_positions(lines)
    parts_per_star = get_parts_per_star(lines, star_positions)
    print(sum([v[0] * v[1] for v in parts_per_star.values() if len(v) == 2]))


if __name__ == "__main__":
    start = datetime.datetime.now()
    # main(debug=True)
    main()
    end = datetime.datetime.now()
    print("Process time: ", end - start)

# 1ST TRY: 69425265 INCORRECT (too low)
# 2ND TRY: 72337821 INCORRECT (too low)
# 3RD TRY: 84051670 CORRECT
