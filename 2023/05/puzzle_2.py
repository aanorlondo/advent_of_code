import os, datetime, random
from timeit import repeat


class ConversionRule:
    def __init__(self, destination: int, source: int, range: int) -> None:
        self.destination = destination
        self.source = source
        self.range = range

    def in_range(self, x: int) -> bool:
        return (self.source <= x) and (x <= self.source + self.range)

    def convert(self, x: int) -> int:
        return self.destination + (x - self.source)


CONVERSION_MAPS = {
    "seed-to-soil": [],
    "soil-to-fertilizer": [],
    "fertilizer-to-water": [],
    "water-to-light": [],
    "light-to-temperature": [],
    "temperature-to-humidity": [],
    "humidity-to-location": [],
}


def read_input(debug: bool) -> str:
    filename = "debug.txt" if debug else "input.txt"
    current_dir = os.path.dirname(os.path.abspath(__file__))
    with open(f"{current_dir}/{filename}", "r") as f:
        return f.readlines()


def seed_to_location(seed: int) -> int:
    for key in CONVERSION_MAPS:
        for rule in CONVERSION_MAPS[key]:
            if rule.in_range(seed):
                seed = rule.convert(seed)
                break
    return seed


def main(debug=False) -> None:
    lines = read_input(debug)
    seeds = None
    section = ""
    for line in lines:
        if line.strip() == "":
            continue
        if line.startswith("seeds:"):
            seeds = tuple(int(x) for x in line.strip().split(":")[1].strip().split())
            continue
        line_is_section_header = False
        for key in CONVERSION_MAPS:
            if line.startswith(key):
                section = key
                line_is_section_header = True
                break
        if not line_is_section_header:
            destination, source, rng = map(int, line.strip().split())
            convertion_rule = ConversionRule(
                destination=destination,
                source=source,
                range=rng,
            )
            CONVERSION_MAPS[section].append(convertion_rule)
    seed_ranges = tuple(
        [
            (seeds[i], seeds[i] + seeds[i + 1])
            for i in range(0, len(seeds), 2)
            if i + 1 < len(seeds)
        ]
    )
    min_loc = seed_to_location(seed_ranges[0][0])
    for rng in seed_ranges:
        for seed in range(rng[0], rng[1] + 1):
            min_loc = min(min_loc, seed_to_location(seed))
    print(min_loc)


if __name__ == "__main__":
    start = datetime.datetime.now()
    print("Start time: ", start)
    main(debug=True)
    # main()
    end = datetime.datetime.now()
    print("End time: ", end)
    print("Process time: ", end - start)
