import input_reader as ir


best_flowrate = 0

class Cave:
    def __init__(self, name, flowrate, neighbours) -> None:
        self.name = name
        self.flowrate = flowrate
        self.neighbours = neighbours


def get_total_flowrate(explored_caves):
    total_flow_rate = 0
    for c in explored_caves:
        total_flow_rate = total_flow_rate + caves[c].flowrate
    return total_flow_rate

#def iterateold(cave, minute, accumulated_release, open_valves, valves_left, prepath):
#    #print("minute ", minute)
#    if minute > 30:
#        releases.append((accumulated_release, get_total_flowrate(open_valves)))
#        return
#
#    accumulated_release = accumulated_release + get_total_flowrate(open_valves)
#
#    if len(prepath) > 0:
#        #move to next room in path
#        c = prepath.pop(0)
#        #print("move to cave ", c)
#        iterate(c, minute + 1, accumulated_release, open_valves, valves_left, prepath)
#    else:
#        if len(valves_left) == 0:
#            iterate(cave, minute + 1, accumulated_release, open_valves, valves_left, prepath)
#        else:
#            #print("open valve in ", cave)
#            new_open_valves = list(open_valves) + [cave]
#            new_valves_left = list(valves_left)
#            new_valves_left.remove(cave)
#            paths_to_valves_left = find_paths_to_valves_left(cave, new_valves_left, [], cave)
#            #prune unnecessary paths
#            min_travel_paths = {}
#            for path in paths_to_valves_left:
#                end_cave = path[-1]
#                if end_cave in min_travel_paths:
#                    if len(path) < len(min_travel_paths[end_cave]):
#                        min_travel_paths[end_cave] = path
#                else:
#                    min_travel_paths[end_cave] = path
#
#            #for path in min_travel_paths.values():
#            for path in paths_to_valves_left:
#                #print("exploring new path ", path)
#                iterate(cave, minute + 1, accumulated_release, new_open_valves, new_valves_left, path)

#def find_paths_to_valves_left(current, valves_left, path, start):
#    paths = []
#
#    for neighbour in caves[current].neighbours:
#        if neighbour in valves_left:
#            paths.append([p for p in path] + [neighbour])
#
#    #print("neighbours ", caves[current].neighbours)
#    for neighbour in caves[current].neighbours:
#        if neighbour not in path and neighbour != start:
#            new_path = [p for p in path] + [neighbour]
#            paths = paths + find_paths_to_valves_left(neighbour, valves_left, new_path, start)
#    #print("paths ", paths)
#    return paths

def should_stop_iterating(minute, accumulated_release, open_valves, flow_rate):
    closed_valves = sorted(list(set(flow_caves) - set(open_valves)))
    total_projected_release = accumulated_release
    move = False
    for _ in range((30 - minute) + 1):
        if move:
            move = False
        if closed_valves:
            cave = closed_valves.pop(0)
            flow_rate = flow_rate + caves[cave].flowrate
            move = True
        total_projected_release = total_projected_release + flow_rate
    return total_projected_release <= best_flowrate

def iterate(cave, minute, accumulated_release, open_valves):
    #print("minute ", minute)
    global best_flowrate
    if minute > 30:
        #print("adding to releases")
        releases.append((accumulated_release, get_total_flowrate(open_valves)))
        if accumulated_release > best_flowrate:
            best_flowrate = accumulated_release
            print("best flowrate is now ", best_flowrate)
        return
    total_flowrate = get_total_flowrate(open_valves)

    if should_stop_iterating(minute, accumulated_release, open_valves, total_flowrate):
        return

    accumulated_release = accumulated_release + total_flowrate

    if cave not in open_valves and caves[cave].flowrate > 0:
        #print("open valve in ", cave)
        iterate(cave, minute + 1, accumulated_release, open_valves + [cave])
    for neighbour in caves[cave].neighbours:
        iterate(neighbour, minute + 1, accumulated_release, open_valves)

if __name__ == "__main__":
    flow_caves = []
    caves = {}

    for line in ir.read_input_lines():
        line = line.replace("tunnel leads to valve", "tunnels lead to valves")
        name, flowrate, neighbours = ir.get_with_regex_groups_int_cast(r"Valve (\w+) has flow rate=(\d+); tunnels lead to valves (.+)", line)
        neighbours = neighbours.split(", ")
        caves[name] = Cave(name, flowrate, neighbours)
        if caves[name].flowrate > 0:
            flow_caves.append(name)

    #start_cave = "FY"
    #explored_caves = ["FY"]
    start_cave = "AA"
    releases = []

    #for p in find_paths_to_valves_left(start_cave, flow_caves, [], start_cave):
    #    iterate(start_cave, 1, 0, [], flow_caves, p)
    #       cave, minute, accumulated_release, open_valves, valves_left, prepath):
    #iterate(start_cave, 1, 0, [], flow_caves, [])
    iterate(start_cave, 1, 0, [])

    print(sorted(releases))
    print(sorted(releases)[-1])
