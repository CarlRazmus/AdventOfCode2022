import functools
import input_reader as ir

def split_in_half(line):
    half_size = int(len(line) / 2)
    return [line[:half_size], line[half_size:]]

def prio(char):
    return ord(char) - 38 if char.isupper() else ord(char) - 96

def unique(*args):
    return functools.reduce(lambda a, b: set(a).intersection(set(b)), args).pop()

def part1():
    halves = [split_in_half(l) for l in ir.read_input_lines()]
    print(sum([prio(unique(x,y)) for x, y in halves]))

def part2():
    threes = ir.findall(r"(\w+)\n(\w+)\n(\w+)\n", ir.read_input())
    print(sum([prio(unique(x,y,z)) for x,y,z in threes]))

if __name__ == "__main__":
    part1()
    part2()
