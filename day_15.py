import pprint
import numpy as np
from numpy import dot,array,empty_like
import input_reader as ir
from collections import defaultdict

def first_version(sx, sy, bx, by):
    visited_positions = []
    add_next_iteration = [(sx, sy)]
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    while True:
        print(len(visited_positions))
        positions_to_mark_around = [x for x in add_next_iteration]
        add_next_iteration = []
        while len(positions_to_mark_around) > 0:
            pos = positions_to_mark_around.pop(0)
            for direction in directions:
                new_pos = (pos[0] + direction[0], pos[1] + direction[1])
                if new_pos not in visited_positions:
                    visited_positions.append(new_pos)
                    add_next_iteration.append(new_pos)
                    if new_pos[1] == 2000000:
                        positions_at_2000000.add(new_pos)

        if (bx, by) in visited_positions:
            return

def second_version(sx, sy, bx, by):
    directions_static = [(1, -1), (-1, -1), (-1, 1), (1, 1)]
    iterate_again = True
    pos = (sx, sy)
    while iterate_again:
        dir_idx = 0
        pos = (pos[0], pos[1] + 1) #start above the last pos
        while dir_idx < 4:
            direction = directions_static[dir_idx]
            if (bx, by) == pos:
                iterate_again = False
            if pos[1] == 2000000:
                positions_at_2000000.add(pos)

            pos = (pos[0] + direction[0], pos[1] + direction[1])
            if pos[0] == sx or pos[1] == sy:
                dir_idx = dir_idx + 1

def mark_line_2000000(sx, sy, bx, by):
    x_diff_from_beacon = abs(sx - bx)
    y_diff_from_beacon = abs(sy - by)
    height_from_center = x_diff_from_beacon + y_diff_from_beacon
    if 2000000 in range(sy - height_from_center, sy + height_from_center):
        y_diff_from_2000000 = abs(2000000 - sy)
        x_diff_from_2000000 = height_from_center - y_diff_from_2000000
        for x_pos in range(sx - x_diff_from_2000000, sx + x_diff_from_2000000):
            positions_at_2000000.add(x_pos)

def get_edge_lines(sx, sy, bx, by):
    edges = []
    x_diff_from_beacon = abs(sx - bx)
    y_diff_from_beacon = abs(sy - by)
    height_from_center = x_diff_from_beacon + y_diff_from_beacon + 1

    edges.append([(sx, sy + height_from_center), (sx + height_from_center, sy)])
    edges.append([(sx + height_from_center, sy), (sx, sy - height_from_center)])
    edges.append([(sx, sy - height_from_center), (sx - height_from_center, sy )])
    edges.append([(sx - height_from_center, sy), (sx, sy + height_from_center)])

    #edges.append([(sx -1, sy + height_from_center + 1), (sx + 1 + height_from_center, sy - 1)])
    #edges.append([(sx + height_from_center + 1, sy + 1), (sx - 1, sy - height_from_center - 1)])
    #edges.append([(sx + 1, sy - height_from_center - 1), (sx - height_from_center - 1, sy + 1 )])
    #edges.append([(sx - height_from_center -1, sy - 1), (sx + 1, sy + height_from_center + 1)])
    return edges


def get_edge_positions(sx, sy, bx, by):
    positions = []
    edges = []
    x_diff_from_beacon = abs(sx - bx)
    y_diff_from_beacon = abs(sy - by)
    height_from_center = x_diff_from_beacon + y_diff_from_beacon + 1

    directions_static = [(1, -1), (-1, -1), (-1, 1), (1, 1)]
    edges.append((sx, sy + height_from_center))
    edges.append((sx + height_from_center, sy))
    edges.append((sx, sy - height_from_center))
    edges.append((sx - height_from_center, sy))
    start_pos = (sx, sy + height_from_center)
    pos = start_pos
    direction = directions_static.pop(0)
    while True:
        #print(pos)
        positions.append(pos)
        if pos[0] in range(0, 4000000) and pos[1] in range(0, 4000000):
            d[pos] = d[pos] + 1

        pos = (pos[0] + direction[0], pos[1] + direction[1])
        if pos == start_pos:
            return positions
        if pos in edges:
            direction = directions_static.pop(0)

def get_intersect(a1, a2, b1, b2):
    """
    Returns the point of intersection of the lines passing through a2,a1 and b2,b1.
    a1: [x, y] a point on the first line
    a2: [x, y] another point on the first line
    b1: [x, y] a point on the second line
    b2: [x, y] another point on the second line
    """
    s = np.vstack([a1,a2,b1,b2])        # s for stacked
    h = np.hstack((s, np.ones((4, 1)))) # h for homogeneous
    l1 = np.cross(h[0], h[1])           # get first line
    l2 = np.cross(h[2], h[3])           # get second line
    x, y, z = np.cross(l1, l2)          # point of intersection
    if z == 0:                          # lines are parallel
        return (float('inf'), float('inf'))
    return (x/z, y/z)

if __name__ == "__main__":
    lines = ir.get_lines_with_regex_int_groups(r"Sensor at x=(-*\d+), y=(-*\d+): closest beacon is at x=(-*\d+), y=(-*\d+)")
    positions_at_2000000 = set()

    #part 1
    #for sx, sy, bx, by in lines:
    #    print("marking sensor ", sx, sy)
    #    mark_line_2000000(sx, sy, bx, by)
    #pprint.pp(len(positions_at_2000000))

    #print(get_intersect((0, 1), (0, 2), (1, 10), (1, 9)))  # parallel  lines
    #print(get_intersect((0, 1), (0, 2), (1, 10), (2, 10))) # vertical and horizontal lines
    #print(get_intersect((0, 1), (1, 2), (0, 10), (1, 9)))  # another line for fun

    #part 2
    intersections = set()
    groups = []
    #for sx, sy, bx, by in lines:
    #    edges = get_edge_lines(sx, sy, bx, by)
    #    groups.append(edges)
    #for group in groups:
    #    for edge in group:
    #        for neighbour in groups:
    #            if neighbour != group:
    #                for neighbour_edge in neighbour:
    #                    intersection = get_intersect(edge[0], edge[1], neighbour_edge[0], neighbour_edge[1])
    #                    if float('inf') not in intersection:
    #                        if intersection[0].is_integer() and intersection[1].is_integer():
    #                            min_x = min(edge[0][0], edge[1][0])
    #                            max_x = max(edge[0][0], edge[1][0])
    #                            min_y = min(edge[0][1], edge[1][1])
    #                            max_y = max(edge[0][1], edge[1][1])
    #                            if int(intersection[0]) in range(min_x, max_x) and int(intersection[1]) in range(min_y, max_y):
    #                                intersections.add((int(intersection[0]), int(intersection[1])))
    #intersections = list(intersections)
    #intersections.sort()
    #pprint.pp(intersections)
    #print(len(intersections))

    #for idx1, left in enumerate(intersections):
    #    #print("trying new iter")
    #    top = None
    #    bottom = None
    #    for idx2, i in enumerate(intersections[idx1 + 1:]):
    #        x_diff = i[0] - left[0]
    #        y_diff = i[1] - left[1]
    #        if x_diff > 1:
    #            break
    #        if y_diff == -1:
    #            bottom = i
    #        elif y_diff == 1:
    #            top = i
    #        if top is not None and bottom is not None:
    #            for right in intersections[idx1 + idx2 + 1:]:
    #                x_right_diff = right[0] - left[0]
    #                y_right_diff = right[1] - left[1]
    #                if x_right_diff > 2:
    #                    break
    #                if y_right_diff == 0:
    #                    print("left", left)
    #                    print("top", top)
    #                    print("bottom", bottom)
    #                    print("right", right)
    #                    print(left[0], left[1])
    #                    print((left[0] + 1) * 4000000 + left[1])

    d = defaultdict(lambda: 0)
    idx = 1
    #for sx, sy, bx, by in lines:
    #    print(idx, "/", len(lines))
    #    idx = idx + 1
    #    edge_positions = get_edge_positions(sx, sy, bx, by)
    #    groups.append(edge_positions)
    #
    #for key, val in d.items():
    #    if val == 4:
    #        print(key)

    positions = [(3129625, 2636475), (3321218, 3415236), (3321219, 3415235)]
    for pos in positions:
        print(pos[0] * 4000000 + pos[1])
