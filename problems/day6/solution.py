from utils import advent
from collections import deque

advent.setup(6)

class SlidingWindow:
    def __init__(self, initial_string: str):
        self.characters_occurrence_map: dict[str, int] = {}  # Dictionary to keep track of character occurrences
        self.characters_added: int = len(initial_string)  # Number of characters added to the sliding window
        self.marker: deque = deque(maxlen=self.characters_added)  # Deque to store the sliding window

        # Initialize the sliding window with the provided initial_string
        for c in initial_string:
            self.marker.append(c)  # Add character to the sliding window
            occurrences = self.characters_occurrence_map.get(c, 0)
            self.characters_occurrence_map.update({c: occurrences + 1})  # Update character occurrences

    def slide(self, new_character: str) -> None:
        old_character = self.marker.popleft()  # Remove the oldest character from the sliding window
        old_character_occurrences = self.characters_occurrence_map.get(old_character)
        if old_character_occurrences is not None:
            self.characters_occurrence_map.update({old_character: old_character_occurrences - 1})

        new_character_occurrences = self.characters_occurrence_map.get(new_character, 0)
        self.characters_occurrence_map.update({new_character: new_character_occurrences + 1})

        self.characters_added += 1
        self.marker.append(new_character)  # Add the new character to the sliding window

    def is_valid_marker(self) -> bool:
        for c in self.marker:
            occurrences = self.characters_occurrence_map.get(c)
            if occurrences is not None and occurrences > 1:
                return False  # If any character has more than one occurrence, the marker is not valid
        return True

    def get_marker(self) -> str:
        return "".join(self.marker)  # Return the sliding window as a single string (the marker)

def tuning_trouble_part_one(input_data):
    initial_string = "".join(input_data)  # Join all lines into a single string
    sliding_window = SlidingWindow(initial_string[:4])  # Initialize with the first 4 characters
    for char in initial_string[4:]:  # Start from the 5th character, as the first 4 are already processed
        sliding_window.slide(char)
        if sliding_window.is_valid_marker():
            break  # Exit the loop as soon as the marker is detected
    return sliding_window.get_marker(), sliding_window.characters_added

def tuning_trouble_part_two(input_data):
    initial_string = "".join(input_data)  # Join all lines into a single string
    sliding_window = SlidingWindow(initial_string[:14])  # Initialize with the first 4 characters
    for char in initial_string[14:]:  # Start from the 5th character, as the first 4 are already processed
        sliding_window.slide(char)
        if sliding_window.is_valid_marker():
            break  # Exit the loop as soon as the marker is detected
    return sliding_window.get_marker(), sliding_window.characters_added


def main():
    input_data = advent.get_input()
    marker, character = tuning_trouble_part_one(input_data)
    marker1, character1 = tuning_trouble_part_two(input_data)

    advent.print_answer(1, f"Packer marker <{marker}> occurs after {character} characters")
    advent.print_answer(2, f"Packer marker <{marker1}> occurs after {character1} characters")
