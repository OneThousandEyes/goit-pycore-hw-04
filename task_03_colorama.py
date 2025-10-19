from colorama import Fore, Style
from pathlib import Path
import sys


def print_tree(base: Path, prefix: str = "") -> None:
    """Recursively print the directory tree with colors."""
    if not base.exists():
        print(f"{Fore.RED}Error: The path '{base}' does not exist.{Style.RESET_ALL}")
        return
    if not base.is_dir():
        print(f"{Fore.RED}Error: The path '{base}' is not a directory.{Style.RESET_ALL}")
        return

    entries = list(base.iterdir())

    for index, entry in enumerate(entries):
        if entry.is_dir():
            print(f"{prefix}{Fore.BLUE}{entry.name}{Style.RESET_ALL}/")
            new_prefix = prefix + ("    ")
            print_tree(entry, new_prefix)
        else:
            print(f"{prefix}{Fore.GREEN}{entry.name}{Style.RESET_ALL}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"{Fore.RED}Usage: python task_03_colorama.py <directory_path>{Style.RESET_ALL}")
        sys.exit(1)
    directory = Path(sys.argv[1])
    print_tree(directory)
