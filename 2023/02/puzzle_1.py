import os, datetime


def read_input(debug: bool) -> str:
    filename = "debug.txt" if debug else "input.txt"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f"{current_dir}/{filename}", "r") as f:
        return f.readlines()


TARGET = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


class Color:
    def __init__(self, qualifier) -> None:
        self.name = qualifier.strip().split(" ")[1]
        self.amount = int(qualifier.strip().split(" ")[0])


class Subset:
    def __init__(self, colors: list[Color]) -> None:
        self.colors = colors

    def count_colors(self) -> dict:
        colors = {}
        for color in self.colors:
            if color.name in colors:
                colors[color.name] += color.amount
            else:
                colors[color.name] = color.amount
        return colors


class Game:
    def __init__(self, id, subsets: list[Subset]) -> None:
        self.id = int(id)
        self.subsets = subsets


def is_possible(game: Game) -> bool:
    for subset in game.subsets:
        subset_colors = subset.count_colors()

        for color in subset_colors:
            if color not in TARGET:
                return False

            if subset_colors[color] > TARGET[color]:
                return False

    return True


def main(debug=False) -> None:
    possible_games = []
    input = read_input(debug)
    for line in input:
        id = line.split(":")[0].split("Game")[1].strip()
        sets = line.split(":")[1].split(";")
        game_subsets = []
        for subset in sets:
            subset_colors = []
            colors = subset.split(",")
            for color in colors:
                subset_colors.append(Color(qualifier=color))
            game_subsets.append(Subset(subset_colors))
        game = Game(id=id, subsets=game_subsets)
        if is_possible(game):
            possible_games.append(game.id)
    print(sum(possible_games))


if __name__ == "__main__":
    start = datetime.datetime.now()
    # main(debug=True)
    main()
    end = datetime.datetime.now()
    print("Process time: ", end - start)


# 1ST TRY: 366 FALSE (too low)
# 2ND TRY: 2545 CORRECT
