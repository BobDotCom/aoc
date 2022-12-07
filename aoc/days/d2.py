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
from typing import Literal

from aoc.utils import Day, part

__all__ = ("Day2",)


P2_MAPPING: dict[
    Literal["A", "B", "C"], dict[Literal["X", "Y", "Z"], Literal["X", "Y", "Z"]]
] = {
    "A": {
        "Z": "Y",  # 3 2
        "Y": "X",  # 2 1
        "X": "Z",  # 1 3
    },
    "B": {
        "Z": "Z",  # 3 3
        "Y": "Y",  # 2 2
        "X": "X",  # 1 1
    },
    "C": {
        "Z": "X",  # 3 1
        "Y": "Z",  # 2 3
        "X": "Y",  # 1 2
    },
}


def logic(value: str, p2_logic: bool = False) -> int:
    """Logic for both parts of the challenge. Takes the input and parses it, then
    returns the result.

    Parameters
    ----------
    value: str
        The input to parse.
    p2_logic: bool
        Whether to use the logic for part 2 or not.

    Returns
    -------
    int
        The result of the logic.
    """
    rt = list[tuple[Literal["A", "B", "C"], Literal["X", "Y", "Z"]]]
    # We know that our typehint is correct here, so we can use a type: ignore
    rounds: rt = [tuple(val.split()) for val in value.splitlines()]  # type: ignore
    total = 0
    for r_val in rounds:
        if p2_logic:
            r_val = (  # type: ignore[assignment]
                r_val[0],
                "XYZ"[("ABC".index(r_val[0]) + "XYZ".index(r_val[1]) - 1) % 3],
            )
        match r_val[1]:
            case "X":
                total += 1
                if r_val[0] == "C":
                    total += 6
            case "Y":
                total += 2
                if r_val[0] == "A":
                    total += 6
            case "Z":
                total += 3
                if r_val[0] == "B":
                    total += 6
    return total


class Day2(Day):
    """Day 2: Rock Paper Scissors"""

    @part(1)
    def part_1(self, value: str) -> int:
        """Part 1

        Parameters
        ----------
        value: str
            The input to parse.

        Returns
        -------
        int
            The result of the logic.
        """
        return logic(value)

    @part(2)
    def part_2(self, value: str) -> int:
        """Part 2

        Parameters
        ----------
        value: str
            The input to parse.

        Returns
        -------
        int
            The result of the logic.
        """
        return logic(value, True)


if __name__ == "__main__":
    Day2().run()
