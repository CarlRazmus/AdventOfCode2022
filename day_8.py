import input_reader as ir


def find_visible_trees_from_all_directions():
    visible_trees = set()
    #NORTH
    for x in range(len_x):
        previous_tree = -1
        for y in range(len_y):
            if forest[x][y] > previous_tree:
                visible_trees.add((x,y))
                previous_tree = forest[x][y]
    #WEST
    for y in range(len_y):
        previous_tree = -1
        for x in range(len_x):
            if forest[x][y] > previous_tree:
                visible_trees.add((x,y))
                previous_tree = forest[x][y]
    #SOUTH
    for x in range(len_x):
        previous_tree = -1
        for y in reversed(range(len_y)):
            if forest[x][y] > previous_tree:
                visible_trees.add((x,y))
                previous_tree = forest[x][y]
    #EAST
    for y in range(len_y):
        previous_tree = -1
        for x in reversed(range(len_x)):
            if forest[x][y] > previous_tree:
                visible_trees.add((x,y))
                previous_tree = forest[x][y]

def visible_trees_in_direction(x, y, x_inc, y_inc, max_val):
    scenic_value = 0
    x = x + x_inc
    y = y + y_inc
    while x in range(0, len_x) and y in range(0, len_y):
        val = forest[y][x]
        scenic_value = scenic_value + 1
        if val >= max_val:
            break
        x = x + x_inc
        y = y + y_inc
    return scenic_value if scenic_value > 0 else 1

def get_scenic_value(start_x, start_y, max_height):
    #NORTH
    tot = visible_trees_in_direction(start_x, start_y, 0, 1, max_height)
    #WEST
    tot = tot * visible_trees_in_direction(start_x, start_y, -1, 0, max_height)
    #SOUTH
    tot = tot * visible_trees_in_direction(start_x, start_y, 0, -1, max_height)
    #EAST
    tot = tot * visible_trees_in_direction(start_x, start_y, 1, 0, max_height)
    return tot

if __name__ == "__main__":
    forest = [[int(s) for s in line] for line in ir.read_input_lines()]
    len_x = len(forest[0])
    len_y = len(forest)
    print(len(find_visible_trees_from_all_directions()))

    scenic_values = []
    for y in range(len_y):
        for x in range(len_x):
            scenic_values.append(get_scenic_value(x, y, forest[y][x]))
    print(max(scenic_values))

