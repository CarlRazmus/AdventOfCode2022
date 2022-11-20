import inspect
import re
import os
import requests


AOC_URL = "https://adventofcode.com/2021/day"

def puzzle_data_exists(day):
    return f"day_{day}.txt" in os.listdir("inputs")

def read_test_input():
    with open("inputs/test_data.txt", encoding="UTF-8") as file:
        return file.read()

def create_puzzle_data(day):
    print(f"creating new puzzle data for day {day}")
    jar = requests.cookies.RequestsCookieJar()
    jar.set('session', os.getenv("AOC_SESSION_COOKIE"))
    response = requests.get(f"{AOC_URL}/{day}/input", cookies=jar, timeout=5)
    if response.ok:
        with open(f"inputs/day_{day}.txt", "w", encoding="UTF-8") as file:
            file.write(response.text)

def read_input():
    calling_file = [stack.filename for stack in inspect.stack() if "AdventOfCode" in stack.filename][-1]

    day = re.search(r"\d{1,2}", calling_file.split("\\")[-1]).group(0)
    if not puzzle_data_exists(day):
        create_puzzle_data(day)

    with open(f"inputs/day_{day}.txt", "r", encoding="UTF-8") as file:
        return [line.rstrip('\n') for line in file]

def get_input_as_int(read_func=read_input):
    return [int(x) for x in read_func()]

def get_input_as_string(read_func=read_input):
    return read_func()

def get_input_with_regex(expr, occurence=0, read_func=read_input):
    return [re.search(expr, x).group(occurence) for x in read_func()]

def get_input_with_regex_groups(expr, read_func=read_input):
    return [re.search(expr, x).groups for x in read_func()]
