import argparse
import csv
import random
from pathlib import Path


def get_all_csv_files(base_directory: str | Path) -> list[Path]:
    folder = Path(base_directory)
    return list(folder.rglob("*.csv"))


def extract_words_from_files(file_paths: list[Path]) -> list[str]:
    all_words = set()

    for file_path in file_paths:
        try:
            with open(file_path, mode="r", encoding="utf-8") as file:
                csv_reader = csv.reader(file, delimiter=";")

                for row in csv_reader:
                    if not row:
                        continue

                    english_word = row[0].strip()

                    if not english_word:
                        continue

                    if len(row) >= 2 and row[1].strip():
                        translation = row[1].strip()
                        all_words.add(f"{english_word} - ({translation})")
                    else:
                        all_words.add(english_word)

        except Exception as e:
            print(f" Error reading {file_path.name}: {e}")

    return list(all_words)


def get_random_practice_words(words: list[str]) -> list[str]:
    if not words:
        return []
    count = min(20, len(words))
    return random.sample(words, count)


def main():
    parser = argparse.ArgumentParser(
        description="A script to find CSV files containing vocabulary words."
    )

    parser.add_argument(
        "folder_path",
        type=Path,
        help="Path to the folder containing CSV files (e.g., /mnt/d/my_words)",
    )

    args = parser.parse_args()
    target_folder = args.folder_path

    if not target_folder.exists() or not target_folder.is_dir():
        print(f"Error: The directory '{target_folder}' does not exist or is not a folder.")
        return

    print(f"Searching for files in: {target_folder}...\n")

    found_files = get_all_csv_files(target_folder)

    if not found_files:
        print("No CSV files found. Please check the path!")
        return

    vocabulary = extract_words_from_files(found_files)

    if not vocabulary:
        print("No words found inside the CSV files.")
        return

    practice_list = get_random_practice_words(vocabulary)

    print(f"Your {len(practice_list)} words for today's practice:\n")
    for word in practice_list:
        print(word)

if __name__ == "__main__":
    main()
