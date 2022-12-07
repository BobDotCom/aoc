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
import collections
from collections.abc import Iterable, Iterator
from itertools import islice
from typing import TypeVar

from aoc.utils import Day, part

V = TypeVar("V")


def sliding_window(iterable: Iterable[V], size: int) -> Iterator[tuple[V, ...]]:
    """Create a sliding window of the given size.

    Parameters
    ----------
    iterable: Iterable[V]
        The iterable to create a sliding window of.
    size: int
        The size of the window.

    Yields
    ------
    tuple[V, ...]
        The window.
    """
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    # https://docs.python.org/3/library/itertools.html#itertools-recipes
    itr = iter(iterable)
    window = collections.deque(islice(itr, size), maxlen=size)
    if len(window) == size:
        yield tuple(window)
    for val in itr:
        window.append(val)
        yield tuple(window)


def logic(value: str, window_size: int) -> int:
    """Logic for both parts.

    Parameters
    ----------
    value: str
        The input.
    window_size: int
        The size of the sliding window.

    Returns
    -------
    int
        The answer.
    """
    window = enumerate(sliding_window(value, window_size))
    for i, win in window:
        if len(set(win)) == window_size:
            return i + window_size
    raise ValueError("No valid window found")  # pragma: no cover


class Day6(Day):
    """Day 6: Tuning Trouble"""

    @part(1)
    def part_1(self, value: str) -> int:
        """Part 1.

        Parameters
        ----------
        value: str
            The input.

        Returns
        -------
        int
            The answer.
        """
        return logic(value, 4)

    @part(2)
    def part_2(self, value: str) -> int:
        """Part 2.

        Parameters
        ----------
        value: str
            The input.

        Returns
        -------
        int
            The answer.
        """
        return logic(value, 14)


if __name__ == "__main__":
    Day6().run()
