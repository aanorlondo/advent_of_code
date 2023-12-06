import os, datetime


def read_input(debug: bool) -> str:
    filename = "debug.txt" if debug else "input.txt"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f"{current_dir}/{filename}", "r") as f:
        return f.readlines()


cards = {}
wins_cache = {}


def calculate_wins(id: int) -> int:
    if id in wins_cache:
        return wins_cache[id]
    nb_cards = len(cards[id])
    for card in cards[id]:
        nb_cards += calculate_wins(card)
    wins_cache[id] = nb_cards
    return wins_cache[id]


def main(debug=False) -> None:
    lines = read_input(debug)
    for line in lines:
        id = int(line.strip().split(":")[0].split()[1])
        winning_numbers, owned_numbers = line.strip().split(":")[1].split("|")
        intersection = list(set(winning_numbers.split()) & set(owned_numbers.split()))
        nb_matches = len(intersection)
        cards[id] = [] if not nb_matches else [id + i for i in range(1, nb_matches + 1)]
    nb_cards_won = len(cards)
    for id in cards:
        nb_cards_won += calculate_wins(id)
    print(nb_cards_won)


if __name__ == "__main__":
    start = datetime.datetime.now()
    # main(debug=True)
    main()
    end = datetime.datetime.now()
    print("Process time: ", end - start)

# 1ST TRY: 5037841 CORRECT
