import os, datetime


class Race:
    def __init__(self, time: int, distance: int) -> None:
        self.time = time
        self.distance = distance

    def win_possibilities(self) -> int:
        p = 0
        for init_speed in range(1, self.time):
            max_distance = (self.time - init_speed) * init_speed
            if max_distance > self.distance:
                p += 1
            elif p > 0:
                break
        return p


def read_input(debug: bool) -> str:
    filename = "debug.txt" if debug else "input.txt"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f"{current_dir}/{filename}", "r") as f:
        return f.readlines()


def main(debug=False) -> None:
    lines = read_input(debug)
    time = int("".join(lines[0].split(":")[1].strip().split()))
    distance = int("".join(lines[1].split(":")[1].strip().split()))
    print(Race(time, distance).win_possibilities())


if __name__ == "__main__":
    start = datetime.datetime.now()
    # main(debug=True)
    main()
    end = datetime.datetime.now()
    print("Process time: ", end - start)


# 1ST TRY: 30125202 CORRECT
