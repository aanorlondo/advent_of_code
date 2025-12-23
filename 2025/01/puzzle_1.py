import os, time

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_input(debug: bool = False):
    file_name = "debug.txt" if debug else "input.txt"
    input_path = os.path.join(CURRENT_DIR, file_name)
    with open(input_path, "r") as file:
        return [line.strip() for line in file.readlines()]


OP = {
    "L": lambda x, y: (x - y) % 100,
    "R": lambda x, y: (x + y) % 100,
}


def parse_input(term: str):
    direction = term[0]
    distance = int(term[1:])
    return direction, distance


# PUZZLE
start_time = time.time()
sequence = read_input(debug=True)
index = 50
counter = 0
for term in sequence:
    direction, distance = parse_input(term)
    index = OP[direction](index, distance)
    if index == 0:
        counter += 1
print(counter)
end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")
