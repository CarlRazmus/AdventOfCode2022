import input_reader as ir
from collections import defaultdict


elevations = []

def heuristic(node, goal):
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

def reconstruct_path(came_from, current):
    total_path = [current]
    while current in came_from:
        current = came_from[current]
        total_path.append(current)
    return total_path

def get_neighbours(node):
    neighbours = []
    directions = [(0,1), (1,0), (0, -1), (-1, 0)]
    x = node[0]
    y = node[1]
    for direction in directions:
        if x + direction[0] in range(matrix_width):
            if y + direction[1] in range(matrix_height):
                if is_neighbour_short_enough(node, (x + direction[0], y + direction[1])):
                    neighbours.append((x + direction[0], y + direction[1]))
    return neighbours

def is_neighbour_short_enough(node, neighbour):
    return ord(elevations[neighbour[1]][neighbour[0]]) - ord(elevations[node[1]][node[0]]) <= 1

def a_star_path(start, goal):
    openSet = [start]
    cameFrom = {}

    gScores = defaultdict(lambda: 9999999)
    gScores[start] = 0
    fScores = defaultdict(lambda: 9999999)
    fScores[start] = heuristic(start, goal)

    while len(openSet) > 0:
        minscore = 99999
        current = None

        for node in openSet:
            if fScores[node] < minscore:
                current = node
                minscore = fScores[node]

        if current == goal:
            return reconstruct_path(cameFrom, current)

        openSet.remove(current)
        for neighbor in get_neighbours(current):
            tentative_gScore = gScores[current] + 1
            if tentative_gScore < gScores[neighbor]:
                cameFrom[neighbor] = current
                gScores[neighbor] = tentative_gScore
                fScores[neighbor] = tentative_gScore + heuristic(neighbor, goal)
                if neighbor not in openSet:
                    openSet.append(neighbor)
    return []

if __name__ == "__main__":
    lines = ir.read_input_lines()
    startpos = None
    endpos = None
    for idx_y, line in enumerate(lines):
        row = []
        for idx_x, char in enumerate(line):
            if char == "S":
                row.append("a")
                startpos = (idx_x, idx_y)
            elif char == "E":
                row.append("z")
                endpos = (idx_x, idx_y)
            else:
                row.append(char)
        elevations.append(row)

    matrix_height = len(lines)
    matrix_width = len(lines[0])

    print(startpos)
    print(endpos)

    path_lenghts = []
    for idx_y, line in enumerate(lines):
        for idx_x, char in enumerate(line):
            if char == "a":
                startpos = (idx_x, idx_y)
                path = a_star_path(startpos, endpos)
                if len(path) > 0:
                    path_lenghts.append(len(path) - 1)

    print(sorted(path_lenghts)[0])