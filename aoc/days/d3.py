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
import string
from collections.abc import Iterable, Iterator
from itertools import islice
from typing import TypeVar

from aoc.utils import Day, part

V = TypeVar("V")


def batched(iterable: Iterable[V], size: int) -> Iterator[list[V]]:
    """Batch data into lists of length ``size``. The last batch may be shorter.

    Parameters
    ----------
    iterable: Iterable[V]
        The iterable to batch.
    size: int
        The size of the batches.

    Returns
    -------
    list[V]
        The batches.
    """
    # batched('ABCDEFG', 3) --> ABC DEF G
    # https://docs.python.org/3/library/itertools.html#itertools-recipes
    itr = iter(iterable)
    while batch := list(islice(itr, size)):
        yield batch


class Day3(Day):
    """Day 3: Rucksack Reorganization"""

    @part(1)
    def part_1(self, value: str) -> int:
        """Part 1 of the challenge.

        Parameters
        ----------
        value: str
            The input to parse.

        Returns
        -------
        int
            The answer to the challenge.
        """
        total = 0

        for line in value.splitlines():
            comp1 = line[: len(line) // 2]
            comp2 = line[len(line) // 2 :]
            for letter in comp1:
                if letter in comp2:
                    total += string.ascii_letters.index(letter) + 1
                    break
        return total

    @part(2)
    def part_2(self, value: str) -> int:
        """Part 2 of the challenge.

        Parameters
        ----------
        value: str
            The input to parse.

        Returns
        -------
        int
            The answer to the challenge.
        """
        total = 0

        for lines in batched(value.splitlines(), 3):
            for letter in lines[0]:
                if letter in lines[1] and letter in lines[2]:
                    total += string.ascii_letters.index(letter) + 1
                    break

        return total


if __name__ == "__main__":
    Day3().run()
