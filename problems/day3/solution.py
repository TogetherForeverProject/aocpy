from utils import advent

advent.setup(3)

def rucksacks_reorganization_part_one(input_data):
    rucksacks = []
    for line in input_data:
        rucksack = line.rstrip().encode()
        length = len(rucksack)
        mid = length // 2
        compartment1, compartment2 = rucksack[:mid], rucksack[mid:length]
        rucksacks.append((compartment1, compartment2))

    return sum_of_priorities(rucksacks)

def rucksacks_reorganization_part_two(input_data):
    rucksacks = []
    idx = 0

    while idx < len(input_data):
        group = [input_data[idx].strip().encode(),
                 input_data[idx + 1].strip().encode(),
                 input_data[idx + 2].strip().encode()]
        rucksacks.append(group)
        idx += 3

    return sum_of_priorities_part_two(rucksacks)

def sum_of_priorities(rucksacks):
    total_sum = 0

    for compartment1, compartment2 in rucksacks:
        items = set(compartment1)
        for item in compartment2:
            if item in items:
                total_sum += item_to_priority(item)
                break

    return total_sum

def sum_of_priorities_part_two(rucksacks):
    total_sum = 0

    for group in rucksacks:
        common_items = find_common_items(*group)
        for item in common_items:
            total_sum += item_to_priority(item)

    return total_sum

def find_common_items(rucksack1, rucksack2, rucksack3):
    set_one = set(rucksack1)
    set_two = set(rucksack2)
    set_three = set(rucksack3)

    return set_one & set_two & set_three


def item_to_priority(item):
        A, Z, a = ord('A'), ord('Z'), ord('a')
        if A <= item <= Z:
            return item - A + 27
        else:
            return item - a + 1


def main():
    input_data = advent.get_input()
    result = rucksacks_reorganization_part_one(input_data)
    result1 = rucksacks_reorganization_part_two(input_data)
    advent.print_answer(1, f"Sum of the priorities of item type that appears in both compartments of each rucksack: {result}")
    advent.print_answer(2, f"Sum of the priorities of item type that corresponds to the badges of each three-Elf group: {result1}")
