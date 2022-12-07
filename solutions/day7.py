# Day 7
from pathlib import Path
import re


class File(object):

    def __init__(self, name='', size=0):
        self.name = name
        self.size = size

    def size_of(self):
        return self.size


class Dir(object):

    def __init__(self, name='', parent=None, children=None):
        if children is None:
            children = []
        self.name = name
        self.parent = parent
        self.children = children

    def size_of(self) -> int:
        return sum([child.size_of() for child in self.children])

    def cd(self, dir: str):
        if dir == '..':
            return self.parent
        else:
            for child in self.children:
                if child.name == dir:
                    return child

    def print_dir(self):
        print(f"dir: {self.name}; size: {self.size_of()}; parent: {self.parent.name if self.parent else 'None'}; children: {[child.name for child in self.children if child]} \n")


class FileSystem(object):

    def __init__(self, data='', root=Dir('/')):
        self.root = root
        self.current_dir = self.root
        self.dir_list = []
        for cmd in data.split('$')[2:]:
            if cmd[:3] == ' ls':
                self.current_dir = self.init_dir(self.current_dir, remove(cmd[3:].split('\n'), ''))
                self.dir_list.append(self.current_dir)
            else:
                self.current_dir = self.cd(self.current_dir, re.sub('[\n ]', '', cmd[3:]))

    def init_dir(self, dir: Dir, data: list) -> Dir:
        for item in data:
            x = item.split()
            if x[0] == 'dir':
                dir.children.append(Dir(x[1], dir, []))
            elif x[0].isdigit():
                dir.children.append(File(x[1], int(x[0])))
            else:
                print("WARNING: Item in dir is neither file nor directory.")
        return dir

    def cd(self, dir: Dir, cmd: str) -> Dir | None:
        if cmd == '..':
            return dir.parent
        else:
            for child in dir.children:
                if child.name == cmd:
                    return child
            print(f"Error: No Directory named {cmd}")
            return None

    def print_dirs(self):
        for dir in self.dir_list:
            dir.print_dir()


def remove(l: list, element) -> list:
    return [x for x in l if x != element]

def main():
    input = Path(__file__).parent.parent.resolve() / "inputs/input7.txt"

    MAX_SIZE = 100000
    TOTAL_SPACE = 70000000
    NEEDED_SPACE = 30000000

    with open(input) as f:
        data = f.read()
        files = FileSystem(data)
        print(f"Part One {sum([dir.size_of() for dir in files.dir_list if dir.size_of() < MAX_SIZE])}")
        print(f"Part Two {min([dir.size_of() for dir in files.dir_list if dir.size_of() >= NEEDED_SPACE - (TOTAL_SPACE - files.root.size_of())])}")


if __name__ == "__main__":
    main()
