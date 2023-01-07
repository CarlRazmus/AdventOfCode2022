import input_reader as ir
from collections import defaultdict

"""
        covered_above = False
        covered_below = False
        covered_left = False
        covered_right = False
        covered_front = False
        covered_back = False

        for neighbour in obsidians:
            if obsidian == neighbour:
                continue
            if obsidian[2] < neighbour[2]:
                covered_above = True
            elif obsidian[2] > neighbour[2]:
                covered_below = True
            elif obsidian[0] > neighbour[0]:
                covered_left = True
            elif obsidian[0] < neighbour[0]:
                covered_right = True
            elif obsidian[1] < neighbour[1]:
                covered_front = True
            elif obsidian[1] > neighbour[1]:
                covered_back = True
        if covered_above and covered_below and covered_left and covered_right and covered_front and covered_back:
            total_open_sides = total_open_sides - 6
"""

def are_neighbours(o1, o2):
    xdiff = abs(o1[0] - o2[0])
    ydiff = abs(o1[1] - o2[1])
    zdiff = abs(o1[2] - o2[2])
    return (xdiff + zdiff + ydiff) == 1

def get_air_neighbours(pos):
    global world_matrix
    global max_z
    global max_y
    global max_x
    air_neighbours = []

    x = pos[0]
    y = pos[1]
    z = pos[2]
    top = (x, y , z + 1)
    if z + 1 in range(max_z + 1) and world_matrix[top] == ".":
        air_neighbours.append(top)

    down = (x, y , z - 1)
    if z - 1 in range(max_z + 1) and world_matrix[down] == ".":
        air_neighbours.append(down)

    left = (x, y - 1 , z)
    if y - 1 in range(max_y + 1) and world_matrix[left] == ".":
        air_neighbours.append(left)

    right = (x, y + 1 , z)
    if y + 1 in range(max_y + 1) and world_matrix[right] == ".":
        air_neighbours.append(right)

    front = (x - 1, y , z)
    if x - 1 in range(max_x + 1) and world_matrix[front] == ".":
        air_neighbours.append(front)

    back = (x + 1, y , z)
    if x + 1 in range(max_x + 1) and world_matrix[back] == ".":
        air_neighbours.append(back)
    return air_neighbours

def get_positions_of_air_group(start_pos):
    group_positions = []
    unexplored = [start_pos]
    while len(unexplored) > 0:
        next_pos = unexplored.pop(0)
        group_positions.append(next_pos)
        possible_neighbours = get_air_neighbours(next_pos)
        for air_neighbour in possible_neighbours:
            if air_neighbour not in group_positions and air_neighbour not in unexplored:
                unexplored.append(air_neighbour)
    return group_positions

if __name__ == "__main__":
    obsidians = ir.get_lines_with_regex_int_groups(r"(\d+),(\d+),(\d+)")
    obsidians = [(x,y,z) for x,y,z in obsidians]
    #print(sorted(obsidians, key=lambda arr: arr[0]))
#    total_open_sides = 0
#    for obsidian in obsidians:
#        open_sides = 6
#        for neighbour in obsidians:
#            if obsidian == neighbour:
#                continue
#            if are_neighbours(obsidian, neighbour):
#                open_sides = open_sides - 1
#        print(open_sides)
#        total_open_sides = total_open_sides + open_sides
#
#    print(total_open_sides)

    total_open_sides = 3466

    world_matrix = defaultdict(lambda: ".")
    obsidians = sorted(obsidians, key=lambda tup: (tup[0],tup[1],tup[2]))
    max_x = 0
    max_y = 0
    max_z = 0
    for obsidian in obsidians:
        x = obsidian[0]
        y = obsidian[1]
        z = obsidian[2]
        world_matrix[(x,y,z)] = "#"
        if x > max_x:
            max_x = x
        if y > max_y:
            max_y = y
        if z > max_z:
            max_z = z

    #start at all edges and find all air cubes on the outsides of the obsidian
    air_cubes_outside = []
    for x in range(max_x + 1):
        for y in range(max_y + 1):
            for z in range(max_z + 1):
                if (z == 0 or z == max_z) or (y == 0 or y == max_y) or (x == 0 or x == max_x):
                    pos = (x,y,z)
                    if pos not in obsidians and pos not in air_cubes_outside:
                        positions = get_positions_of_air_group(pos)
                        air_cubes_outside = air_cubes_outside + positions

    world_positions = set([(x,y,z) for z in range(max_z + 1) for y in range(max_y + 1) for x in range(max_x + 1)])
    #print(obsidians, "\n")
    #print(air_cubes_outside, "\n")
    #print(world_positions - (set(air_cubes_outside).union(set(obsidians))))
    air_pockets = world_positions - (set(air_cubes_outside).union(set(obsidians)))

    for air_pocket in air_pockets:
        air_pocket_open_sides = 6
        for neighbour in air_pockets:
            if air_pocket == neighbour:
                continue
            if are_neighbours(air_pocket, neighbour):
                air_pocket_open_sides = air_pocket_open_sides - 1
        total_open_sides = total_open_sides - air_pocket_open_sides
    print(total_open_sides)

