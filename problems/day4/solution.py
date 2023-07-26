from utils.file import get_input_file_data

class Section:
    def __init__(self, start, end):
        self.start = start
        self.end = end


def camp_cleanup(input_data):
    number_of_ranges_which_fully_contains_the_other = 0
    number_of_intersections = 0

    for line in input_data:
        range_one, range_two = line.strip().split(',')
        start_one, end_one = map(int, range_one.split('-'))
        start_two, end_two = map(int, range_two.split('-'))
        s1 = Section(start_one, end_one)
        s2 = Section(start_two, end_two)

        if section_contains_the_other(s1, s2): # For Part One
            number_of_ranges_which_fully_contains_the_other += 1
        if section_overlaps_the_other(s1, s2): # For Part Two
            number_of_intersections += 1

    return number_of_ranges_which_fully_contains_the_other, number_of_intersections


def section_contains_the_other(first: Section, second: Section) -> bool:
    return first.start <= second.start <= second.end <= first.end or \
           second.start <= first.start <= first.end <= second.end

def section_overlaps_the_other(first: Section, second: Section) -> bool:
    return first.start <= second.start <= first.end <= second.end or \
           second.start <= first.start <= second.end <= first.end or \
           section_contains_the_other(first, second)

def main():
    input_data = get_input_file_data(4)
    result1, result2 = camp_cleanup(input_data)
    print(f"[1] Number of ranges which fully contain the other: {result1}")
    print(f"[2] Number of ranges intersections: {result2}")
