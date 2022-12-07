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
from aoc.utils import Day, part

__all__ = ("Day1",)


def parse_input(value: str) -> list[int]:
    """Parse input into a list of ints. Takes the input in the form of integers on
    individual lines, separated into groups. Each group is separated by a blank line.
    The return value is a list of integers, where the items are the sum of the integers
    in each group.

    Parameters
    ----------
    value: str
        The input to parse.

    Returns
    -------
    list[int]
        The parsed input.
    """
    lines = value.splitlines()
    values = [0]
    for line in lines:
        if line == "":
            values.append(0)
        else:
            values[-1] += int(line)
    return values


class Day1(Day):
    """Day 1: Calorie Counting"""

    @part(1)
    def part_1(self, value: str) -> int:
        """Part 1 of the challenge. Takes the input and parses it via :func:`parse_input`,
        then returns the largest value in the list.

        Parameters
        ----------
        value: str
            The input to parse.

        Returns
        -------
        int
            The largest value in the list.
        """
        return max(parse_input(value))

    @part(2)
    def part_2(self, value: str) -> int:
        """Part 2 of the challenge. This is the same as part one, but it returns the sum
        of the top 3, instead of the top 1.

        Parameters
        ----------
        value: str
            The input to parse.

        Returns
        -------
        int
            The sum of the top 3 values in the list.
        """
        return sum(sorted(parse_input(value))[-3:])


if __name__ == "__main__":
    Day1().run()
