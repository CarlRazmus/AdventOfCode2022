import input_reader as ir


if __name__ == "__main__":
    x_register = 1
    check_cycles = [20, 60, 100, 140, 180, 220]
    signal_strengths_sum = 0
    cycle = 1

    i = [l.split() for l in ir.read_input_lines()]
    n = []
    for l in i:
        if len(l) == 2:
            n.append([l[0], int(l[1])])
        else:
            n.append([l[0], 0])

    for command, val in n:
        if cycle in check_cycles:
            signal_strengths_sum = signal_strengths_sum + cycle * x_register
        if command == "addx":
            cycle = cycle + 1
            if cycle in check_cycles:
                signal_strengths_sum = signal_strengths_sum + cycle * x_register
            x_register = x_register + val
        cycle = cycle + 1

    print(signal_strengths_sum)


    #part 2
    crt = ""
    spritepos = 1
    pixelpos = 0
    for command, val in n:
        pixel = "#" if pixelpos in range(spritepos - 1, spritepos + 2) else "."
        crt = crt + pixel
        if pixelpos == 39:
            print(crt)
            crt = ""
            pixelpos = 0
        else:
            pixelpos = pixelpos + 1

        if command == "addx":
            pixel = "#" if pixelpos in range(spritepos - 1, spritepos + 2) else "."
            crt = crt + pixel
            if pixelpos == 39:
                print(crt)
                crt = ""
                pixelpos = 0
            else:
                pixelpos = pixelpos + 1
            spritepos = spritepos + val
