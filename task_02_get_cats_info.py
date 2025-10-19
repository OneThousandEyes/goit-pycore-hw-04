from pathlib import Path

# ANSI color codes for terminal output
RED = "\033[91m"
RESET = "\033[0m"

CURRENT_DIR = Path(
    "/Users/vitalii/Documents/goit_local/github/"
    "goit-pycore-hw-04/"
)


def error_message(e, err_type):
    print(f"\n{err_type}: {RED} {e} {RESET}\n")
    exit()


def get_cats_info(path):
    dict_cats_info = []
    try:
        with open(path, 'r', encoding="UTF-8") as file:
            for line in file:
                id, name, age = line.rstrip().split(',')
                dict_cats_info.append({"id": id, "name": name, "age": age})
        return dict_cats_info
    except FileNotFoundError as e:
        error_message(e, type(e).__name__)
    except Exception as e:
        error_message(e, type(e).__name__)


if __name__ == '__main__':
    cats_info = get_cats_info(CURRENT_DIR / "task_02_get_cats_info_test_file.txt")
    print(*cats_info, sep='\n')
