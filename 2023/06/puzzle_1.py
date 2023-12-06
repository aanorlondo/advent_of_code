from math import prod
import os, datetime


class Race:
    def __init__(self, time: int, distance: int) -> None:
        self.time = time
        self.distance = distance

    def win_possibilities(self) -> int:
        p = 0
        for init_speed in range(1, self.time):
            max_distance = (self.time - init_speed) * init_speed
            time_to_reach = max_distance / init_speed
            record_beaten = (
                max_distance > self.distance and init_speed + time_to_reach <= self.time
            )
            print(
                f"DEBUG - Race(t:{self.time}s, d:{self.distance}m).",
                f"If pressed: {init_speed}s, starts with speed:{init_speed}m/s.",
                f"Reaches {max_distance}m after remaining {time_to_reach}s. Beats record: {record_beaten}",
            )
            if record_beaten:
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
    wins = []
    times = tuple(map(int, lines[0].split(":")[1].strip().split()))
    distances = tuple(map(int, lines[1].split(":")[1].strip().split()))
    for t, d in zip(times, distances):
        wins.append(Race(time=t, distance=d).win_possibilities())
    print(prod(wins))


if __name__ == "__main__":
    start = datetime.datetime.now()
    # main(debug=True)
    main()
    end = datetime.datetime.now()
    print("Process time: ", end - start)


# 1ST TRY: 2344708 CORRECT
