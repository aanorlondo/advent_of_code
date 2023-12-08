import os, datetime
from math import lcm


class Node:
    def __init__(self, next: str) -> None:
        left, right = next.replace("(", "").replace(")", "").split(",")
        self.next = {"L": left.strip(), "R": right.strip()}


def read_input(debug: bool) -> str:
    filename = "debug3.txt" if debug else "input.txt"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f"{current_dir}/{filename}", "r") as f:
        return f.readlines()


def main(debug=False) -> None:
    nodes = {}
    start_nodes = []
    lines = read_input(debug)
    for line in lines:
        if line.strip() == "":
            continue
        if "=" not in line:
            directions = line.strip()
            continue
        id, next = line.split(" = ")
        if id.endswith("A"):
            start_nodes.append(id)
        nodes[id] = Node(next=next)
    paths = []
    for n in start_nodes:
        moves, index = 0, 0
        while not n.endswith("Z"):
            n = nodes[n].next[directions[index]]
            moves += 1
            index = (index + 1) % len(directions)
        paths.append(moves)
    print(lcm(*paths))


if __name__ == "__main__":
    start = datetime.datetime.now()
    # main(debug=True)
    main()
    end = datetime.datetime.now()
    print("Process time: ", end - start)


# 1ST TRY: 12030780859469 CORRECT
