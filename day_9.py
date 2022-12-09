import input_reader as ir

moves = {
    "U" : (0, 1),
    "R" : (1, 0),
    "D" : (0, -1),
    "L" : (-1, 0)
}

def move(pos, d):
    return tuple(map(sum,zip(pos,d)))

def get_move_direction(first, second):
    x_dir = int((first[0] - second[0]) / max(1, abs(first[0] - second[0])))
    y_dir = int((first[1] - second[1]) / max(1, abs(first[1] - second[1])))
    return (x_dir, y_dir)

def is_adjacent(first, second):
    return abs(first[0] - second[0]) <= 1 and abs(first[1] - second[1]) <= 1

def move_knot(head, tail):
    return move(tail, get_move_direction(head, tail))

def move_according_to_instructions(knots, instructions):
    visited_pos = set()
    visited_pos.add((0,0))
    tail_idx = len(knots) - 1
    for direction, steps in instructions:
        for _ in range(steps):
            knots[0] = move(knots[0], moves[direction])
            previous_knot = knots[0]
            for idx, knot in enumerate(knots[1:]):
                if not is_adjacent(previous_knot, knot):
                    knot = move_knot(previous_knot, knot)
                    knots[idx+1] = knot
                    if idx+1 == tail_idx:
                        visited_pos.add(knot)
                previous_knot = knot
    print(len(visited_pos))

if __name__ == "__main__":
    instructions = ir.get_lines_with_regex_groups_int_cast(r"(\w) (\d+)")

    knots = [(0,0) for _ in range(2)]
    move_according_to_instructions(knots, instructions)

    knots = [(0,0) for _ in range(10)]
    move_according_to_instructions(knots, instructions)

