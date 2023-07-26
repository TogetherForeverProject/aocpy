import argparse
import importlib
import os


def run_problem(problem_number):
    problem_file = f"problems/day{problem_number}/solution.py"

    if not os.path.isfile(problem_file):
        print(f"[bold red]Error:[/bold red] Problem file 'day{problem_number}.py' not found.")
        return None

    # Capture the standard output

    module = importlib.import_module(f"problems.day{problem_number}.solution")
    module.main()

def main():
    parser = argparse.ArgumentParser(description="Run Advent of Code Problems")
    parser.add_argument("-P", "--problem", type=int, required=True, help="Problem number to run")
    args = parser.parse_args()
    run_problem(args.problem)

    # print("\n[bold green]Finished![/bold green]")


if __name__ == "__main__":
    main()
