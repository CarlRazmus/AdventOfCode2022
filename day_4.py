import input_reader as ir


def fully_overlap(r1, r2):
    return all(e in r2 for e in r1) or all(e in r1 for e in r2)

def any_overlap(r1, r2):
    return any(e in r2 for e in r1) or all(e in r1 for e in r2)

if __name__ == "__main__":
    l = ir.get_lines_with_regex_groups_int_cast(r"(\d+)-(\d+),(\d+)-(\d+)")
    l = [[range(a,b+1), range(x,y+1)] for a,b,x,y in l]

    print(len([[r1,r2] for r1, r2 in l if fully_overlap(r1,r2)]))
    print(len([[r1,r2] for r1, r2 in l if any_overlap(r1,r2)]))
