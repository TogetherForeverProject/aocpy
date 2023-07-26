from utils.file import get_input_file_data

def rock_paper_scissors_part_one(file_path):
    mapping = {
        'A': {
            'type': 'rock'
        },
        'B': {
            'type': 'paper'
        },
        'C': {
            'type': 'scissors'
        },
        'X': {
            'value': 1,
            'type': 'rock'
        },
        'Y': {
            'value': 2,
            'type': 'paper'
        },
        'Z': {
            'value': 3,
            'type': 'scissors'
        }
    }

    score = 0

    for line in file_path:
        choices = line.strip().split(' ')
        opponent = mapping[choices[0]]
        player = mapping[choices[1]]

        score += player['value']

        if opponent['type'] == player['type']:
            score += 3
        elif player['type'] == 'scissors' and opponent['type'] == 'paper':
            score += 6
        elif player['type'] == 'rock' and opponent['type'] == 'scissors':
            score += 6
        elif player['type'] == 'paper' and opponent['type'] == 'rock':
            score += 6

    return score


def rock_paper_scissors_part_two(input_data):
    mapping = {
        'A': {
            'type': 'rock',
            'desired_outcomes': {
                'X': 'scissors',
                'Y': 'rock',
                'Z': 'paper'
            }
        },
        'B': {
            'type': 'paper',
            'desired_outcomes': {
                'X': 'rock',
                'Y': 'paper',
                'Z': 'scissors'
            }
        },
        'C': {
            'type': 'scissors',
            'desired_outcomes': {
                'X': 'paper',
                'Y': 'scissors',
                'Z': 'rock'
            }
        }
    }

    player_choice_scores = {
        'rock': 1,
        'paper': 2,
        'scissors': 3
    }

    score = 0

    for line in input_data:
        choices = line.strip().split(' ')
        opponent = mapping[choices[0]]
        desired_outcome = choices[1]

        player = {
            'type': opponent['desired_outcomes'].get(desired_outcome)
        }

        score += player_choice_scores[player['type']]

        if opponent['type'] == player['type']:
            score += 3
        elif player['type'] == 'scissors' and opponent['type'] == 'paper':
            score += 6
        elif player['type'] == 'rock' and opponent['type'] == 'scissors':
            score += 6
        elif player['type'] == 'paper' and opponent['type'] == 'rock':
            score += 6

    return score


def main():
    input_data = get_input_file_data(2)

    result = rock_paper_scissors_part_one(input_data)
    result1 = rock_paper_scissors_part_two(input_data)
    print(f"[1] Total score with strategy 1: {result}")
    print(f"[2] Total score with strategy 2: {result1}")
