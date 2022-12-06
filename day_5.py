import copy
import input_reader as ir


def move_stack(stacks):
    for move, pos1, pos2 in instructions:
        for _ in range(move):
            box = stacks[pos1].pop()
            stacks[pos2].append(box)

def move_keep_order(stacks):
    for move, pos1, pos2 in instructions:
        temp_list = []
        for _ in range(move):
            temp_list.append(stacks[pos1].pop())
        for _ in range(move):
            stacks[pos2].append(temp_list.pop())

if __name__ == "__main__":
    groups = ir.get_with_separator("\n\n")
    input_lines = groups[0].splitlines()[:-1]
    nr_containers = int(groups[0].splitlines()[-1].split()[-1])
    instructions = groups[1].splitlines()
    instructions = [ir.get_with_regex_groups_int_cast(r"move (\d+) from (\d+) to (\d+)", instruction) for instruction in instructions]

    d = {}
    for idx in range(1, nr_containers+1):
        for line in reversed(input_lines):
            if idx > len(line) / 4 + 1:
                continue
            char = line[(idx-1)*4 + 1]
            if char != " ":
                print("char", char)
                if idx not in d:
                    d[idx] = list()
                d[idx].append(char)
    d2 = copy.deepcopy(d)

    move_stack(d)
    print("".join([d[a][-1] for a in d]))

    move_keep_order(d2)
    print("".join([d2[a][-1] for a in d2]))
