import input_reader as ir
import time


#1class Robot:
#1    def __init__(self, produce_value) -> None:
#1        self.produce_value = produce_value
#1
#1    def produce(self):
#1        return self.produce_value
#1
#1class OreRobot(Robot):
#1    def __init__(self, ore_production) -> None:
#1        pass
#1
#1    def produce():
#1        return

iterations = 0

def find_max_geodes(minute, ore, clay, obsidian, geode, ore_robots, clay_robots, obsidian_robots, geode_robots):
    minute = minute + 1
    global iterations
    if minute == 25:
        iterations = iterations + 1
        print(iterations)
        if geode > blueprint_best_values[blueprint]:
            blueprint_best_values[blueprint] = geode
        return

    #print("minute ", minute)
    args_in_next_iteration = []
    #try building something
    build_ore_robot = False
    build_clay_robot = False
    build_obsidian_robot = False
    build_geode_robot = False

    if ore >= ore_robot_cost:
        build_ore_robot = True
    if ore >= clay_robot_cost:
        build_clay_robot = True
    if ore >= obsidian_robot_ore_cost and clay >= obsidian_robot_clay_cost:
        build_obsidian_robot = True
    if ore >= geode_robot_ore_cost and obsidian >= geode_robot_obsidian_cost:
        build_geode_robot = True

    #reap bounties
    ore = ore + ore_robots
    clay = clay + clay_robots
    obsidian = obsidian + obsidian_robots
    geode = geode + geode_robots

    args_in_next_iteration.append((minute, ore, clay, obsidian, geode, ore_robots, clay_robots, obsidian_robots, geode_robots))
    if build_ore_robot:
        print("building ore robot in minute ", minute)
        args_in_next_iteration.append((minute, ore - ore_robot_cost, clay, obsidian, geode, ore_robots + 1, clay_robots, obsidian_robots, geode_robots))
    if build_clay_robot:
        print("building clay robot in minute ", minute)
        args_in_next_iteration.append((minute, ore - clay_robot_cost, clay, obsidian, geode, ore_robots, clay_robots + 1, obsidian_robots, geode_robots))
    if build_obsidian_robot:
        print("building obsidian robot in minute ", minute)
        args_in_next_iteration.append((minute, ore - obsidian_robot_ore_cost, clay - obsidian_robot_clay_cost, obsidian, geode, ore_robots, clay_robots, obsidian_robots + 1, geode_robots))
    if build_geode_robot:
        print("building geode robot in minute ", minute)
        args_in_next_iteration.append((minute, ore - geode_robot_ore_cost, clay, obsidian - geode_robot_obsidian_cost, geode, ore_robots, clay_robots, obsidian_robots, geode_robots + 1))
    for args in args_in_next_iteration:
        find_max_geodes(*args)

def find_max_geodes2(minute, ore, clay, obsidian, geode, ore_robots, clay_robots, obsidian_robots, geode_robots):
    minute = minute + 1
    if minute == 33:
    #if minute == 25:
        if geode > blueprint_best_values[blueprint]:
            blueprint_best_values[blueprint] = geode
            #print("new best value was ", geode)
        return

    if minute >= 20 and obsidian_robots == 0:
        return

    if ore >= geode_robot_ore_cost and obsidian >= geode_robot_obsidian_cost:
        find_max_geodes2(minute, ore + ore_robots - geode_robot_ore_cost, clay + clay_robots, obsidian + obsidian_robots - geode_robot_obsidian_cost, geode + geode_robots, ore_robots, clay_robots, obsidian_robots, geode_robots + 1)
    else:
        if obsidian_robots < max_obsidian_cost and ore >= obsidian_robot_ore_cost and clay >= obsidian_robot_clay_cost:
            find_max_geodes2(minute, ore + ore_robots - obsidian_robot_ore_cost, clay + clay_robots - obsidian_robot_clay_cost, obsidian + obsidian_robots, geode + geode_robots, ore_robots, clay_robots, obsidian_robots + 1, geode_robots)
        if ore_robots < max_ore_cost and ore >= clay_robot_cost:
            find_max_geodes2(minute, ore + ore_robots - clay_robot_cost, clay + clay_robots, obsidian + obsidian_robots, geode + geode_robots, ore_robots, clay_robots + 1, obsidian_robots, geode_robots)
        if clay_robots < max_clay_cost and clay_robots == 0 and ore >= ore_robot_cost:
            find_max_geodes2(minute, ore + ore_robots - ore_robot_cost, clay + clay_robots, obsidian + obsidian_robots, geode + geode_robots, ore_robots + 1, clay_robots, obsidian_robots, geode_robots)
        find_max_geodes2(minute, ore + ore_robots, clay + clay_robots, obsidian + obsidian_robots, geode + geode_robots, ore_robots, clay_robots, obsidian_robots, geode_robots)

if __name__ == "__main__":
    lines = ir.get_lines_with_regex_groups_int_cast(r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.")
    blueprint_best_values = {}
    quality_levels = []

    start_time = time.time()
    for line in lines:
        blueprint = line[0]
        ore_robot_cost = line[1]
        clay_robot_cost = line[2]
        obsidian_robot_ore_cost = line[3]
        obsidian_robot_clay_cost = line[4]
        geode_robot_ore_cost = line[5]
        geode_robot_obsidian_cost = line[6]

        max_ore_cost = max(ore_robot_cost, clay_robot_cost, obsidian_robot_ore_cost, geode_robot_ore_cost)
        max_clay_cost = obsidian_robot_clay_cost
        max_obsidian_cost = geode_robot_obsidian_cost

        blueprint_best_values[blueprint] = 0
        start_time_iter = time.time()

        find_max_geodes2(minute=0, ore= 0, clay= 0, obsidian= 0, geode= 0, ore_robots=1, clay_robots=0, obsidian_robots=0, geode_robots=0)
        print(f"most geodes in {blueprint} was {blueprint_best_values[blueprint]}, it took {time.time() - start_time_iter} seconds")
        quality_levels.append(blueprint * blueprint_best_values[blueprint])

    print(quality_levels)
    print(sum(quality_levels))
    print(f"it took {time.time() - start_time} seconds in total for all iterations")
