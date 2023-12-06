import os, datetime


def read_input(debug: bool) -> str:
    filename = "debug.txt" if debug else "input.txt"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f"{current_dir}/{filename}", "r") as f:
        return f.readlines()


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


def calculate_power(colors_dict: dict) -> int:
    p = 1
    for color in colors_dict:
        p *= colors_dict[color]
    return p


def max_colors(game: Game) -> dict:
    game_subset_colors = [subset.count_colors() for subset in game.subsets]
    max_colors = {}
    for colors_count_dict in game_subset_colors:
        if max_colors == {}:
            max_colors = colors_count_dict.copy()
        else:
            for color in colors_count_dict:
                max_colors[color] = max(
                    colors_count_dict[color],
                    max_colors.get(color, 0),
                )
    return max_colors


def main(debug=False) -> None:
    games_powers = []
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
        games_powers.append(calculate_power(max_colors(game)))
    print(sum(games_powers))


if __name__ == "__main__":
    start = datetime.datetime.now()
    # main(debug=True)
    main()
    end = datetime.datetime.now()
    print("Process time: ", end - start)


# 1ST TRY: 78111 CORRECT
