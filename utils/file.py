def get_input_file_data(day: int):
    with open(f"inputs/day{day}.txt", "r") as file:
        input_data = file.readlines()
    return input_data

def get_input_file_string(day: int):
    with open(f"inputs/day{day}.txt", "r") as file:
        input_data = file.read()

    return input_data
