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
import os
from unittest.mock import patch

import pytest

from aoc.utils import Day
from aoc.utils import part as part_deco


@pytest.fixture(params=(True, False))
def example(request):
    return request.param


@pytest.fixture(params=range(1, 26))
def day(request):
    return request.param


@pytest.fixture
def day_object(day, example):
    # If file doesn't exist, skip
    print(os.path.join(__file__, "..", "aoc", "days", f"d{day}.py"))
    if not os.path.exists(
        os.path.join(os.path.dirname(__file__), "..", "aoc", "days", f"d{day}.py")
    ):
        pytest.skip(f"Day {day} doesn't exist yet")
    # Import the day
    day_file = __import__(f"aoc.days.d{day}", fromlist=["Day" + str(day)])
    day = getattr(day_file, "Day" + str(day))
    if example:
        return day(input_path=os.path.join("inputs", "examples"))
    return day()


@pytest.fixture(params=(1, 2))
def part(request):
    return request.param


@pytest.fixture
def expected(day, part, example):
    if not example:
        return {
            1: [69693, 200945],
            2: [15572, 16098],
            3: [7980, 2881],
            4: [490, 921],
            5: ["WCZTHTMPS", "BLSGJSDTS"],
            6: [1582, 3588],
            7: [1141028, 8278005],
            8: [1543, 595080],
        }.get(day, [None] * 2)[part - 1]
    else:
        return {
            1: [24000, 45000],
            2: [15, 12],
            3: [157, 70],
            4: [2, 4],
            5: ["CMZ", "MCD"],
            6: [7, 19],
            7: [95437, 24933642],
            8: [21, 8],
        }.get(day, [None] * 2)[part - 1]


def test(day, day_object, part, expected):
    assert day_object.run_part(part) == expected
    if hasattr(day_object, "reset"):
        day_object.reset()


class DayTest(Day):
    @part_deco(1)
    def part_1(self, value: str) -> int:
        return int(value)

    def get_input(self, title: int | str) -> str:
        return str(title)


def test_day():
    day = Day()
    with pytest.raises(FileNotFoundError):
        day.get_input("")
    day = DayTest()
    day._date = 1
    assert day.get_date() == "1"
    day._date = lambda: 1
    assert day.get_date() == "1"
    with patch("builtins.print") as print_mock:
        day.run()
    print_mock.assert_called_once_with(1)
    with pytest.raises(ValueError):
        day.run_part(3)
