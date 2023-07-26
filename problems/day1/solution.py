from utils.file import get_input_file_string

def calorie_counting_part_one(input_data):
    elves = input_data.strip().split("\n\n")  # Split input into groups of Calorie values for each Elf

    max_calories = 0
    max_calories_elf_id = None  # Initialize the variable to store the ID of the elf with maximum calories

    for elf_id, elf in enumerate(elves):
        calories = [int(calorie) for calorie in elf.split()]  # Convert Calorie values to integers
        total_calories = sum(calories)

        if total_calories > max_calories:
            max_calories = total_calories
            max_calories_elf_id = elf_id

    return max_calories_elf_id, max_calories


def calorie_counting_part_two(input_data):
    # Split the input_data into lines
    lines = input_data.strip().split("\n")

    # Create a list to store the total calories of each Elf
    elves_calories = []

    # Initialize a variable to keep track of the current Elf's calories
    current_elf_calories = 0

    for line in lines:
        # If the line is not empty, update the current Elf's calories
        if line.strip():
            current_elf_calories += int(line)
        # If the line is empty, it indicates the end of the current Elf's inventory
        else:
            # Add the current Elf's calories to the list
            elves_calories.append(current_elf_calories)
            # Reset the current Elf's calories for the next Elf
            current_elf_calories = 0

    # Add the last Elf's calories to the list
    elves_calories.append(current_elf_calories)

    # Sort the list of Elves' calories in descending order
    elves_calories.sort(reverse=True)

    # Get the top three Elves' calories and sum them
    top_three_calories_total = sum(elves_calories[:3])

    return top_three_calories_total

def main():
    input_data = get_input_file_string(1)

    id, result = calorie_counting_part_one(input_data)
    result1 = calorie_counting_part_two(input_data)

    print(f"[1] Max calories owner is elf number {id} with {result} calories")
    print(f"[2] The sum of calories carried by the top 3 elves: {result1}")
