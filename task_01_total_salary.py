from pathlib import Path


# ANSI color codes for terminal output
RED = "\033[91m"
GREEN = "\033[32m"
RESET = "\033[0m"
YELLOW = "\033[33m"

CURRENT_DIR = Path(
    "/Users/vitalii/Documents/goit_local/github/"
    "goit-pycore-hw-04/"
)


def error_message(e, err_type):
    print(f"\n{err_type}: {RED} {e} {RESET}\n")
    exit()

def total_salary(path):
    """Calculate total and average salary from a file."""
    total = 0
    count = 0
    try:
        with open(path, 'r', encoding="UTF-8") as file:
            for line in file:
                member = line.rstrip().split(',')
                if len(member) == 2:
                    try:
                        salary = int(member[1])
                        total += salary
                        count += 1
                    except ValueError as e:
                        error_message(e, type(e).__name__)
                else:
                    print(f"\n{RED} Invalid line format: {line.strip()} {RESET}\n")
                    print("Це значення, на жаль, не може бути опрацьовано. \n")
                    exit()
        avg_salary = total / count if count > 0 else 0
        return total, avg_salary
    except FileNotFoundError as e:
        error_message(e, type(e).__name__)
    except Exception as e:
        error_message(e, type(e).__name__)


if __name__ == '__main__':
    total, avg_salary = total_salary(CURRENT_DIR / 'task_01_test_file1.txt')
    print(
        f"Загальна сума заробітної плати: {total}, "
        f"Середня заробітна плата: {avg_salary}"
    )
