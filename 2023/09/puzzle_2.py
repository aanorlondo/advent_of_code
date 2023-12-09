import os, datetime


def extrapolate(sequence: tuple) -> int:
    if sequence.count(0) == len(sequence):
        return sequence[-1]
    diff = tuple(sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1))
    return sequence[-1] + extrapolate(diff)


def read_input(debug: bool) -> str:
    filename = "debug.txt" if debug else "input.txt"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f"{current_dir}/{filename}", "r") as f:
        return f.readlines()


def main(debug=False) -> None:
    lines = read_input(debug)
    xvals = []
    for line in lines:
        serie = tuple(map(int, [s for s in line.strip().split()]))[::-1]
        xvals.append(extrapolate(serie))
    print(sum(xvals))


if __name__ == "__main__":
    start = datetime.datetime.now()
    # main(debug=True)
    main()
    end = datetime.datetime.now()
    print("Process time: ", end - start)

# 1ST TRY: 1031 CORRECT
