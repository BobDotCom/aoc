"""
MIT License

Copyright (c) 2022 BobDotCom

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
from math import prod

from aoc.utils import Day, part

__all__ = ("Day8",)


def logic(value: str, part2: bool = False) -> int:
    values = [list(map(int, list(v))) for v in value.splitlines()]
    result = 0
    for row in range(len(values)):
        for col in range(len(values[row])):
            val = values[row][col]
            # if on an edge, skip
            on_edge = (
                row == 0
                or row == len(values) - 1
                or col == 0
                or col == len(values[row]) - 1
            )

            if on_edge and not part2:
                result += 1
                continue

            directions = [
                [v[col] for v in values[:row][::-1]],
                [v[col] for v in values[row + 1 :]],
                values[row][:col][::-1],
                values[row][col + 1 :],
            ]
            vals = []

            for adjacent in directions:
                for i, v in enumerate(adjacent):
                    if v >= val:
                        if part2:
                            vals.append(i + 1)
                        break
                else:
                    vals.append(max(int(not on_edge), len(adjacent)))

            if part2:
                if prod(vals) > result:
                    result = prod(vals)
            else:
                result += int(bool(vals))

    return result


class Day8(Day):
    """Day 8: Treetop Tree House"""

    @part(1)
    def part_1(self, value: str) -> int:
        return logic(value)

    @part(2)
    def part_2(self, value: str) -> int:
        return logic(value, part2=True)


if __name__ == "__main__":
    Day8().run()
