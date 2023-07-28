import sys

INPUT_DIR = "inputs"
DAY = -1

def setup(day):
    global DAY

    if not(1 <= day <= 25):
        log('Error: Invalid day set!\n')
        sys.exit(1)

    DAY = day

def log(s, *a):
    sys.stderr.write('[AoC] ' + s.format(*a))
    sys.stderr.flush()

def get_input():
    if DAY <= -1:
        log("Error: Please setup the day!\n")
        sys.exit(1)

    try:
        file = open(f"{INPUT_DIR}/day{DAY}.txt", "r")
        return file.readlines()
    except FileNotFoundError:
        log("Error: Day not found!\n")
        sys.exit(1)

def print_answer(part, answer):
    print(f"[{part}] {answer}")
