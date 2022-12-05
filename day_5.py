import input_reader as ir
import copy


def move(d):
    for move, p1, p2 in instructions:
        for _ in range(move):
            x = d[p1].pop()
            d[p2].append(x)

def move_keep_order(d):
    for move, p1, p2 in instructions:
        temp_list = []
        for _ in range(move):
            temp_list.append(d[p1].pop())
        for _ in range(move):
            d[p2].append(temp_list.pop())

if __name__ == "__main__":
    groups = ir.get_with_separator("\n\n")
    input_lines = groups[0].splitlines()
    nr_items = int(input_lines[-1].split()[-1])
    input_lines = input_lines[:-1]
    d = {}
    for idx in range(1, nr_items+1):
        for line in reversed(input_lines):
            if idx > len(line) / 4 + 1:
                continue
            char = line[(idx-1)*4 + 1]
            if char != " ":
                print("char", char)
                if idx not in d:
                    d[idx] = list()
                d[idx].append(char)

    instructions = groups[1].splitlines()
    instructions = [ir.get_with_regex_groups_int_cast(r"move (\d+) from (\d+) to (\d+)", instruction) for instruction in instructions]
    d2 = copy.deepcopy(d)
    move(d)
    print("".join([d[a][-1] for a in d]))
    move_keep_order(d2)
    print("".join([d2[a][-1] for a in d2]))
