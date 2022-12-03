import input_reader as ir

if __name__ == "__main__":
    l = [sum(ir.get_as_ints(g)) for g in ir.get_with_separator("\n\n")]
    print(max(l))
    print(sum(sorted(l)[-3:]))
