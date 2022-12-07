import re

from aoc.utils import Day, part


def parse_input(value: str) -> tuple[dict[int, list[str]], int]:
    # Find the first line that doesn't contain a bracket
    i, line = -1, ""
    for i, line in enumerate(value.splitlines()):
        if "[" not in line:
            break
    indexes = line.split()
    values = {}
    for index in indexes:
        loc = line.index(index)
        values[int(index)] = [
            v[loc] for v in value.splitlines()[:i] if len(v) > loc and v[loc] != " "
        ]
        # Reverse the values
        values[int(index)].reverse()
    return values, i


def logic(value: str, part1: bool) -> str:
    data, index = parse_input(value)
    for line in value.splitlines()[index + 2 :]:
        # Parse the line with regex
        regex = re.compile(r"move (?P<amount>\d+) from (?P<from>\d+) to (?P<to>\d+)")
        match = regex.match(line)
        if match is None:
            raise ValueError(f"Invalid line: {line}")
        # Get the values from the match
        amount = int(match.group("amount"))
        from_ = int(match.group("from"))
        to = int(match.group("to"))
        # Move the values
        val = data[from_][-amount:]
        if part1:
            val.reverse()
        data[to].extend(val)
        data[from_] = data[from_][:-amount]
    # Now, get the last value in each list
    print(data)
    return "".join([v[-1] for v in data.values()])


class Day5(Day):
    @part(1)
    def part_1(self, value: str) -> str:
        return logic(value, True)

    @part(2)
    def part_2(self, value: str) -> str:
        return logic(value, False)


if __name__ == "__main__":
    Day5().run()
