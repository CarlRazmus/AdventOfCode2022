import input_reader as ir
import re
import sys

valid_commands = ["cd", "dir", ]


class Directory():
    def __init__(self, name):
        self.name = name
        self.files = []
        self.subdirs = []

    def get_size(self):
        tot_size = 0
        for name, size in self.files:
            tot_size = tot_size + size
        for ddd in self.subdirs:
            tot_size = tot_size + d[ddd].get_size()
        return tot_size




if __name__ == "__main__":
    sys.setrecursionlimit(3000)
    i = ir.read_input_lines()
    d = {}
    dirs_stack = list()
    for line in i:
        command_line = line.split()

        if command_line[0] == "$":
            if command_line[1] == "cd":
                next_dir = line.split()[2]
                if next_dir == "..":
                    dirs_stack.pop()
                else:
                    if next_dir not in d:
                        d[next_dir] = Directory(next_dir)
                    dirs_stack.append(next_dir)
        else:
            size, file_name = line.split()
            current_dir = dirs_stack[-1]
            if size != "dir":
                existing_names = [n for n,_ in d[current_dir].files]
                if file_name not in existing_names:
                    d[current_dir].files.append((file_name, int(size)))
            else:
                d[current_dir].subdirs.append(file_name)


    #print(d)
    print("hej")
    sizes = [d[x] for x in d if d[x].get_size() < 100000]
    #for dname in d:
    #    print(d[dname].get_size())
    print(sizes)
    print(len(sizes))