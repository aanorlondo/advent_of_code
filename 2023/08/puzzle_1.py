import os, datetime


class Node:
    def __init__(self, id: str, next: str) -> None:
        self.id = id
        left, right = next.replace("(", "").replace(")", "").split(",")
        self.next = {"L": left.strip(), "R": right.strip()}


def read_input(debug: bool) -> str:
    filename = "debug2.txt" if debug else "input.txt"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f"{current_dir}/{filename}", "r") as f:
        return f.readlines()


def main(debug=False) -> None:
    nodes = {}
    lines = read_input(debug)
    for line in lines:
        if line.strip() == "":
            continue
        if "=" not in line:
            directions = line.strip()
            continue
        id, next = line.split(" = ")
        nodes[id] = Node(id=id, next=next)
    moves, index = 0, 0
    start, destination = "AAA", "ZZZ"
    while start != destination:
        start = nodes[start].next[directions[index]]
        moves += 1
        index = (index + 1) % len(directions)
    print(moves)


if __name__ == "__main__":
    start = datetime.datetime.now()
    # main(debug=True)
    main()
    end = datetime.datetime.now()
    print("Process time: ", end - start)


# 1ST TRY: 2264 INCORRECT (too low)
# 2ND TRY: 12169 CORRECT
