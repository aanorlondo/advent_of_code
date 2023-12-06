import os, datetime


def read_input(debug: bool) -> str:
    filename = "debug.txt" if debug else "input.txt"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f"{current_dir}/{filename}", "r") as f:
        return f.readlines()


wins_cache = {}


def calculate_wins(n: int) -> int:
    if n in wins_cache:
        return wins_cache[n]
    if n <= 2:
        wins_cache[n] = n
        return n
    wins_cache[n] = calculate_wins(n - 1) * 2
    return wins_cache[n]


def main(debug=False) -> None:
    wins = 0
    lines = read_input(debug)
    for line in lines:
        winning_numbers, owned_numbers = line.strip().split(":")[1].split("|")
        intersection = list(set(winning_numbers.split()) & set(owned_numbers.split()))
        nb_matches = len(intersection)
        wins += calculate_wins(nb_matches)
    print(wins)


if __name__ == "__main__":
    start = datetime.datetime.now()
    # main(debug=True)
    main()
    end = datetime.datetime.now()
    print("Process time: ", end - start)


# 1ST TRY: 26542 INCORRECT (too low)
# 2ND TRY: 32001 CORRECT
