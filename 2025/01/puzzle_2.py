import os, time

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def read_input(debug: bool = False):
    file_name = "debug.txt" if debug else "input.txt"
    input_path = os.path.join(CURRENT_DIR, file_name)
    with open(input_path, "r") as file:
        return [line.strip() for line in file.readlines()]


start_time = time.time()

# PUZZLE START
OP = {
    "L": lambda x, y: (x - y) % 100,
    "R": lambda x, y: (x + y) % 100,
}


def parse_input(term: str):
    direction = term[0]
    distance = int(term[1:])
    return direction, distance


sequence = read_input(debug=True)
index_current = 50
index_before = None
counter = 0
for term in sequence:
    direction, distance = parse_input(term)
    index_before = index_current
    index_current = OP[direction](index_current, distance)
    cycles = (index_before - index_current) % 100
    counter += cycles


print(counter)
# PUZZLE END

end_time = time.time()
print(f"Execution time: {end_time - start_time} seconds")
