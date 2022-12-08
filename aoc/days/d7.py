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


class Item:  # pylint: disable=too-few-public-methods
    """Base class for all items in the filetree."""

    def __init__(self, name: str, parent: "Directory | None"):
        self.name = name
        self.parent = parent

    @property
    def size(self) -> int:
        """The size of the item."""
        return 0


class File(Item):
    """A file in the filetree."""

    def __init__(self, name: str, parent: "Directory | None", size: int):
        super().__init__(name, parent)
        self._size = size

    @property
    def size(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"- {self.name} (file, size={self.size})"


class Directory(Item):
    """A directory in the filetree."""

    instances: list["Directory"] = []

    def __init__(self, name: str, parent: "Directory | None"):
        super().__init__(name, parent)
        self.children: list[Item] = []
        self.instances.append(self)

    # def __repr__(self) -> str:
    #     return f"- {self.name} (dir)\n" + textwrap.indent(
    #         "\n".join(repr(f) for f in self.children), "  "
    #     )

    @classmethod
    def root(cls) -> "Directory":
        """Returns the root directory."""
        if not cls.instances:
            return cls("/", None)
        return cls.instances[0]

    def add(self, item: Item) -> None:
        """Adds an item to the directory."""
        self.children.append(item)

    def cd(self, path: str) -> "Directory":  # pylint: disable=invalid-name
        """Changes the current directory to the given path."""
        if path == "..":
            if self.parent:
                return self.parent
        elif path == "/":
            return self.instances[0]
        for child in self.children:
            if child.name == path and isinstance(child, Directory):
                return child
        new_dir = Directory(path, self)
        self.children.append(new_dir)
        return new_dir

    @property
    def size(self) -> int:
        return sum(child.size for child in self.children)

    @classmethod
    def get_sum(cls) -> int:
        """Return the sum of all instance sizes that are under 100000"""
        return sum(
            instance.size for instance in cls.instances if instance.size < 100000
        )

    @classmethod
    def free_space(cls, needed: int) -> int:
        """Available space is 70000000. We need to have``needed`` available, so find the
        smallest directory that we can delete to free up space.

        Parameters
        ----------
        needed: int
            The amount of space needed.

        Returns
        -------
        int
            The size of the smallest directory that can be deleted.
        """
        return min(
            instance.size
            for instance in cls.instances
            if instance.size > (needed - 70000000 + cls.root().size)
        )


def parse_input(value: str) -> None:
    """Parse the input and create the directory structure. All the necessary data is
    stored on the :class:`Directory` class.

    Parameters
    ----------
    value: str
        The input to parse.
    """
    Directory.instances = []
    cwd = Directory.root()
    lines = list(enumerate(value.splitlines()))
    commands = [(i, line[2:]) for i, line in lines if line.startswith("$")]
    for i, line in commands:
        if line.startswith("cd"):
            cwd = cwd.cd(line[3:])
        elif line.startswith("ls"):
            # Iterate through the lines until the next command, and add them to the filetree
            for _, data in lines[i + 1 :]:
                if data.startswith("$"):
                    break
                # If the line starts with "dir", it's a directory, otherwise it's a file
                if data.startswith("dir"):
                    cwd.cd(data[4:])
                else:
                    # Split the line into the file size and the file name
                    size, name = data.split(" ", 1)
                    cwd.add(File(name, cwd, int(size)))


class Day7(Day):
    """Day 7: No Space Left On Device"""

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
        parse_input(value)
        return Directory.get_sum()

    @part(2)
    def part_2(self, value: str) -> int:
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
        parse_input(value)
        return Directory.free_space(30000000)


if __name__ == "__main__":
    Day7().run()
