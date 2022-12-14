from collections import defaultdict
import input_reader as ir


def get_move_direction(first, second):
    x_dir = int((second[0] - first[0]) / max(1, abs(second[0] - first[0])))
    y_dir = int((second[1] - first[1]) / max(1, abs(second[1] - first[1])))
    return (x_dir, y_dir)

def drop_sand_unit(simulate_floor_at_max_depth=False):
    pos = (500, 0)
    move_dirs = [(0, 1), (-1, 1), (1, 1)]

    while True:
        old_pos = pos
        for move_dir in move_dirs:
            new_pos = (pos[0] + move_dir[0], pos[1] + move_dir[1])
            if d[new_pos] == ".":
                pos = new_pos
                break
        if old_pos == pos:
            d[pos] = "O"
            return True
        if simulate_floor_at_max_depth and pos[1] == max_depth:
            d[pos] = "O"
            return True
        elif pos[1] == max_depth + 1:
            return False

def add_stones_to_map():
    lines = [[[int(x) for x in g.split(",")] for g in line.split(" -> ")] for line in ir.read_input_lines()]
    for positions in lines:
        paths = list(zip(positions, positions[1:]))
        for path in paths:
            start = path[0]
            end = path[1]
            move_dir = get_move_direction(start, end)
            curr_pos = (start[0], start[1])
            for _ in range(max(abs(start[0] - end[0]), abs(start[1] - end[1])) + 1):
                d[curr_pos] = "#"
                curr_pos = (curr_pos[0] + move_dir[0], curr_pos[1] + move_dir[1])

d = defaultdict(lambda: ".")
if __name__ == "__main__":
    add_stones_to_map()
    max_depth = max([pos[1] - 1 for pos in d])

    #part 1
    cnt = 0
    while drop_sand_unit():
        cnt = cnt + 1
    print(cnt)

    #part 2
    max_depth = max_depth + 2
    while d[(500, 0)] != "O":
        drop_sand_unit(simulate_floor_at_max_depth=True)
        cnt = cnt + 1
    print(cnt)
