import inspect
import re
import os
import requests


AOC_URL = "https://adventofcode.com/2021/day"

def puzzle_data_exists(day):
    return f"day_{day}.txt" in os.listdir("inputs")

def create_puzzle_data(day):
    print(f"creating new puzzle data for day {day}")
    jar = requests.cookies.RequestsCookieJar()
    jar.set('session', os.getenv("AOC_SESSION_COOKIE"))
    response = requests.get(f"{AOC_URL}/{day}/input", cookies=jar, timeout=5)

    if response.ok:
        with open(f"inputs/day_{day}.txt", "w", encoding="UTF-8") as file:
            file.write(response.text)

def read_test_input():
    with open("inputs/test_data.txt", encoding="UTF-8") as file:
        return [line.rstrip('\n') for line in file]

def get_current_day_and_generate_input_data():
    calling_file = [stack.filename for stack in inspect.stack() if "AdventOfCode" in stack.filename][-1]
    day = re.search(r"\d{1,2}", calling_file.split("\\")[-1]).group(0)

    if not puzzle_data_exists(day):
        create_puzzle_data(day)
    return day

def read_input():
    day = get_current_day_and_generate_input_data()

    with open(f"inputs/day_{day}.txt", "r", encoding="UTF-8") as file:
        return file.read()

def read_input_lines():
    day = get_current_day_and_generate_input_data()

    with open(f"inputs/day_{day}.txt", "r", encoding="UTF-8") as file:
        return [line.rstrip('\n') for line in file]


def get_lines_as_int(lines):
    return [get_lines_as_int(line) for line in lines]

def get_lines_as_ints(lines):
    return [get_as_ints(line) for line in lines]

def get_lines_as_string(lines, split_cond=None):
    return [get_as_string(line, split_cond) for line in lines]

def get_lines_with_regex(expr, lines, group_idx=0):
    return [get_with_regex(expr, l, group_idx=group_idx) for l in lines]

def get_lines_with_regex_with_int_cast(expr, lines, group_idx=0):
    return [get_with_regex_with_int_cast(expr=expr, line=line, group_idx=group_idx) for line in lines]

def get_lines_with_regex_groups(expr, lines):
    return [get_with_regex_groups(expr=expr, line=line) for line in lines]

def get_lines_with_regex_groups_int_cast(expr, lines):
    return [get_with_regex_groups_int_cast(expr=expr, line=line) for line in lines]


def get_as_int(line):
    return int(line)

def get_as_ints(line, split_cond=None):
    return [int(y) for y in line.split(split_cond)]

def get_as_string(lines):
    return lines

def get_as_strings(line, split_cond=None):
    return [y for y in line.split(split_cond)]

def get_with_regex(expr, line, group_idx=0):
    return [m.group(group_idx) for m in [re.search(expr, line)] if m]

def get_with_regex_with_int_cast(expr, line, group_idx=0):
    return [int(m.group(group_idx)) if m.group(group_idx).isnumeric() else m.group(group_idx) for m in [re.search(expr, line)] if m]

def get_with_regex_groups(expr, line):
    return [m.groups() for m in [re.search(expr, line)] if m]

def get_with_regex_groups_int_cast(expr, line):
    return [[int(x) if x.isnumeric() else x for x in m.groups()] for m in [re.search(expr, line)] if m]

def get_with_separator(separator):
    return read_input().split(separator)
