import json
import input_reader as ir


def iscorrectorder(p1, p2):
    for idx, i1 in enumerate(p1):
        if idx == len(p2):
            return False
        i2 = p2[idx]
        i1_islist = isinstance(i1, list)
        i2_islist = isinstance(i2, list)
        if i1_islist and i2_islist:
            iscorrect = iscorrectorder(i1, i2)
            if iscorrect is not None:
                return iscorrect
        elif i1_islist or i2_islist:
            if i1_islist:
                iscorrect = iscorrectorder(i1, [i2])
                if iscorrect is not None:
                    return iscorrect
            else:
                iscorrect = iscorrectorder([i1], i2)
                if iscorrect is not None:
                    return iscorrect
        else:
            if i1 > i2:
                return False
            elif i1 < i2:
                return True

    if len(p2) > len(p1):
        return True
    return None

if __name__ == "__main__":
    groups_strings = [group.split("\n") for group in ir.get_with_separator("\n\n")]
    groups = []
    for group_string in groups_strings:
        group = []
        for packet_string in group_string:
            res = json.loads(packet_string)
            group.append(res)
        groups.append(group)

    #part 1
    correctness = [iscorrectorder(group[0], group[1]) for group in groups]
    print("part 1: ", sum([idx+1 for idx, iscorrect in enumerate(correctness) if iscorrect]))

    #part2
    packets = [json.loads(line) for line in ir.read_input().replace("\n\n", "\n").split("\n")]
    packets.append([[2]])
    packets.append([[6]])
    packet = packets.pop()
    #sorted_list = [packet]

    #while len(packets) > 0:
    #    packet = packets.pop()
    #    insert_at_end = True
    #    for idx, packet_from_sorted_list in enumerate(sorted_list):
    #        if iscorrectorder(packet, packet_from_sorted_list):
    #            sorted_list.insert(idx, packet)
    #            insert_at_end = False
    #            break
    #    if insert_at_end:
    #        sorted_list.append(packet)

    sorted_list = sorted(packets, iscorrectorder)

    first_idx = sorted_list.index([[2]]) + 1
    second_idx = sorted_list.index([[6]]) + 1
    print("part 1: ", first_idx * second_idx)
