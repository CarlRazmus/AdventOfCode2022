import input_reader as ir


class Directory():

    def __init__(self, name):
        self.name = name
        self.files = []
        self.subdirs = []

    def get_size(self):
        tot_size = 0
        for _, size in self.files:
            tot_size = tot_size + size
        for ddd in self.subdirs:
            tot_size = tot_size + d[ddd].get_size()
        return tot_size

def get_dir_name():
    if len(dirs_stack) > 1:
        return "/".join(dirs_stack)
    elif len(dirs_stack) == 1:
        return dirs_stack[0]
    else:
        return ""

if __name__ == "__main__":
    i = ir.read_input_lines()
    current_dir = ""
    d = {}
    dirs_stack = list()
    for line in i:
        command_line = line.split()
        if command_line[0] == "$":
            if command_line[1] == "cd":
                next_catalog = command_line[2]
                if next_catalog == "..":
                    dirs_stack.pop()
                    current_dir = get_dir_name()
                else:
                    current_dir = get_dir_name()
                    dirs_stack.append(next_catalog)
                    next_dir = get_dir_name()
                    if next_dir not in d:
                        d[next_dir] = Directory(next_dir)
                    if current_dir != "":
                      d[current_dir].subdirs.append(next_dir)
                    current_dir = next_dir
        else:
            size, file_name = line.split()
            if size != "dir":
                existing_names = [n for n,_ in d[current_dir].files]
                if file_name not in existing_names:
                    d[current_dir].files.append((file_name, int(size)))

    sizes = [d[x].get_size() for x in d]
    small_sizes = [s for s in sizes if s < 100000]
    print(sum(small_sizes))
    space_needed = d["root"].get_size() - 40000000
    big_sizes = [s for s in sizes if s >= space_needed]
    print(sorted(big_sizes)[0])
