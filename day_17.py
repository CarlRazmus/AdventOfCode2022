import input_reader as ir
from collections import defaultdict

def get_next_stone(idx, highest_y):
    start_y_pos = highest_y + 4
    stone = []

    """####"""
    if idx % 5 == 0:
        stone = [(2, start_y_pos), (3, start_y_pos), (4, start_y_pos), (5, start_y_pos)]

    """.#.
       ###
       .#."""
    if idx % 5 == 1:
        stone = [(3, start_y_pos), (2, start_y_pos + 1), (3, start_y_pos + 1), (4, start_y_pos + 1), (3, start_y_pos + 2)]

    """..#"""
    """..#"""
    """###"""
    if idx % 5 == 2:
        stone = [(2, start_y_pos), (3, start_y_pos), (4, start_y_pos), (4, start_y_pos + 1), (4, start_y_pos + 2)]

    #
    #
    #
    #
    if idx % 5 == 3:
        stone = [(2, start_y_pos), (2, start_y_pos + 1), (2, start_y_pos + 2), (2, start_y_pos + 3)]

    ##
    ##
    if idx % 5 == 4:
        stone = [(2, start_y_pos), (2, start_y_pos + 1), (3, start_y_pos), (3, start_y_pos + 1)]
    return stone

if __name__ == "__main__":
    jets = [c for c in ir.read_input()]
    nr_jets = len(jets)
    jet_idx = 0
    #stones = []
    stones = defaultdict(lambda: [])
    highest_y = 0
    iteration_diffs = []
    last_highest = 0
    last_stone_idx = 0
    wrapped_around = False

    for stone_idx in range(1730 + 1740 + 1190):
        stone = get_next_stone(stone_idx, highest_y)
        #print("new stone was created", stone)
        while True:
            if jet_idx == 0:
                wrapped_around = True
            #    print("stone idx diff ", stone_idx - last_stone_idx)
            #    print("stone_idx", stone_idx)
            #    last_stone_idx = stone_idx
            #    iteration_diffs.append(highest_y - last_highest)
            #    last_highest = highest_y
            #    print(iteration_diffs[-1])
            #    print()

            #move stone by jets
            jet = jets[jet_idx]
            jet_idx = (jet_idx + 1) % nr_jets
            x_dir = 1 if jet == ">" else -1
            jetted_stone = [(pos[0] + x_dir, pos[1]) for pos in stone]

            #verify movement ok
            move_aside = True
            for jetted_pos in jetted_stone:
                if jetted_pos[0] not in range(0, 7) or jetted_pos[0] in stones[jetted_pos[1]]:
                    move_aside = False
                    break

            if move_aside:
                stone = jetted_stone

            #move stone downwards
            dropped_stone = [(pos[0], pos[1] - 1) for pos in stone]

            #verify movement ok
            has_stopped = False
            for dropped_pos in dropped_stone:
                if dropped_pos[1] == 0 or dropped_pos[0] in stones[dropped_pos[1]]:
                    has_stopped = True
                    break

            if has_stopped:
                #stones = stones + stone
                for pos in stone:
                    stones[pos[1]].append(pos[0])
                    if pos[1] > highest_y:
                        highest_y = pos[1]

                if wrapped_around == True:
                #if stone_idx % 5 == 0:
                    wrapped_around = False
                    print("stone idx diff ", stone_idx - last_stone_idx)
                    print("stone_idx", stone_idx)
                    last_stone_idx = stone_idx
                    iteration_diffs.append(highest_y - last_highest)
                    last_highest = highest_y
                    print(iteration_diffs[-1])
                    print()

                #print()
                #for y in range(highest_y, 0, -1):
                #    row = ""
                #    for x in range(0, 7):
                #        row = row + ("#" if (x, y) in stones else ".")
                #    print(row)
                break
            else:
                #print("stone dropped down one level")
                stone = dropped_stone

    #Version 1
#    for stone_idx in range(2022):
#        stone = get_next_stone(stone_idx, highest_y)
#        #print("new stone was created", stone)
#        while True:
#            if stone_idx % 5 == 0 and jet_idx == 0:
#                print("highest_y", highest_y)
#                print("stone_idx", stone_idx)
#
#            #move stone by jets
#            jet = jets[jet_idx]
#            jet_idx = (jet_idx + 1) % nr_jets
#            x_dir = 1 if jet == ">" else -1
#            jetted_stone = [(pos[0] + x_dir, pos[1]) for pos in stone]
#
#            #verify movement ok
#            move_aside = True
#            for jetted_pos in jetted_stone:
#                if jetted_pos[0] not in range(0, 7) or jetted_pos in stones:
#                    move_aside = False
#                    break
#            if move_aside:
#                stone = jetted_stone
#
#            #move stone downwards
#            dropped_stone = [(pos[0], pos[1] - 1) for pos in stone]
#
#            #verify movement ok
#            has_stopped = False
#            for dropped_pos in dropped_stone:
#                if dropped_pos[1] == 0 or dropped_pos in stones:
#                    has_stopped = True
#                    break
#            if has_stopped:
#                stones = stones + stone
#                for pos in stone:
#                    if pos[1] > highest_y:
#                        highest_y = pos[1]
#
#                #print()
#                #for y in range(highest_y, 0, -1):
#                #    row = ""
#                #    for x in range(0, 7):
#                #        row = row + ("#" if (x, y) in stones else ".")
#                #    print(row)
#                break
#            else:
#                #print("stone dropped down one level")
#                stone = dropped_stone

    print(highest_y)