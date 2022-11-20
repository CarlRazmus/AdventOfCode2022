import inspect
import re
import requests
import os


def puzzle_data_already_downloaded(day):
    return f"day_{day}.txt" in os.listdir("inputs")

def get_input():
    base_url = "https://adventofcode.com/2021/day/"
    #day = re.search(r"\d{1,2}", inspect.stack()[1].filename.split("\\")[-1]).group(0)

    day = "1"
    if not puzzle_data_already_downloaded(day):
        jar = requests.cookies.RequestsCookieJar()
        jar.set('session', os.getenv("AOC_SESSION_COOKIE"))
        response = requests.get(base_url + day + "/input", cookies=jar)
        if response.ok:
            with open(f"inputs/day_{day}.txt") as file:
                file.write(response.text, "w")

        with open(f"inputs/day_{day}.txt") as file:
            file.write(response.text, "r")



    #print(puzzle_text.text)


print(puzzle_data_already_downloaded(1))
get_input()
