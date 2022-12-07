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


def parse_input(value: str) -> list[list[list[int]]]:
    """Parses the input into groups.

    Parameters
    ----------
    value: str
        The input to parse.

    Returns
    -------
    list[list[list[int]]]
        The parsed input.
    """
    return [
        [
            list(
                range(
                    int(x.split("-")[0]),
                    int(x.split("-")[1]) + 1,
                )
            )
            for x in group.split(",")
        ]
        for group in value.splitlines()
    ]


class Day4(Day):
    """Day 4: Camp Cleanup"""

    @part(1)
    def part_1(self, value: str) -> int:
        """Part 1 of the challenge. Takes the input and parses it, then returns the
        result.

        Parameters
        ----------
        value: str
            The input to parse.

        Returns
        -------
        int
            The result of the challenge.
        """
        groups = parse_input(value)
        total = 0
        for group in groups:
            start_len = len(group[1])
            for item in group[0]:
                if item in group[1]:
                    group[1].remove(item)
            total += bool(
                len(group[1]) == 0 or len(group[0]) == start_len - len(group[1])
            )
        return total

    @part(2)
    def part_2(self, value: str) -> int:
        """Part 2 of the challenge. Takes the input and parses it, then returns the
        result.

        Parameters
        ----------
        value: str
            The input to parse.

        Returns
        -------
        int
            The result of the challenge.
        """
        groups = parse_input(value)
        total = 0
        for group in groups:
            total += int(any(item in group[1] for item in group[0]))
        return total


if __name__ == "__main__":
    Day4().run()
