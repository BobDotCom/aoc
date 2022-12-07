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
import functools
import os
from collections.abc import Callable
from typing import Any, TypeVar

__all__ = (
    "Day",
    "part",
)


class Day:
    """Base class for all days. This class is used to store the input for the day,
    and to run the parts of the challenge.
    """

    def __init__(self, input_path: str = "inputs") -> None:
        self.input_path = input_path
        for attr in dir(self):
            if hasattr((obj := getattr(self, attr)), "__part__"):
                setattr(self, attr, obj.__part__(self))

    def get_input(self, title: int | str) -> str:
        """Get the input for the day.

        Parameters
        ----------
        title: int | str
            The title of the day.

        Returns
        -------
        str
            The input for the day.
        """
        possible_paths = [
            os.path.join(self.input_path, f"{self.get_date()}{title}.txt"),
            os.path.join(self.input_path, f"{self.get_date()}.txt"),
        ]
        for val in possible_paths:
            path = os.path.join(os.path.dirname(__file__), val)
            if os.path.exists(path):
                with open(path, encoding="utf-8") as file:
                    return file.read()
        raise FileNotFoundError(
            f"Could not find input for day {self.get_date()} part {title}"
        )

    def get_date(self) -> int | str:
        """The day of the challenge. This is used to get the input for the day.

        Returns
        -------
        int | str
            The day of the challenge.
        """
        if hasattr(self, "_date"):
            if callable(self._date):
                return str(self._date())
            return str(self._date)
        return self.__class__.__name__.lower().lstrip("day")

    def parts(self) -> list["Part"]:
        """Get a list of all parts of the challenge.

        Returns
        -------
        list[Part]
            A list of all parts of the challenge.
        """
        return [
            getattr(self, attr)
            for attr in dir(self)
            if isinstance(getattr(self, attr), Part)
        ]

    def run_part(self, title: str | int) -> Any:
        """Run a specific part of the challenge.

        Parameters
        ----------
        title: str | int
            The title of the part to run.

        Returns
        -------
        Any
            The return value of the part.
        """
        for func in self.parts():
            if func.title == title:
                return func()
        raise ValueError(f"Could not find part {title} for day {self.get_date()}")

    def run(self) -> None:
        """Run all parts of the challenge."""
        for func in self.parts():
            print(func())


SELF = TypeVar("SELF", bound=Day)


class Part:
    """A part of the challenge. To run, simply call this object or use :meth:`.call()`.

    Attributes
    ----------
    title: int | str
        The title of the part.
    func: Callable[[Day], Any]
        The function to run.
    day: Day
        The day of the challenge.
    """

    def __init__(self, func: Callable[[SELF], Any], title: int | str, day: SELF):
        """
        Parameters
        ----------
        func: Callable[[Day], Any]
            The function to run.
        title: int | str
            The title of the part.
        day: Day
            The day of the challenge.
        """
        self.title = title
        self.func = func
        self.day = day

    def __call__(self) -> Any:
        return self.call()

    def call(self) -> Any:
        """Run the part of the challenge.

        Returns
        -------
        Any
            The result of the function.
        """
        return self.func(self.day)


def part(
    title: int | str,
) -> Callable[[Callable[[SELF, str], Any]], Callable[[SELF], Any]]:
    """A decorator to mark a function as a part of the challenge.

    Parameters
    ----------
    title: int | str
        The title of the part.

    Returns
    -------
    Callable[[Callable[[Day, str], Any]], Callable[[Day], Any]]
        The decorator.
    """

    def decorator(func: Callable[[SELF, str], Any]) -> Callable[[SELF], Any]:
        @functools.wraps(func)
        def wrapper(self: SELF) -> Any:
            return func(self, self.get_input(title))

        # Ignore the type error here because we need to add this attribute
        wrapper.__part__ = lambda self: Part(wrapper, title, self)  # type: ignore[attr-defined]
        return wrapper

    return decorator
