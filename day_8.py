import input_reader as ir


def get_scenic_value(x, y, max_height):
    tot = max(1, len(visible_trees_in_direction2(x, y, 0, 1, max_height))) #NORTH
    tot = tot * max(1, len(visible_trees_in_direction2(x, y, -1, 0, max_height))) #WEST
    tot = tot * max(1, len(visible_trees_in_direction2(x, y, 0, -1, max_height))) #SOUTH
    tot = tot * max(1, len(visible_trees_in_direction2(x, y, 1, 0, max_height))) #EAST
    return tot

def visible_trees_in_direction1(x, y, x_inc, y_inc):
    visible_trees_in_direction = []
    visible_trees_in_direction.append((x,y))
    max_height = forest[y][x]
    x = x + x_inc
    y = y + y_inc
    while x in range(0, len_x) and y in range(0, len_y):
        val = forest[y][x]
        if val > max_height:
            visible_trees_in_direction.append((x,y))
            max_height = val
        x = x + x_inc
        y = y + y_inc
    return visible_trees_in_direction

def visible_trees_in_direction2(x, y, x_inc, y_inc, max_height):
    visible_trees_in_direction = []
    x = x + x_inc
    y = y + y_inc
    while x in range(0, len_x) and y in range(0, len_y):
        val = forest[y][x]
        visible_trees_in_direction.append((x,y))
        if val >= max_height:
            break
        x = x + x_inc
        y = y + y_inc
    return visible_trees_in_direction

if __name__ == "__main__":
    forest = [[int(s) for s in line] for line in ir.read_input_lines()]
    len_x = len(forest[0])
    len_y = len(forest)
    visible_trees = set()
    for x in range(len_x):
        visible_trees.update(visible_trees_in_direction1(x, 0, 0, 1)) #top
        visible_trees.update(visible_trees_in_direction1(x, len_y-1, 0, -1)) #bottom
    for y in range(len_y):
        visible_trees.update(visible_trees_in_direction1(0, y, 1, 0)) #left side
        visible_trees.update(visible_trees_in_direction1(len_x-1, y, -1, 0)) #right side
    print("part1: ", len(visible_trees))

    scenic_values = []
    for y in range(len_y):
        for x in range(len_x):
            scenic_values.append(get_scenic_value(x, y, forest[y][x]))
    print("part2: ", max(scenic_values))
