from utils import advent
from io import TextIOWrapper
import re

advent.setup(5)

move_regex = re.compile('move (\d+) from (\d+) to (\d+)')

class Instruction:
    def __init__(self, moves_number, start, end):
        self.moves_number = moves_number
        self.start = start
        self.end = end

def supply_stacks_part_one(input_data) -> None:
    stacks = get_stacks_configuration()
    for line in input_data:
        move = line.strip()
        if not move:  # Skip empty lines
            continue

        match = move_regex.match(move)
        if match is None:
            continue

        moves_number, start, end = map(int, match.groups())
        instruction = Instruction(moves_number, start - 1, end - 1)
        move_crate(stacks, instruction)
    print(f"[1] Crate on top of each stack with CrateMover 9000: {get_solution(stacks)}")

def supply_stacks_part_two(input_data) -> None:
    stacks = get_stacks_configuration()
    for line in input_data:
        move = line.strip()
        if not move:  # Skip empty lines
            continue

        match = move_regex.match(move)
        if match is None:
            continue

        moves_number, start, end = map(int, match.groups())
        instruction = Instruction(moves_number, start - 1, end - 1)
        move_multiple_crates(stacks, instruction)
    print(f"[2] Crate on top of each stack with CrateMover 9001: {get_solution(stacks)}")


def read_configuration(file: TextIOWrapper):
    # Discard first 10 lines
    for _ in range(9):
        file.readline()
        # print(config_row, end='') # Crates Configuration
    return get_stacks_configuration()


def move_crate(stacks, instruction: Instruction) -> None:
    moves_number = instruction.moves_number
    while moves_number > 0:
        crate = stacks[instruction.start].pop()
        stacks[instruction.end].append(crate)
        moves_number -= 1

def move_multiple_crates(stacks, instruction: Instruction) -> None:
    temp_stack = []
    moves_number = instruction.moves_number
    while moves_number > 0:
        crate = stacks[instruction.start].pop()
        temp_stack.append(crate)
        moves_number -= 1
    while len(temp_stack) > 0:
        stacks[instruction.end].append(temp_stack.pop())

def get_solution(stacks):
    solution = ''
    for s in stacks:
        solution += s[-1]
    return solution


'''
[N]             [R]             [C]
[T] [J]         [S] [J]         [N]
[B] [Z]     [H] [M] [Z]         [D]
[S] [P]     [G] [L] [H] [Z]     [T]
[Q] [D]     [F] [D] [V] [L] [S] [M]
[H] [F] [V] [J] [C] [W] [P] [W] [L]
[G] [S] [H] [Z] [Z] [T] [F] [V] [H]
[R] [H] [Z] [M] [T] [M] [T] [Q] [W]
 1   2   3   4   5   6   7   8   9
'''
def get_stacks_configuration():
    stacks = []
    stacks.append(['R', 'G', 'H', 'Q', 'S', 'B', 'T', 'N'])
    stacks.append(['H', 'S', 'F', 'D', 'P', 'Z', 'J'])
    stacks.append(['Z', 'H', 'V'])
    stacks.append(['M', 'Z', 'J', 'F', 'G', 'H'])
    stacks.append(['T', 'Z', 'C', 'D', 'L', 'M', 'S', 'R'])
    stacks.append(['M', 'T', 'W', 'V', 'H', 'Z', 'J'])
    stacks.append(['T', 'F', 'P', 'L', 'Z'])
    stacks.append(['Q', 'V', 'W', 'S'])
    stacks.append(['W', 'H', 'L', 'M', 'T', 'D', 'N', 'C'])
    return stacks


def main():
    input_data = advent.get_input()
    supply_stacks_part_one(input_data)
    supply_stacks_part_two(input_data)
